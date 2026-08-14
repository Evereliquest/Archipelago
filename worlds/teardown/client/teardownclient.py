import asyncio
import subprocess
import os
import json
import xml.etree.ElementTree as ET
from Utils import gui_enabled, open_filename, user_path
from CommonClient import CommonContext, get_base_parser, server_loop
from typing import Any
import typing
import re
import traceback
from items import Mission_Enable, Tool_Enable, Tool_Items, Cash_Value
from template import SAVE_TEMPLATE
from xml_path import Missionindex
from locations import Mission_Locations, Mission_Checked_Locations, Tool_Locations, Valuables_Names

SETTINGS_PATH = user_path("teardownsettings.json")

Valuable_First_ID = 800

Valuable_Locations = {
    name: Valuable_First_ID + index
    for index, name in enumerate(Valuables_Names)
}



class TeardownContext(CommonContext):
    game = "Teardown"
    tags = CommonContext.tags | {"AP"}
    items_handling = 0b111
    want_slot_data = True
    slot_data: dict[str, Any]
    last_connected_slot: int | None = None
    stored_data: dict[str, typing.Any]
    stored_data_notification_keys: set[str]
    items_received: int = 0
    locations_found: int = 0


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = "Teardown"
        self.game_exe_path = ""
        self.savegame_path = ""
        self.player_data = None
        self.loadsettings()
        self.MissionAmount = 0
        self.ToolUpgrades = True
        self.ValuableSanity = False
        self.FastGoal = False
        self.EasyGoal = False
        self.mission_count = 0
        self.items_received_event = asyncio.Event()
        self.locations_found_event = asyncio.Event()
        self.locations_checked = []
        self.last_cash = 0
        self.current_cash = 0
        self.mission_bitmask = 0
        self.cash = 0
        self.received_counts = {}
        self.applied_cash_total = 0

        self.innit_event = asyncio.Event()
        self.message_event1 = asyncio.Event()
        self.message_event2 = asyncio.Event()


    #Setup settings like exe and xml
    def loadsettings(self):
        # Load settings from the json file
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as f:
                data = json.load(f)
                self.game_exe_path = data.get("game_exe_path", "")
                self.savegame_path = data.get("savegame_path", "")

    def checkgamepath(self):
        # Ask for exe if not found
        if not self.game_exe_path or not os.path.exists(self.game_exe_path):
            if gui_enabled:
                prompt_title = "Select Teardown Executable"

                while True:
                    new_path = open_filename(
                        title=prompt_title,
                        filetypes=(("Teardown Executable", ".exe"), ("All Files", "*"))
                    )
                    if not new_path:
                        break

                    if os.path.basename(new_path) == "savegame.xml":
                        self.game_exe_path = new_path
                        self.savesettings()
                        break
                    else:
                        # Restarts the loop with new title
                        prompt_title = "INVALID: You must select 'teardown.exe'!"

        if not self.savegame_path or not os.path.exists(self.savegame_path):
            if gui_enabled:
                prompt_title = "Select Teardown savegame.xml"

                while True:
                    new_save = open_filename(
                        title=prompt_title,
                        filetypes=(("Teardown Save File", ".xml"), ("All Files", "*"))
                    )
                    if not new_save:
                        break

                    if os.path.basename(new_save) == "savegame.xml":
                        self.savegame_path = new_save
                        self.savesettings()
                        break
                    else:
                        # Restarts the loop with new title
                        prompt_title = "INVALID: You must select 'savegame.xml'!"

    def savesettings(self):
        # Save our settings to our json file
        data = {
            "game_exe_path": self.game_exe_path,
            "savegame_path": self.savegame_path
        }
        with open(SETTINGS_PATH, "w") as f:
            json.dump(data, f, indent=4)


    # Updates node in xml and creates if needed
    def update_node(self, path, value):
        node = self.player_data.find(path)
        if node is None:
            curr = self.player_data
            for part in path.split('/'):
                child = curr.find(part)
                if child is None: child = ET.SubElement(curr, part)
                curr = child
            node = curr
        node.set("value", str(value))
        #print(f"Update Node: {path} set to {value}")

    # Setup Window Name
    def run_gui(self):
        from kvui import GameManager

        class TeardownManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Teardown Client"

        self.ui = TeardownManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


    # Main functions seperater above is helpers, below is workers

    # XML setup function, does all the work in setting up save on connect
    # Still needs cleanup

    async def reset_save(self):
        print("Reset: Applying Save Template")

        if not self.savegame_path or not os.path.exists(self.savegame_path):
            return

        with open(self.savegame_path, 'r', encoding='utf-8') as f:
            text_data = f.read()
        clean_text = re.sub(r'^\s*<\d+[^>]*/>.*\n?', '', text_data, flags=re.MULTILINE)

        try:
            with open(self.savegame_path, "w", encoding='utf-8') as f:
                f.write(clean_text)

            tree = ET.parse(self.savegame_path)
            root = tree.getroot()

            self.player_data = root.find("savegame/mod/steam-3708322400")
            print(f"Reset: player_data found: {self.player_data is not None}")

            if self.player_data is None:
                mod_node = root.find("mod")
                if mod_node is None:
                    mod_node = ET.SubElement(root, "mod")
                self.player_data = ET.SubElement(mod_node, "steam-3708322400")


            for category, nodes in SAVE_TEMPLATE.items():

                print(f"Reset: Processing Category: {category}")
                cat_node = self.player_data.find(category)
                if cat_node is None:
                    print(f"Reset: Category '{category}' not found, creating new SubElement.")

                cat_node = self.player_data.find(category)
                if cat_node is None:
                    cat_node = ET.SubElement(self.player_data, category)

                for path, val in nodes.items():
                    parts = path.split('/')
                    current = cat_node
                    for i, part in enumerate(parts):
                        child = current.find(part)
                        if child is None:
                            child = ET.SubElement(current, part)
                        if i == len(parts) - 1:
                            #full_path = f"{category} -> {' -> '.join(parts)}"

                            #print(f"Reset:  [{full_path}] to value: {val}")
                            child.set("value", str(val))

                        current = child
            last_node = self.player_data.find("lastcompleted")
            if last_node is None:
                last_node = ET.SubElement(self.player_data, "lastcompleted")
            last_node.set("value", "")

            for message_node in self.player_data.findall("message"):
                self.player_data.remove(message_node)
                print(f"Reset: Pruned message node: {message_node.tag}")

            for mission_node in self.player_data.findall("mission"):
                self.player_data.remove(mission_node)
                print(f"Reset: Pruned message node: {mission_node.tag}")

            resetcash = self.player_data.find("cash")
            if resetcash is None:
                resetcash = ET.SubElement(self.player_data, "cash")

            resetcash.set("value", "0")


        except Exception as e:
            print(f"Failed to initialize player_data: {e}")
            traceback.print_exc()









    async def applying_save(self, ):
        print("Applying: Applying Progress to Save")

        if not self.savegame_path or not os.path.exists(self.savegame_path):
            return

        with open(self.savegame_path, 'r', encoding='utf-8') as f:
            text_data = f.read()
        clean_text = re.sub(r'^\s*<\d+[^>]*/>.*\n?', '', text_data, flags=re.MULTILINE)

        try:
            with open(self.savegame_path, "w", encoding='utf-8') as f:
                f.write(clean_text)

            tree = ET.parse(self.savegame_path)
            root = tree.getroot()

            self.player_data = root.find("savegame/mod/steam-3708322400")
            print(f"Initializing: player_data found: {self.player_data is not None}")

            if self.player_data is None:
                mod_node = root.find("mod")
                if mod_node is None:
                    mod_node = ET.SubElement(root, "mod")
                self.player_data = ET.SubElement(mod_node, "steam-3708322400")


            await self.apply_server_state_to_xml(self.player_data)

            bigint = getattr(self, "mission_bitmask", 0)
            current_count = bigint.bit_count()
            goal_required = getattr(self, 'MissionAmount', 20)
            print(f"Archipelago: Current Missions Count {current_count} Goal Required Count {goal_required}")

            if not self.FastGoal:
                if current_count >= goal_required:
                    if self.EasyGoal:
                        asyncio.create_task(self.send_msgs([{
                            "cmd": "StatusUpdate",
                            "status": 30,
                        }]))
                        print("Goal Sent Easy")

                    message_path = self.player_data.find("message")
                    cullington_path = self.player_data.find("cullington_bomb")

                    if cullington_path is None:
                        cullington_path = ET.SubElement(message_path, "cullington_bomb")

                    cullington_path.set("value", "1")
                    print("Archipelago: Final Mission Unlocked.")
            else:
                mission_count = sum(1 for mission_id in Mission_Enable if mission_id in self.items_received)
                if mission_count >= goal_required:
                    if self.EasyGoal:
                        asyncio.create_task(self.send_msgs([{
                            "cmd": "StatusUpdate",
                            "status": 30,
                        }]))
                        print("Goal Sent Easy")

                    message_path = self.player_data.find("message")
                    cullington_path = self.player_data.find("cullington_bomb")

                    if cullington_path is None:
                        cullington_path = ET.SubElement(message_path, "cullington_bomb")

                    cullington_path.set("value", "1")
                    print("Archipelago: Final Mission Unlocked Fast.")

            for i in range(5):  # Try 5 times
                try:
                    print(f"Initializing: Attempting initialization write {i + 1}/5")
                    ET.indent(tree, space="          ", level=0)
                    tree.write(self.savegame_path, encoding="UTF-8", xml_declaration=False)

                    print("Teardown Save: Player Data initialized and globally set.")
                    return True

                except PermissionError:
                    print("Initializing: File locked during init, retrying")
                    await asyncio.sleep(0.2)
                except Exception as e:
                    print(f"Failed to initialize player_data: {e}")
                    traceback.print_exc()
                    break

            return False

        except Exception as e:
            print(f"Failed to initialize player_data: {e}")
            traceback.print_exc()


    # Smaller Worker function for Reset Save
    # Needs Cleanup
    async def apply_server_state_to_xml(self, player_data):

        while not hasattr(self, 'items_received'):
            print("Initializing: Waiting for items to be received from server")
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)

        while not hasattr(self, 'checked_locations'):
            print("Initializing: Waiting for found locations")
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)

        self.received_counts = {}
        print(f"First Apply: Total items in items_received: {len(self.items_received)}")

        for item in self.items_received:
            item_id = item.item
            self.received_counts[item_id] = self.received_counts.get(item_id, 0) + 1
            #print(f"First Apply: Counted Item ID {item_id}")

        # 1. Sync Tools & Missions
        for mapping in [Tool_Enable, Mission_Enable]:
            for ap_id, xml_path in mapping.items():
                count = self.received_counts.get(ap_id, 0)
                if count > 0:
                    self.update_node(xml_path, "1")

        for mapping in [Mission_Enable]:
            for ap_id, xml_path in mapping.items():
                count = self.received_counts.get(ap_id, 0)
                if count > 0:
                    modified_path = xml_path.replace("mission/", "message/")
                    self.update_node(modified_path, "2")
                    print(modified_path)

        for ap_id, config in Tool_Items.items():
            count = self.received_counts.get(ap_id, 0)
            path, mult, base = config
            final_val = (count * mult) + base
            self.update_node(path, final_val)

        def missions_checked():
            group_results = {}
            received_item_ids = {network_item.item for network_item in self.items_received}

            # Cycle through ALL groups automatically
            for group_name, location_ids in Mission_Checked_Locations.items():

                prereq_id = location_ids["prereq_id"]
                location_ids = location_ids["locations"]

                # Check prerequisites
                if prereq_id not in received_item_ids:
                    group_results[prereq_id] = 0
                    continue
                # Count the checked locations
                found_count = 0
                for loc_id in location_ids:
                    if loc_id in self.checked_locations:
                        found_count += 1

                # Save the final tally
                group_results[prereq_id] = found_count
            return group_results


        print(f"First Apply: Total items in self.checked_locations: {len(self.checked_locations)}")
        print(f"First Apply: Checking Mission Sent Locations")
        current_loc = missions_checked()
        for mission_id, xml_path in Mission_Enable.items():
            new_path = xml_path + "/score"
            count = current_loc.get(mission_id, 0)
            if count > 0:
                self.update_node(new_path, str(count))


        def tools_checked():
            upgrade_results = {}

            for xml_path_tool, upgrades in Tool_Locations.items():
                sorted_amounts = sorted(upgrades.keys())

                highest_amount = None

                # 2. Check each location ID in order
                for amount in sorted_amounts:
                    loc_id = upgrades[amount]  # This grabs the Location ID (e.g., 501)

                    if loc_id in self.checked_locations:
                        # They have this location! Update the highest amount achieved.
                        highest_amount = amount
                    else:
                        # A location wasn't checked!
                        # The chain is broken, stop counting and skip to the next tool.
                        break

                        # 3. Save to results ONLY if they actually found at least one upgrade
                    # (If they found none, it leaves the game's default base value alone)
                if highest_amount is not None:
                    upgrade_results[xml_path_tool] = highest_amount

            return upgrade_results

        print(f"First Apply: Checking Tool Sent Locations")
        if self.ToolUpgrades:
            # Setting put in savegame for mod to know if to separate or give upgrade
            self.update_node("toolupgradeon", 1)
            current_upgrades = tools_checked()
            for xml_path, total_value in current_upgrades.items():
                self.update_node(xml_path, str(total_value))
        else:
            self.update_node("toolupgradeon", 0)


        def valuables_checked():
            valuable_results = {}

            for index, item_name in enumerate(Valuables_Names):

                # Calculate the ID
                current_id = Valuable_First_ID + index

                # Build the XML path
                xml_path_val = f"valuable/{item_name}"

                # Check if the player has this ID
                if current_id in self.checked_locations:
                    valuable_results[xml_path_val] = 1
                else:
                    valuable_results[xml_path_val] = 0

            return valuable_results

        print(f"First Apply: Checking Valuable Sent Locations")
        if self.ValuableSanity:
            current_valuables = valuables_checked()
            for xml_path, total_value in current_valuables.items():
                self.update_node(xml_path, str(total_value))


        # Cash Setting Below
        def cash_counted():
            self.current_cash = self.cash
            print(f"Cash Counted: Cash XML node synchronized to {self.cash}")
            print(f"Cash Counted: {self.applied_cash_total}")


            total_received_cash = sum(
                self.received_counts.get(ap_id, 0) * cash_val
                for ap_id, cash_val in Cash_Value.items()
            )

            if self.applied_cash_total is not None:
                cash_to_add = total_received_cash - self.applied_cash_total
            else:
                print(f"Cash Counted: self.applied_cash_total is None")
                cash_to_add = total_received_cash

            if cash_to_add > 0:
                self.current_cash += cash_to_add
                self.applied_cash_total = total_received_cash

                asyncio.create_task(self.send_msgs([{
                    "cmd": "Set",
                    "key": f"Teardown_Applied_Cash{self.team}_{self.slot}",
                    "default": 0,
                    "want_reply": True,
                    "operations": [{"operation": "replace", "value": total_received_cash}]
                }]))

                asyncio.create_task(self.send_msgs([{
                    "cmd": "Set",
                    "key": f"Teardown_Cash{self.team}_{self.slot}",
                    "default": 0,
                    "want_reply": True,
                    "operations": [{"operation": "replace", "value": self.current_cash}]
                }]))
                print(f"cash_counted: Updated cash on server to {self.current_cash}.")

            self.update_node("cash", self.current_cash)
            self.last_cash = self.current_cash
            print(f"Cash Counted: Cash XML node synchronized to {self.current_cash}")


        cash_counted()


    async def sync_savegame(self):
        if not self.savegame_path or not os.path.exists(self.savegame_path):
            return False

        print(f"Sync: Starting Sync")

        try:
            tree = ET.parse(self.savegame_path)
            root = tree.getroot()
            self.player_data = root.find("savegame/mod/steam-3708322400")
            original_xml_string = ET.tostring(root, encoding="unicode")
            print("Sync: Parse successful.")

        except Exception as e:
            print(f"Sync: Parse FAILED with error: {e}")
            return


        self.check_missions()
        if self.ToolUpgrades:
            self.check_tools()
        self.check_valuables()
        print("Sync: Functions ran.")

        new_xml_string = ET.tostring(root, encoding="unicode")

        if original_xml_string == new_xml_string:
            print("Sync: No changes in XML, skipping save.")
            return True

        print("Sync: XML Differences, Now Saving.")
        for i in range(5):
            try:
                print(f"Sync: Save started, attempt {i + 1}")
                ET.indent(tree, space="          ", level=0)
                tree.write(self.savegame_path, encoding="UTF-8", xml_declaration=False)
                return True  # Exit function and return to loop
            except PermissionError:
                print("Sync: File locked, waiting...")
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Sync: Critical Write Error: {e}")
                return False

        return False


    def check_missions(self):
        print("Sync Mission: Entering check_missions")
        if self.player_data is None:
            print("Sync Mission: Player Data is None")
            return

        last_node = self.player_data.find("lastcompleted")
        if last_node is None:
            print("Sync Mission: lastcompleted isn't found")
            return

        mission_id = last_node.get("value")
        if mission_id is None:
            print("Sync Mission: lastcompleted is none")
            return

        print(f"Sync Missions: Starting check_missions, lastcompleted: {mission_id}")

        if mission_id and mission_id in Mission_Locations:
            start_id = Mission_Locations[mission_id]

            print("Sync Mission: Trigger mission_counter")
            self.mission_counter(mission_id)

            mission_container = self.player_data.find("mission")
            if mission_container is not None:
                score_node = mission_container.find(f"{mission_id}/score")

                if score_node is not None:
                    current_score = int(score_node.get("value", "0"))
                    print(f"Sync Mission: Current Score is: {current_score}")

                    # Loop through the score
                    for i in range(current_score):
                        # Calculate the specific ID for this check
                        location_id = start_id + i

                        # Send the ID directly to your check function
                        self.send_upgrade_check(location_id)

            # 4. Clear the trigger in the XML data so it doesn't fire again
            last_node.set("value", "")

    def check_tools(self):
        print("Sync Tools: Entering check_tools")
        if self.player_data is None:
            return

        for xml_path, thresholds in Tool_Locations.items():
            node = self.player_data.find(xml_path)
            if node is not None:
                try:
                    current_val_str = node.get("value", "0")
                    current_val = int(current_val_str)

                    for threshold_val, location_id in thresholds.items():
                        if location_id in self.locations_checked:
                            continue
                        if current_val >= threshold_val:
                            print(f"Sync Tools: {xml_path} reached {current_val} (Target: {threshold_val}). Sending ID {location_id}")

                            self.send_upgrade_check(location_id)


                except (ValueError, TypeError) as e:
                    print(f"Sync Tools: Error processing value at {xml_path}: {e}")
            else:
                pass

    def check_valuables(self):
        print("Sync Valuables: Entering check_valuables")
        if self.player_data is None:
            return

        cash_node = self.player_data.find("cash")
        if cash_node is None:
            print("Sync Valuables: cash isn't found")
            return
        try:
            self.current_cash = int(cash_node.get("value", "0"))
        except (ValueError, TypeError):
            return
        if not hasattr(self, "last_cash"):
            self.last_cash = None

        print(f"Sync Valuables: Current Cash {self.current_cash} Last Cash {self.last_cash}")
        if self.current_cash != self.last_cash:
            print(f"Sync Valuables: Cash changed from {self.last_cash} to {self.current_cash}. Scanning valuables...")
            self.watch_cash()

            if self.ValuableSanity:
                # 3. Locate the 'valuable' base block in the XML
                valuable_base = self.player_data.find("valuable")
                if valuable_base is None:
                    return
                print(f"Sync Valuables: No Valuable Base")
                # 4. Iterate over the valuable names and their sequential integer IDs
                for xml_path, location_id in Valuable_Locations.items():
                    # Skip if this location check was already completed/sent
                    if location_id in self.locations_checked:
                        continue

                    # Look for the valuable item element inside the valuable block
                    node = valuable_base.find(xml_path)
                    if node is not None:
                        try:
                            current_val = int(node.get("value", "0"))

                            # If the valuable item has been collected (value is 1 or greater)
                            if current_val >= 1:
                                print(f"Sync Valuables: {xml_path} collected. Sending ID {location_id}")
                                self.send_upgrade_check(location_id)

                        except (ValueError, TypeError) as e:
                            print(f"Sync Valuables: Error processing value at {xml_path}: {e}")

    def watch_cash(self):
        print("Sync Cash: Entering watch_cash")

        if self.player_data is None:
            return

        self.last_cash = self.current_cash

        asyncio.create_task(self.send_msgs([{
            "cmd": "Set",
            "key": f"Teardown_Cash{self.team}_{self.slot}",
            "default": 0,
            "want_reply": True,
            "operations": [{"operation": "replace", "value": self.current_cash}]
        }]))
        print(f"Sync Cash: Updated cash on server to {self.current_cash}.")



    def send_upgrade_check(self, location_id):
        print(f"Send Upgrade: Entering send_upgrade_check location {location_id}")

        if location_id not in self.locations_checked:
            print(f"Sync Missions: Queuing Location ID {location_id}")

            asyncio.create_task(self.check_locations({location_id}))

            self.locations_checked.append(location_id)
            print(f"Success: Task created for {location_id}")


    def mission_counter(self, mission_id: str):
        # 1. Get the index (e.g., lee_login is 2)
        index = Missionindex.get(mission_id)

        if index is not None:
            # 1 << 2 becomes 00000100 in binary
            bit_to_set = 1 << index
            current_mask = getattr(self, 'mission_bitmask', 0)
            #if current_mask & bit_to_set:
                #print(f"Archipelago: Bit at index {index} is already 1. No update needed.")
                #return

            asyncio.create_task(self.send_msgs([{
                "cmd": "Set",
                "key": f"Teardown_Missions_Counter{self.team}_{self.slot}",
                "default": 0,
                "want_reply": True,
                "operations": [{"operation": "or", "value": bit_to_set}]
            }]))
            self.mission_bitmask = current_mask | bit_to_set
            print(f"Archipelago: Flipped bit {index} to 1.")

    def handle_victory_unlock(self, bitmask):
        if self.player_data is None:
            return None

        final_mission = self.player_data.find("mission/cullington_bomb/score")
        if final_mission is not None:
            final_score = final_mission.get("value")
            print(f"Final Score {final_score}")

            if final_score is not None and final_score == "1":
                asyncio.create_task(self.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": 30,
                }]))
                print("Goal Sent!!")

        current_count = bitmask.bit_count()
        goal_required = getattr(self, 'MissionAmount', 20)
        print(f"Archipelago: Current Missions Count {current_count} Goal Required Count {goal_required}")
        if current_count >= goal_required:
            if self.EasyGoal:
                asyncio.create_task(self.send_msgs([{
                    "cmd": "StatusUpdate",
                    "status": 30,
                }]))
                print("Goal Sent Easy")
                return None
        return None

    async def launch_game(self):
        if self.game_exe_path and os.path.exists(self.game_exe_path):
            subprocess.Popen([self.game_exe_path])
        else:
            print("Cannot launch: Valid executable path not found.")


    async def teardown_loop(self):
        while True:
            await asyncio.to_thread(self.checkgamepath)
            print("Loop: Game path found")
            await self.reset_save()
            print("Loop: Save Reset")

            await self.message_event1.wait()
            print("Loop: Message 1 set")
            await self.message_event2.wait()
            print("Loop: Message 2 set")

            await self.applying_save()
            print("Loop: Save Applied")

            await self.launch_game()
            print("Loop: Game Launched")
            self.innit_event.set()

            while self.innit_event.is_set():
                print("Loop: Tick")
                await self.sync_savegame()
                await asyncio.sleep(3)
            print("Loop: Innit_event Cleared")



    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            print("Connected")

            self.game = self.slot_info[self.slot].game
            self.last_connected_slot = self.slot

            self.slot_data = args["slot_data"]
            self.MissionAmount = self.slot_data.get("MissionAmount", 20)
            print(self.MissionAmount)
            self.ToolUpgrades = self.slot_data.get("ToolUpgrades", True)
            print(self.ToolUpgrades)
            self.ValuableSanity = self.slot_data.get("ValuableSanity", False)
            print(self.ValuableSanity)
            self.FastGoal = self.slot_data.get("FastGoal", False)
            print(self.FastGoal)
            self.EasyGoal = self.slot_data.get("EasyGoal", False)
            print(self.EasyGoal)
            self.message_event1.set()
            print("Message Event 1 set")


            async def init_sequence():
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown_Missions{self.team}_{self.slot}"]}])
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown_Cash{self.team}_{self.slot}"]}])
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown_Missions_Counter{self.team}_{self.slot}"]}])
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown_Applied_Cash{self.team}_{self.slot}"]}])

                self.message_event2.set()
                print("Message Event 2 set")

            asyncio.create_task(init_sequence())


        elif cmd == "Retrieved":
            retrieved_keys = args.get("keys", [])
            #print(f"Retrieved: retrieved_keys = {retrieved_keys}")

            if f"Teardown_Missions{self.team}_{self.slot}" in retrieved_keys:
                self.mission_count = retrieved_keys.get(f"Teardown_Missions{self.team}_{self.slot}", 0)
                print(f"Retrieved: self.mission_count = {self.mission_count}")

            if f"Teardown_Missions_Counter{self.team}_{self.slot}" in retrieved_keys:
                self.mission_bitmask = retrieved_keys.get(f"Teardown_Missions_Counter_{self.team}_{self.slot}", 0)
                print(f"Retrieved: self.mission_bitmask = {self.mission_bitmask}")

            if f"Teardown_Applied_Cash{self.team}_{self.slot}" in retrieved_keys:
                self.applied_cash_total = retrieved_keys.get(f"Teardown_Applied_Cash{self.team}_{self.slot}", 0)
                print(f"Retrieved: self.applied_cash_total = {self.applied_cash_total}")

            if f"Teardown_Cash{self.team}_{self.slot}" in retrieved_keys:
                self.cash = retrieved_keys.get(f"Teardown_Cash{self.team}_{self.slot}", 0)
                print(f"Retrieved: self.cash = {self.cash}")


        elif cmd == "SetReply":
            if args.get("key") == f"Teardown_Missions_Counter{self.team}_{self.slot}":
                self.mission_bitmask = args.get("value")
                self.handle_victory_unlock(args.get("value"))

            #elif args.get("key") == f"Teardown_Applied_Cash{self.team}_{self.slot}":
                #self.applied_cash_total = args.get("value")


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TeardownContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="Teardown")

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = ""
        await super().disconnect(allow_autoreconnect)
        self.message_event1.clear()
        self.message_event2.clear()
        self.innit_event.clear()


async def main(args):
    ctx = TeardownContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()


    ctx.sync_task = asyncio.create_task(ctx.teardown_loop(), name="Teardown Loop")

    await ctx.exit_event.wait()
    await ctx.shutdown()

import colorama

def launch():
    parser = get_base_parser(description="Teardown Archipelago Client")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")

    args = parser.parse_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()


if __name__ == "__main__":
    launch()