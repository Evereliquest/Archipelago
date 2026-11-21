from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import TeardownWorld


def create_and_connect_regions(world: TeardownWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

# Creates all regions
def create_all_regions(world: TeardownWorld) -> None:
    menu = Region("Main Menu", world.player, world.multiworld)


# Lists all regions
    regions = [menu]


# Creates region if option is enabled
    if "Base Campaign" in world.options.CampaignSelection:
        regions.append(Region("Old Building Problem", world.player, world.multiworld))
        regions.append(Region("Lee Computers", world.player, world.multiworld))
        regions.append(Region("Login Devices", world.player, world.multiworld))
        regions.append(Region("Making Space", world.player, world.multiworld))
        regions.append(Region("Classic Cars", world.player, world.multiworld))
        regions.append(Region("The GPS Devices", world.player, world.multiworld))
        regions.append(Region("The Car Wash", world.player, world.multiworld))
        regions.append(Region("Heavy Lifting", world.player, world.multiworld))
        regions.append(Region("The Tower", world.player, world.multiworld))
        regions.append(Region("Fine Arts", world.player, world.multiworld))
        regions.append(Region("Tool Up", world.player, world.multiworld))
        regions.append(Region("Art Return", world.player, world.multiworld))
        regions.append(Region("Covert Chaos", world.player, world.multiworld))
        regions.append(Region("Insurance Fraud", world.player, world.multiworld))
        regions.append(Region("The BlueTide Computers", world.player, world.multiworld))
        regions.append(Region("The Speed Deal", world.player, world.multiworld))
        regions.append(Region("A Wet Affair", world.player, world.multiworld))
        regions.append(Region("Power Outage", world.player, world.multiworld))
        regions.append(Region("Motivational Reminder", world.player, world.multiworld))
        regions.append(Region("An Assortment Of Dishes", world.player, world.multiworld))
        regions.append(Region("Flooding", world.player, world.multiworld))
        regions.append(Region("The Chase", world.player, world.multiworld))
        regions.append(Region("Roborazzi", world.player, world.multiworld))
        regions.append(Region("The Secret Ingredients", world.player, world.multiworld))
        regions.append(Region("The BlueTide Shortage", world.player, world.multiworld))
        regions.append(Region("The Shipping Logs", world.player, world.multiworld))
        regions.append(Region("The Alarm System", world.player, world.multiworld))
        regions.append(Region("Moving The Goods", world.player, world.multiworld))
        regions.append(Region("Havoc In Paradise", world.player, world.multiworld))
        regions.append(Region("Elena's Revenge", world.player, world.multiworld))
        regions.append(Region("Truckload Of Trouble", world.player, world.multiworld))
        regions.append(Region("Ornament Ordeal", world.player, world.multiworld))
        regions.append(Region("The Quilez Tools", world.player, world.multiworld))
        regions.append(Region("Connecting The Dots", world.player, world.multiworld))
        regions.append(Region("The Pawn Shop", world.player, world.multiworld))
        regions.append(Region("The Droid Abduction", world.player, world.multiworld))
        regions.append(Region("Malice In Woonderland", world.player, world.multiworld))
        regions.append(Region("Handle With Care", world.player, world.multiworld))
        regions.append(Region("Droid Dismount", world.player, world.multiworld))
        regions.append(Region("The Final Diversion", world.player, world.multiworld))

        if world.options.ToolUpgrades:
            regions.append(Region("Blowtorch Upgrades", world.player, world.multiworld))
            regions.append(Region("Shotgun Upgrades", world.player, world.multiworld))
            regions.append(Region("Plank Upgrades", world.player, world.multiworld))
            regions.append(Region("Pipe Bomb Upgrades", world.player, world.multiworld))
            regions.append(Region("Gun Upgrades", world.player, world.multiworld))
            regions.append(Region("Bomb Upgrades", world.player, world.multiworld))
            regions.append(Region("Rocket Launcher Upgrades", world.player, world.multiworld))
            regions.append(Region("Rocket Booster Upgrades", world.player, world.multiworld))
            regions.append(Region("Leaf Blower Upgrades", world.player, world.multiworld))
            regions.append(Region("Cable Upgrades", world.player, world.multiworld))
            regions.append(Region("Vehicle Thruster Upgrades", world.player, world.multiworld))
            regions.append(Region("Nitroglycerin Upgrades", world.player, world.multiworld))
            regions.append(Region("Hunting Rifle Upgrades", world.player, world.multiworld))
            regions.append(Region("BlueTide Upgrades", world.player, world.multiworld))

        if world.options.ValuableSanity:
            regions.append(Region("Lee Valuables", world.player, world.multiworld))
            regions.append(Region("Lee Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Lee Valuables Computers", world.player, world.multiworld))
            regions.append(Region("Lee Valuables Woonderland", world.player, world.multiworld))

            regions.append(Region("Marina Valuables", world.player, world.multiworld))
            regions.append(Region("Marina Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Marina Valuables Making Space", world.player, world.multiworld))
            regions.append(Region("Marina Valuables After Art", world.player, world.multiworld))

            regions.append(Region("Gordon Valuables", world.player, world.multiworld))
            regions.append(Region("Gordon Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Gordon Valuables Fraud", world.player, world.multiworld))

            regions.append(Region("Hollowrock Valuables", world.player, world.multiworld))
            regions.append(Region("Hollowrock Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Hollowrock Valuables Even Harder", world.player, world.multiworld))
            regions.append(Region("Hollowrock Valuables Dishes", world.player, world.multiworld))

            regions.append(Region("Evertides Valuables", world.player, world.multiworld))
            regions.append(Region("Evertides Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Evertides Valuables Covert Chaos", world.player, world.multiworld))

            regions.append(Region("Frustrum Valuables", world.player, world.multiworld))
            regions.append(Region("Frustrum Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Frustrum Valuables Chase", world.player, world.multiworld))

            regions.append(Region("Quilez Valuables", world.player, world.multiworld))
            regions.append(Region("Quilez Valuables Harder", world.player, world.multiworld))
            regions.append(Region("Quilez Valuables Handle with Care", world.player, world.multiworld))

            regions.append(Region("Isla Valuables", world.player, world.multiworld))
            regions.append(Region("Isla Valuables Harder", world.player, world.multiworld))

    if "Time Campers" in world.options.CampaignSelection:
        regions.append(Region("Stocking Up", world.player, world.multiworld))
        regions.append(Region("Going Volatile", world.player, world.multiworld))
        regions.append(Region("Hiding Traces", world.player, world.multiworld))
        regions.append(Region("Preemptive Prohibition", world.player, world.multiworld))
        regions.append(Region("Tumbling Around", world.player, world.multiworld))
        regions.append(Region("Greasing the Gears", world.player, world.multiworld))
        regions.append(Region("Motivational Reminder", world.player, world.multiworld))
        regions.append(Region("Four Stolen Hooves", world.player, world.multiworld))
        regions.append(Region("Cho-Choosing Path", world.player, world.multiworld))


    # Adds all regions to list
    world.multiworld.regions += regions

def connect_regions(world: TeardownWorld) -> None:

    menu = world.get_region("Main Menu")


    if "Base Campaign" in world.options.CampaignSelection:
        menu.connect(world.get_region("Old Building Problem"), "Main Menu to Old Building Problem")
        menu.connect(world.get_region("Lee Computers"), "Main Menu to Lee Computers")
        menu.connect(world.get_region("Login Devices"), "Main Menu to Login Devices")
        menu.connect(world.get_region("Making Space"), "Main Menu to Making Space")
        menu.connect(world.get_region("Classic Cars"), "Main Menu to Classic Cars")
        menu.connect(world.get_region("The GPS Devices"), "Main Menu to The GPS Devices")
        menu.connect(world.get_region("The Car Wash"), "Main Menu to The Car Wash")
        menu.connect(world.get_region("Heavy Lifting"), "Main Menu to Heavy Lifting")
        menu.connect(world.get_region("The Tower"), "Main Menu to The Tower")
        menu.connect(world.get_region("Fine Arts"), "Main Menu to Fine Arts")
        menu.connect(world.get_region("Tool Up"), "Main Menu to Tool Up")
        menu.connect(world.get_region("Art Return"), "Main Menu to Art Return")
        menu.connect(world.get_region("Covert Chaos"), "Main Menu to Covert Chaos")
        menu.connect(world.get_region("Insurance Fraud"), "Main Menu to Insurance Fraud")
        menu.connect(world.get_region("The BlueTide Computers"), "Main Menu to The BlueTide Computers")
        menu.connect(world.get_region("The Speed Deal"), "Main Menu to The Speed Deal")
        menu.connect(world.get_region("A Wet Affair"), "Main Menu to A Wet Affair")
        menu.connect(world.get_region("Power Outage"), "Main Menu to Power Outage")
        menu.connect(world.get_region("Motivational Reminder"), "Main Menu to Motivational Reminder")
        menu.connect(world.get_region("An Assortment Of Dishes"), "Main Menu to An Assortment Of Dishes")
        menu.connect(world.get_region("Flooding"), "Main Menu to Flooding")
        menu.connect(world.get_region("The Chase"), "Main Menu to The Chase")
        menu.connect(world.get_region("Roborazzi"), "Main Menu to Roborazzi")
        menu.connect(world.get_region("The Secret Ingredients"), "Main Menu to The Secret Ingredients")
        menu.connect(world.get_region("The BlueTide Shortage"), "Main Menu to The BlueTide Shortage")
        menu.connect(world.get_region("The Shipping Logs"), "Main Menu to The Shipping Logs")
        menu.connect(world.get_region("The Alarm System"), "Main Menu to The Alarm System")
        menu.connect(world.get_region("Moving The Goods"), "Main Menu to Moving The Goods")
        menu.connect(world.get_region("Havoc In Paradise"), "Main Menu to Havoc In Paradise")
        menu.connect(world.get_region("Elena's Revenge"), "Main Menu to Elena's Revenge")
        menu.connect(world.get_region("Truckload Of Trouble"), "Main Menu to Truckload Of Trouble")
        menu.connect(world.get_region("Ornament Ordeal"), "Main Menu to Ornament Ordeal")
        menu.connect(world.get_region("The Quilez Tools"), "Main Menu to The Quilez Tools")
        menu.connect(world.get_region("Connecting The Dots"), "Main Menu to Connecting The Dots")
        menu.connect(world.get_region("The Pawn Shop"), "Main Menu to The Pawn Shop")
        menu.connect(world.get_region("The Droid Abduction"), "Main Menu to The Droid Abduction")
        menu.connect(world.get_region("Malice In Woonderland"), "Main Menu to Malice In Woonderland")
        menu.connect(world.get_region("Handle With Care"), "Main Menu to Handle With Care")
        menu.connect(world.get_region("Droid Dismount"), "Main Menu to Droid Dismount")
        menu.connect(world.get_region("The Final Diversion"), "Main Menu to The Final Diversion")

        if world.options.ToolUpgrades:
            menu.connect(world.get_region("Blowtorch Upgrades"), "Main Menu to Blowtorch Upgrades")
            menu.connect(world.get_region("Shotgun Upgrades"), "Main Menu to Shotgun Upgrades")
            menu.connect(world.get_region("Plank Upgrades"), "Main Menu to Plank Upgrades")
            menu.connect(world.get_region("Pipe Bomb Upgrades"), "Main Menu to Pipe Bomb Upgrades")
            menu.connect(world.get_region("Gun Upgrades"), "Main Menu to Gun Upgrades")
            menu.connect(world.get_region("Bomb Upgrades"), "Main Menu to Bomb Upgrades")
            menu.connect(world.get_region("Rocket Launcher Upgrades"), "Main Menu to Rocket Launcher Upgrades")
            menu.connect(world.get_region("Rocket Booster Upgrades"), "Main Menu to Rocket Booster Upgrades")
            menu.connect(world.get_region("Leaf Blower Upgrades"), "Main Menu to Leaf Blower Upgrades")
            menu.connect(world.get_region("Cable Upgrades"), "Main Menu to Cable Upgrades")
            menu.connect(world.get_region("Vehicle Thruster Upgrades"), "Main Menu to Vehicle Thruster Upgrades")
            menu.connect(world.get_region("Nitroglycerin Upgrades"), "Main Menu to Nitroglycerin Upgrades")
            menu.connect(world.get_region("Hunting Rifle Upgrades"), "Main Menu to Hunting Rifle Upgrades")
            menu.connect(world.get_region("BlueTide Upgrades"), "Main Menu to BlueTide Upgrades")

        if world.options.ValuableSanity:
            leevaluable = world.get_region("Lee Valuables")
            leevaluablewoonderland = world.get_region("Lee Valuables Woonderland")
            marinavaluable = world.get_region("Marina Valuables")
            gordonvaluable = world.get_region("Gordon Valuables")
            hollowrockvaluable = world.get_region("Hollowrock Valuables")
            evertidesvaluable = world.get_region("Evertides Valuables")
            frustrumvaluable = world.get_region("Frustrum Valuables")
            quilezvaluable = world.get_region("Quilez Valuables")
            islavaluable = world.get_region("Isla Valuables")


            menu.connect(leevaluable, "Main Menu to Lee Valuables")
            menu.connect(leevaluablewoonderland, "Main Menu to Lee Valuables Woonderland")
            menu.connect(marinavaluable, "Main Menu to Marina Valuables")
            menu.connect(gordonvaluable, "Main Menu to Gordon Valuables")
            menu.connect(hollowrockvaluable, "Main Menu to Hollowrock Valuables")
            menu.connect(evertidesvaluable, "Main Menu to Evertides Valuables")
            menu.connect(frustrumvaluable, "Main Menu to Frustrum Valuables")
            menu.connect(quilezvaluable, "Main Menu to Quilez Valuables")
            menu.connect(islavaluable, "Main Menu to Isla Valuables")


            leevaluable.connect(world.get_region("Lee Valuables Harder"), "Lee Valuables to Lee Valuables Harder")
            leevaluable.connect(world.get_region("Lee Valuables Computers"), "Lee Valuables to Lee Valuables Computers")

            marinavaluable.connect(world.get_region("Marina Valuables Harder"), "Marina Valuables to Marina Valuables Harder")
            marinavaluable.connect(world.get_region("Marina Valuables Making Space"), "Marina Valuables to Marina Valuables Making Space")
            marinavaluable.connect(world.get_region("Marina Valuables After Art"), "Marina Valuables to Marina Valuables After Art")

            gordonvaluable.connect(world.get_region("Gordon Valuables Harder"), "Gordon Valuables to Gordon Valuables Harder")
            gordonvaluable.connect(world.get_region("Gordon Valuables Fraud"), "Gordon Valuables to Gordon Valuables Fraud")

            hollowrockvaluable.connect(world.get_region("Hollowrock Valuables Harder"), "Hollowrock Valuables to Hollowrock Valuables Harder")
            hollowrockvaluable.connect(world.get_region("Hollowrock Valuables Even Harder"), "Hollowrock Valuables to Hollowrock Valuables Even Harder")
            hollowrockvaluable.connect(world.get_region("Hollowrock Valuables Dishes"), "Hollowrock Valuables to Hollowrock Valuables Dishes")

            evertidesvaluable.connect(world.get_region("Evertides Valuables Harder"), "Evertides Valuables to Evertides Valuables Harder")
            evertidesvaluable.connect(world.get_region("Evertides Valuables Covert Chaos"), "Evertides Valuables to Evertides Valuables Covert Chaos")

            frustrumvaluable.connect(world.get_region("Frustrum Valuables Harder"), "Frustrum Valuables to Frustrum Valuables Harder")
            frustrumvaluable.connect(world.get_region("Frustrum Valuables Chase"), "Frustrum Valuables to Frustrum Valuables Chase")

            quilezvaluable.connect(world.get_region("Quilez Valuables Harder"), "Quilez Valuables to Quilez Valuables Harder")
            quilezvaluable.connect(world.get_region("Quilez Valuables Handle with Care"), "Quilez Valuables to Quilez Valuables Handle with Care")

            islavaluable.connect(world.get_region("Isla Valuables Harder"), "Isla Valuables to Isla Valuables Harder")

