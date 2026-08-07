from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TeardownWorld

ITEM_NAME_TO_ID = {

    "Old Building Problem Unlock": 1,

}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Old Building Problem Unlock": ItemClassification.progression,
    "Spraycan Unlock": ItemClassification.useful,
    "Blowtorch Fuel Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Cash Bundle 20": ItemClassification.filler,
}

item_name_groups = {
    "levels": [
        "Old Building Problem Unlock",
        "Lee Computers Unlock",
        "Login Devices Unlock",
        "Making Space Unlock",
        "Classic Cars Unlock",
        "The GPS Devices Unlock",
        "The Car Wash Unlock",
        "Heavy Lifting Unlock",
        "The Tower Unlock",
        "Fine Arts Unlock",
        "Tool Up Unlock",
        "Art Return Unlock",
        "Covert Chaos Unlock",
        "Insurance Fraud Unlock",
        "The BlueTide Computers Unlock",
        "The Speed Deal Unlock",
        "A Wet Affair Unlock",
        "Power Outage Unlock",
        "Motivational Reminder Unlock",
        "An Assortment Of Dishes Unlock",
        "Flooding Unlock",
        "The Chase Unlock",
        "Roborazzi Unlock",
        "The Secret Ingredients Unlock",
        "The BlueTide Shortage Unlock",
        "The Shipping Logs Unlock",
        "The Alarm System Unlock",
        "Moving The Goods Unlock",
        "Havoc In Paradise Unlock",
        "Elena's Revenge Unlock",
        "Truckload Of Trouble Unlock",
        "Ornament Ordeal Unlock",
        "The Quilez Tools Unlock",
        "Connecting The Dots Unlock",
        "The Pawn Shop Unlock",
        "The Droid Abduction Unlock",
        "Malice In Woonderland Unlock",
        "Handle With Care Unlock",
        "Droid Dismount Unlock",
    ],

    "nonlevels": [
        "Old Building Problem Unlock",
        "Lee Computers Unlock",
        "Login Devices Unlock",
        "Making Space Unlock",
        "Classic Cars Unlock",
        "The GPS Devices Unlock",
        "The Car Wash Unlock",
        "The Tower Unlock",
        "Fine Arts Unlock",
        "Covert Chaos Unlock",
        "The Chase Unlock",
        "Roborazzi Unlock",
        "The Alarm System Unlock",
        "Moving The Goods Unlock",
        "Havoc In Paradise Unlock",
        "Elena's Revenge Unlock",
    ],

    "tools": [
        "Sledge Hammer Unlock",
        "Spraycan Unlock",
        "Extinguisher Unlock",
        "Blowtorch Unlock",
        "Shotgun Unlock",
        "Plank Unlock",
        "Pipe Bomb Unlock",
        "Gun Unlock",
        "Bomb Unlock",
        "Rocket Launcher Unlock",
        "Rocket Booster Unlock",
        "Leaf Blower Unlock",
        "Cable Unlock",
        "Vehicle Thruster Unlock",
        "Nitroglycerin Unlock",
        "Hunting Rifle Unlock",
        "BlueTide Unlock",

    ],

    "Lee Chemicals": [
        "Lee Computers Unlock",
        "Login Devices Unlock",
        "Heavy Lifting Unlock",
        "The Tower Unlock",
        "Power Outage Unlock",
        "Flooding Unlock",
        "Malice In Woonderland Unlock",
    ],

    "West Point Marina": [
        "Making Space Unlock",
        "Classic Cars Unlock",
        "The GPS Devices Unlock",
        "Tool Up Unlock",
        "Art Return Unlock",
    ],

    "Villa Gordon": [
        "Classic Cars Unlock",
        "Fine Arts Unlock",
        "Insurance Fraud Unlock",
        "The Speed Deal Unlock",
        "A Wet Affair Unlock",
    ],

    "Hollowrock Island": [
        "The BlueTide Computers Unlock",
        "Motivational Reminder Unlock",
        "An Assortment Of Dishes Unlock",
        "The Secret Ingredients Unlock",
        "Droid Dismount Unlock",
    ],

    "Evertides Mall": [
        "Covert Chaos Unlock",
        "The Shipping Logs Unlock",
        "Ornament Ordeal Unlock",
        "Connecting The Dots Unlock",
    ],

    "Frustrum": [
        "The BlueTide Shortage Unlock",
        "Truckload Of Trouble Unlock",
        "The Pawn Shop Unlock",
    ],

    "Quilez Security": [
        "The Quilez Tools Unlock",
        "The Droid Abduction Unlock",
        "Handle With Care Unlock",
    ],

    "Isla Estocastica": [
        "The Alarm System Unlock",
        "Moving The Goods Unlock",
        "Havoc In Paradise Unlock",
        "Elena's Revenge Unlock",
    ],

    "Door": [
        "Blowtorch Unlock",
        "Shotgun Unlock",
        "Gun Unlock",
        "Pipe Bomb Unlock",
        "Hunting Rifle Unlock",
    ],

    "Wall/Opening": [
        "Shotgun Unlock",
        "Pipe Bomb Unlock",
        "Bomb Unlock",
        "Rocket Launcher Unlock",
    ],

    "Destruction": [
        "Shotgun Unlock",
        "Pipe Bomb Unlock",
        "Bomb Unlock",
        "Rocket Launcher Unlock",
        "Nitroglycerin Unlock",
    ],

    "Guns": [
        "Gun Unlock",
        "Rocket Launcher Unlock",
        "Hunting Rifle Unlock",

    ],

    "Plank/Cable": [
        "Plank Unlock",
        "Cable Unlock",
    ],

}


