from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TeardownWorld

ITEM_NAME_TO_ID = {

    "Old Building Problem Unlock": 1,
    "Lee Computers Unlock": 2,
    "Login Devices Unlock": 3,
    "Making Space Unlock": 4,
    "Classic Cars Unlock": 5,
    "The GPS Devices Unlock": 6,
    "The Car Wash Unlock": 7,
    "Heavy Lifting Unlock": 8,
    "The Tower Unlock": 9,
    "Fine Arts Unlock": 10,
    "Tool Up Unlock": 11,
    "Art Return Unlock": 12,
    "Covert Chaos Unlock": 13,
    "Insurance Fraud Unlock": 14,
    "The BlueTide Computers Unlock": 15,
    "The Speed Deal Unlock": 16,
    "A Wet Affair Unlock": 17,
    "Power Outage Unlock": 18,
    "Motivational Reminder Unlock": 19,
    "An Assortment Of Dishes Unlock": 20,
    "Flooding Unlock": 21,
    "The Chase Unlock": 22,
    "Roborazzi Unlock": 23,
    "The Secret Ingredients Unlock": 24,
    "The BlueTide Shortage Unlock": 25,
    "The Shipping Logs Unlock": 26,
    "The Alarm System Unlock": 27,
    "Moving The Goods Unlock": 28,
    "Havoc In Paradise Unlock": 29,
    "Elena's Revenge Unlock": 30,
    "Truckload Of Trouble Unlock": 31,
    "Ornament Ordeal Unlock": 32,
    "The Quilez Tools Unlock": 33,
    "Connecting The Dots Unlock": 34,
    "The Pawn Shop Unlock": 35,
    "The Droid Abduction Unlock": 36,
    "Malice In Woonderland Unlock": 37,
    "Handle With Care Unlock": 38,
    "Droid Dismount Unlock": 39,
    "The Final Diversion Unlock": 40,

#   Progressive Tool Upgrades

    "Sledge Hammer Unlock": 41,
    "Spraycan Unlock": 42,
    "Extinguisher Unlock": 43,

    "Blowtorch Unlock": 51,
    "Shotgun Unlock": 52,
    "Plank Unlock": 53,
    "Pipe Bomb Unlock": 54,
    "Gun Unlock": 55,
    "Bomb Unlock": 56,
    "Rocket Launcher Unlock": 57,
    "Rocket Booster Unlock": 58,
    "Leaf Blower Unlock": 59,
    "Cable Unlock": 60,
    "Vehicle Thruster Unlock": 61,
    "Nitroglycerin Unlock": 62,
    "Hunting Rifle Unlock": 63,
    "BlueTide Unlock": 64,

    "Blowtorch Fuel Upgrade": 71,

    "Shotgun Rounds Upgrade": 81,
    "Shotgun Range Upgrade": 82,
    "Shotgun Damage Upgrade": 83,

    "Plank Amount Upgrade": 91,
    "Plank Width Upgrade": 92,
    "Plank Max Length Upgrade": 93,

    "Pipe Bomb Rounds Upgrade": 101,
    "Pipe Bomb Blast Upgrade": 102,

    "Gun Rounds Upgrade": 111,
    "Gun Range Upgrade": 112,
    "Gun Damage Upgrade": 113,

    "Bomb Rounds Upgrade": 121,
    "Bomb Blast Upgrade": 122,

    "Rocket Launcher Rounds Upgrade": 131,
    "Rocket Launcher Blast Upgrade": 132,

    "Rocket Booster Rounds Upgrade": 141,
    "Rocket Booster Power Upgrade": 142,
    "Rocket Booster Time Upgrade": 143,

    "Leaf Blower Power Upgrade": 151,

    "Cable Amount Upgrade": 161,
    "Cable Stretch Upgrade": 162,

    "Vehicle Thruster Rounds Upgrade": 171,
    "Vehicle Thruster Power Upgrade": 172,

    "Nitroglycerin Rounds Upgrade": 181,
    "Nitroglycerin Blast Upgrade": 182,

    "Hunting Rifle Rounds Upgrade": 191,

    "BlueTide Bottles Upgrade": 201,
    "BlueTide Duration Upgrade": 202,

    "Cash Bundle 20": 251,
    "Cash Bundle 50": 252,
    "Cash Bundle 100": 253,
    "Cash Bundle 250": 254,
    "Cash Bundle 500": 255,
    "Cash Bundle 750": 256,
    "Cash Bundle 1000": 257,
    "Cash Bundle 3000": 258,

    "Extra Nothing": 300,

}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Old Building Problem Unlock": ItemClassification.progression,
    "Lee Computers Unlock": ItemClassification.progression,
    "Login Devices Unlock": ItemClassification.progression,
    "Making Space Unlock": ItemClassification.progression,
    "Classic Cars Unlock": ItemClassification.progression,
    "The GPS Devices Unlock": ItemClassification.progression,
    "The Car Wash Unlock": ItemClassification.progression,
    "Heavy Lifting Unlock": ItemClassification.progression,
    "The Tower Unlock": ItemClassification.progression,
    "Fine Arts Unlock": ItemClassification.progression,
    "Tool Up Unlock": ItemClassification.progression,
    "Art Return Unlock": ItemClassification.progression,
    "Covert Chaos Unlock": ItemClassification.progression,
    "Insurance Fraud Unlock": ItemClassification.progression,
    "The BlueTide Computers Unlock": ItemClassification.progression,
    "The Speed Deal Unlock": ItemClassification.progression,
    "A Wet Affair Unlock": ItemClassification.progression,
    "Power Outage Unlock": ItemClassification.progression,
    "Motivational Reminder Unlock": ItemClassification.progression,
    "An Assortment Of Dishes Unlock": ItemClassification.progression,
    "Flooding Unlock": ItemClassification.progression,
    "The Chase Unlock": ItemClassification.progression,
    "Roborazzi Unlock": ItemClassification.progression,
    "The Secret Ingredients Unlock": ItemClassification.progression,
    "The BlueTide Shortage Unlock": ItemClassification.progression,
    "The Shipping Logs Unlock": ItemClassification.progression,
    "The Alarm System Unlock": ItemClassification.progression,
    "Moving The Goods Unlock": ItemClassification.progression,
    "Havoc In Paradise Unlock": ItemClassification.progression,
    "Elena's Revenge Unlock": ItemClassification.progression,
    "Truckload Of Trouble Unlock": ItemClassification.progression,
    "Ornament Ordeal Unlock": ItemClassification.progression,
    "The Quilez Tools Unlock": ItemClassification.progression,
    "Connecting The Dots Unlock": ItemClassification.progression,
    "The Pawn Shop Unlock": ItemClassification.progression,
    "The Droid Abduction Unlock": ItemClassification.progression,
    "Malice In Woonderland Unlock": ItemClassification.progression,
    "Handle With Care Unlock": ItemClassification.progression,
    "Droid Dismount Unlock": ItemClassification.progression,
    "The Final Diversion Unlock": ItemClassification.progression,

    "Sledge Hammer Unlock": ItemClassification.progression,
    "Spraycan Unlock": ItemClassification.useful,
    "Extinguisher Unlock": ItemClassification.progression,

    "Blowtorch Unlock": ItemClassification.progression,
    "Shotgun Unlock": ItemClassification.progression,
    "Plank Unlock": ItemClassification.progression,
    "Pipe Bomb Unlock": ItemClassification.progression,
    "Gun Unlock": ItemClassification.progression,
    "Bomb Unlock": ItemClassification.progression,
    "Rocket Launcher Unlock": ItemClassification.progression,
    "Rocket Booster Unlock": ItemClassification.progression,
    "Leaf Blower Unlock": ItemClassification.progression,
    "Cable Unlock": ItemClassification.progression,
    "Vehicle Thruster Unlock": ItemClassification.progression,
    "Nitroglycerin Unlock": ItemClassification.progression,
    "Hunting Rifle Unlock": ItemClassification.progression,
    "BlueTide Unlock": ItemClassification.progression,

    "Blowtorch Fuel Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Shotgun Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Shotgun Range Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Shotgun Damage Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Plank Amount Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Plank Width Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Plank Max Length Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Pipe Bomb Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Pipe Bomb Blast Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Gun Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Gun Range Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Gun Damage Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Bomb Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Bomb Blast Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Rocket Launcher Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Rocket Launcher Blast Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Rocket Booster Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Rocket Booster Power Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Rocket Booster Time Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Leaf Blower Power Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Cable Amount Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Cable Stretch Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Vehicle Thruster Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Vehicle Thruster Power Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Nitroglycerin Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,
    "Nitroglycerin Blast Upgrade": ItemClassification.progression| ItemClassification.useful,

    "Hunting Rifle Rounds Upgrade": ItemClassification.progression| ItemClassification.useful,

    "BlueTide Bottles Upgrade": ItemClassification.progression| ItemClassification.useful,
    "BlueTide Duration Upgrade": ItemClassification.progression| ItemClassification.useful,


    "Cash Bundle 20": ItemClassification.filler,
    "Cash Bundle 50": ItemClassification.filler,
    "Cash Bundle 100": ItemClassification.filler,
    "Cash Bundle 250": ItemClassification.useful,
    "Cash Bundle 500": ItemClassification.useful,
    "Cash Bundle 750": ItemClassification.useful,
    "Cash Bundle 1000": ItemClassification.useful,
    "Cash Bundle 3000": ItemClassification.useful,
}

item_name_groups = {
    "Levels": [
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

    "Easy Levels": [
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

    "Tools": [
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

    "Lee Chemicals Unlock": [
        "Lee Computers Unlock",
        "Login Devices Unlock",
        "Heavy Lifting Unlock",
        "The Tower Unlock",
        "Power Outage Unlock",
        "Flooding Unlock",
        "Malice In Woonderland Unlock",
    ],

    "West Point Marina Unlock": [
        "Making Space Unlock",
        "Classic Cars Unlock",
        "The GPS Devices Unlock",
        "Tool Up Unlock",
        "Art Return Unlock",
    ],

    "Villa Gordon Unlock": [
        "Classic Cars Unlock",
        "Fine Arts Unlock",
        "Insurance Fraud Unlock",
        "The Speed Deal Unlock",
        "A Wet Affair Unlock",
    ],

    "Hollowrock Island Unlock": [
        "The BlueTide Computers Unlock",
        "Motivational Reminder Unlock",
        "An Assortment Of Dishes Unlock",
        "The Secret Ingredients Unlock",
        "Droid Dismount Unlock",
    ],

    "Evertides Mall Unlock": [
        "Covert Chaos Unlock",
        "The Shipping Logs Unlock",
        "Ornament Ordeal Unlock",
        "Connecting The Dots Unlock",
    ],

    "Frustrum Unlock": [
        "The BlueTide Shortage Unlock",
        "Truckload Of Trouble Unlock",
        "The Pawn Shop Unlock",
    ],

    "Quilez Security Unlock": [
        "The Quilez Tools Unlock",
        "The Droid Abduction Unlock",
        "Handle With Care Unlock",
    ],

    "Isla Estocastica Unlock": [
        "The Alarm System Unlock",
        "Moving The Goods Unlock",
        "Havoc In Paradise Unlock",
        "Elena's Revenge Unlock",
    ],

    "Door Breaking Tools": [
        "Sledge Hammer Unlock"
        "Blowtorch Unlock",
        "Shotgun Unlock",
        "Gun Unlock",
        "Pipe Bomb Unlock",
        "Hunting Rifle Unlock",
    ],

    "Wall Opening Tools": [
        "Sledge Hammer Unlock"
        "Shotgun Unlock",
        "Pipe Bomb Unlock",
        "Bomb Unlock",
        "Rocket Launcher Unlock",
    ],

    "Destruction Tools": [
        "Shotgun Unlock",
        "Pipe Bomb Unlock",
        "Bomb Unlock",
        "Rocket Launcher Unlock",
        "Nitroglycerin Unlock",
    ],

    "Gun Tools": [
        "Gun Unlock",
        "Rocket Launcher Unlock",
        "Hunting Rifle Unlock",

    ],

    "Plank/Cable Unlock": [
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
        startingtools = list(item_name_groups["Tools"])

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
    startinglevels = list(item_name_groups["Easy Levels"])
    totallevels = list(item_name_groups["Levels"])
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

    if world.options.StartingTool:
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))
        itempool.append(world.create_item("Cash Bundle 50"))

        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))
        itempool.append(world.create_item("Cash Bundle 100"))

        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))
        itempool.append(world.create_item("Cash Bundle 250"))

        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))
        itempool.append(world.create_item("Cash Bundle 500"))

        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))
        itempool.append(world.create_item("Cash Bundle 750"))

        itempool.append(world.create_item("Cash Bundle 1000"))
        itempool.append(world.create_item("Cash Bundle 1000"))
        itempool.append(world.create_item("Cash Bundle 1000"))
        itempool.append(world.create_item("Cash Bundle 1000"))
        itempool.append(world.create_item("Cash Bundle 1000"))

        itempool.append(world.create_item("Cash Bundle 3000"))
        itempool.append(world.create_item("Cash Bundle 3000"))
        itempool.append(world.create_item("Cash Bundle 3000"))


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