class TeardownItem(Item):
    game = "Teardown"


def get_random_filler_item_name(world: TeardownWorld) -> str:
    return "Cash Bundle 20"

def create_item_with_correct_classification(world: TeardownWorld, name: str) -> TeardownItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    if name == "Elena's Revenge Unlock":
        classification = ItemClassification.progression

    return TeardownItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: TeardownWorld) -> None:
    itempool: list[Item] = [

        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),
        world.create_item("Cash Bundle 50"),

        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),
        world.create_item("Cash Bundle 100"),

        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),
        world.create_item("Cash Bundle 250"),

        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),
        world.create_item("Cash Bundle 500"),

        world.create_item("Cash Bundle 750"),
        world.create_item("Cash Bundle 750"),
        world.create_item("Cash Bundle 750"),
        world.create_item("Cash Bundle 750"),
        world.create_item("Cash Bundle 750"),

        world.create_item("Cash Bundle 1000"),
        world.create_item("Cash Bundle 1000"),
        world.create_item("Cash Bundle 1000"),

        world.create_item("Cash Bundle 3000"),
    ]


    if world.options.StartingTool:
        amount = world.options.AmountTools.value
        startingtools = list(item_name_groups["tools"])

        for number in range(amount):
            chosentool = world.random.choice(startingtools)

            startingtools.remove(chosentool)

            world.push_precollected(world.create_item(chosentool))

        for leftover in startingtools:
            itempool.append(world.create_item(leftover))


    else:
        world.push_precollected(world.create_item("Sledge Hammer Unlock"))
        world.push_precollected(world.create_item("Spraycan Unlock"))
        world.push_precollected(world.create_item("Extinguisher Unlock"))

        itempool.append(world.create_item("Blowtorch Unlock"))
        itempool.append(world.create_item("Shotgun Unlock"))
        itempool.append(world.create_item("Plank Unlock"))
        itempool.append(world.create_item("Pipe Bomb Unlock"))
        itempool.append(world.create_item("Gun Unlock"))
        itempool.append(world.create_item("Bomb Unlock"))
        itempool.append(world.create_item("Rocket Launcher Unlock"))
        itempool.append(world.create_item("Rocket Booster Unlock"))
        itempool.append(world.create_item("Leaf Blower Unlock"))
        itempool.append(world.create_item("Cable Unlock"))
        itempool.append(world.create_item("Vehicle Thruster Unlock"))
        itempool.append(world.create_item("Nitroglycerin Unlock"))
        itempool.append(world.create_item("Hunting Rifle Unlock"))
        itempool.append(world.create_item("BlueTide Unlock"))


    amountlevels = world.options.AmountLevels.value
    startinglevels = list(item_name_groups["nonlevels"])
    totallevels = list(item_name_groups["levels"])
    totallevels = [level for level in totallevels if level not in startinglevels]

    if not world.options.StartingLevel:
        world.push_precollected(world.create_item("Old Building Problem Unlock"))
        startinglevels.remove("Old Building Problem Unlock")
        amountlevels = amountlevels - 1

    for number in range(amountlevels):
        if startinglevels:
            chosenlevel = world.random.choice(startinglevels)
            startinglevels.remove(chosenlevel)
        else:
            chosenlevel = world.random.choice(totallevels)
            totallevels.remove(chosenlevel)

        world.push_precollected(world.create_item(chosenlevel))

    for leftover in startinglevels:
        itempool.append(world.create_item(leftover))

    for leftover in totallevels:
        itempool.append(world.create_item(leftover))



    if world.options.ToolUpgrades:
        itempool.append(world.create_item("Blowtorch Fuel Upgrade"))
        itempool.append(world.create_item("Blowtorch Fuel Upgrade"))
        itempool.append(world.create_item("Blowtorch Fuel Upgrade"))
        itempool.append(world.create_item("Blowtorch Fuel Upgrade"))

        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))
        itempool.append(world.create_item("Shotgun Rounds Upgrade"))

        itempool.append(world.create_item("Shotgun Range Upgrade"))
        itempool.append(world.create_item("Shotgun Range Upgrade"))

        itempool.append(world.create_item("Shotgun Damage Upgrade"))
        itempool.append(world.create_item("Shotgun Damage Upgrade"))

        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))
        itempool.append(world.create_item("Plank Amount Upgrade"))

        itempool.append(world.create_item("Plank Width Upgrade"))
        itempool.append(world.create_item("Plank Width Upgrade"))

        itempool.append(world.create_item("Plank Max Length Upgrade"))
        itempool.append(world.create_item("Plank Max Length Upgrade"))
        itempool.append(world.create_item("Plank Max Length Upgrade"))

        itempool.append(world.create_item("Pipe Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Pipe Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Pipe Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Pipe Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Pipe Bomb Rounds Upgrade"))

        itempool.append(world.create_item("Pipe Bomb Blast Upgrade"))
        itempool.append(world.create_item("Pipe Bomb Blast Upgrade"))

        itempool.append(world.create_item("Gun Rounds Upgrade"))
        itempool.append(world.create_item("Gun Rounds Upgrade"))
        itempool.append(world.create_item("Gun Rounds Upgrade"))
        itempool.append(world.create_item("Gun Rounds Upgrade"))
        itempool.append(world.create_item("Gun Rounds Upgrade"))

        itempool.append(world.create_item("Gun Range Upgrade"))
        itempool.append(world.create_item("Gun Range Upgrade"))
        itempool.append(world.create_item("Gun Range Upgrade"))

        itempool.append(world.create_item("Gun Damage Upgrade"))
        itempool.append(world.create_item("Gun Damage Upgrade"))

        itempool.append(world.create_item("Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Bomb Rounds Upgrade"))
        itempool.append(world.create_item("Bomb Rounds Upgrade"))

        itempool.append(world.create_item("Bomb Blast Upgrade"))
        itempool.append(world.create_item("Bomb Blast Upgrade"))

        itempool.append(world.create_item("Rocket Launcher Rounds Upgrade"))
        itempool.append(world.create_item("Rocket Launcher Rounds Upgrade"))
        itempool.append(world.create_item("Rocket Launcher Rounds Upgrade"))

        itempool.append(world.create_item("Rocket Launcher Blast Upgrade"))
        itempool.append(world.create_item("Rocket Launcher Blast Upgrade"))

        itempool.append(world.create_item("Rocket Booster Rounds Upgrade"))
        itempool.append(world.create_item("Rocket Booster Rounds Upgrade"))
        itempool.append(world.create_item("Rocket Booster Rounds Upgrade"))

        itempool.append(world.create_item("Rocket Booster Power Upgrade"))
        itempool.append(world.create_item("Rocket Booster Power Upgrade"))

        itempool.append(world.create_item("Rocket Booster Time Upgrade"))
        itempool.append(world.create_item("Rocket Booster Time Upgrade"))

        itempool.append(world.create_item("Leaf Blower Power Upgrade"))
        itempool.append(world.create_item("Leaf Blower Power Upgrade"))
        itempool.append(world.create_item("Leaf Blower Power Upgrade"))

        itempool.append(world.create_item("Cable Amount Upgrade"))
        itempool.append(world.create_item("Cable Amount Upgrade"))
        itempool.append(world.create_item("Cable Amount Upgrade"))

        itempool.append(world.create_item("Cable Stretch Upgrade"))
        itempool.append(world.create_item("Cable Stretch Upgrade"))

        itempool.append(world.create_item("Vehicle Thruster Rounds Upgrade"))
        itempool.append(world.create_item("Vehicle Thruster Rounds Upgrade"))
        itempool.append(world.create_item("Vehicle Thruster Rounds Upgrade"))

        itempool.append(world.create_item("Vehicle Thruster Power Upgrade"))
        itempool.append(world.create_item("Vehicle Thruster Power Upgrade"))

        itempool.append(world.create_item("Nitroglycerin Rounds Upgrade"))
        itempool.append(world.create_item("Nitroglycerin Rounds Upgrade"))
        itempool.append(world.create_item("Nitroglycerin Rounds Upgrade"))

        itempool.append(world.create_item("Nitroglycerin Blast Upgrade"))
        itempool.append(world.create_item("Nitroglycerin Blast Upgrade"))
        itempool.append(world.create_item("Nitroglycerin Blast Upgrade"))

        itempool.append(world.create_item("Hunting Rifle Rounds Upgrade"))
        itempool.append(world.create_item("Hunting Rifle Rounds Upgrade"))

        itempool.append(world.create_item("BlueTide Bottles Upgrade"))
        itempool.append(world.create_item("BlueTide Bottles Upgrade"))

        itempool.append(world.create_item("BlueTide Duration Upgrade"))
        itempool.append(world.create_item("BlueTide Duration Upgrade"))

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool