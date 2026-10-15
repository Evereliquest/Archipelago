from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld

ITEM_NAME_TO_ID = {

    # Schematics
    "Connect Tool Schematic": 11,
    "Paint Tool Schematic": 12,
    "Weld Tool Schematic": 13,
    "Cardboard Block Schematic": 16,
    "Wood Block Level 1 Schematic": 17,
    "Wood Block Level 2 Schematic": 18,
    "Metal Block Level 1 Schematic": 19,
    "Metal Block Level 2 Schematic": 20,
    "Sand Block Schematic": 21,
    "Concrete Block Level 1 Schematic": 22,
    "Concrete Block Level 2 Schematic": 23,
    "Glass Block Schematic": 24,
    "Bearing Schematic": 25,
    "Switch Schematic": 26,
    "Button Schematic": 27,
    "Sport Suspension Schematic": 28,
    "Off-Road Suspension Schematic": 29,
    "Gas Engine Schematic": 30,
    "Driver's Seat Schematic": 31,
    "Seat Schematic": 32,
    "Controller Schematic": 33,
    "Small Digital Sign Schematic": 34,
    "Medium Digital Sign Schematic": 35,
    "Large Digital Sign Schematic": 36,
    "Radio Schematic": 37,
    "Horn Schematic": 38,
    "Scrap Chest Schematic": 39,
    "Small Chest Schematic": 40,
    "Vacuum Pump Schematic": 41,
    "Vacuum Pipe Schematic": 42,
    "Vacuum Pipe Corner Schematic": 43,
    "Vacuum Pipe T Schematic": 44,
    "Water Bucket Schematic": 45,
    "Soil Bag Schematic": 46,
    "Water Schematic": 47,
    "Chemical Schematic": 48,
    "Crude Oil Schematic": 49,
    "Gasoline Schematic": 50,
    "Glue Schematic": 51,
    "Paint Ammo Schematic": 52,
    "Ember Schematic": 53,
    "Wheel Schematic": 54,
    "Big Wheel Schematic": 55,
    "Beacon Schematic": 56,
    "Portable Craftbot Schematic": 57,
    "Headlight Schematic": 58,
    "Solid Net Block Schematic": 59,
    "Small Pipe Short Schematic": 60,
    "Small Pipe Long Schematic": 61,
    "Small Pipe Bend Schematic": 62,
    "Small Pipe Tee Schematic": 63,
    "Small Pipe Corner Schematic": 64,
    "Small Pipe Four Way Schematic": 65,
    "Small Pipe Four Way Tee Schematic": 66,
    "Small Pipe Five Way Schematic": 67,
    "Small Pipe Six Way Schematic": 68,
    "Large Windshield Schematic": 69,
    "Small Windshield Schematic": 70,

    # Growlabs
    "GrowLab Key 1": 101,
    "GrowLab Key 2": 102,
    "GrowLab Key 3": 103,
    "GrowLab Key 4": 104,
    "GrowLab Key 5": 105,
    "GrowLab Key 6": 106,
    "GrowLab Key 7": 107,

    # Tools
    "Sledge Hammer Unlock": 121,
    "Lift Unlock": 122,
    "Scrap Spudgun Unlock": 123,
    "Spudgun Unlock": 124,
    #"Spudgun": 125,
    #"Spudgun": 126,
    #"Spudgun": 127,
    #"Spudgun": 128,
    #"Spudgun": 129,

    # Bots
    "Craftbot Unlock": 151,
    "Refinebot Unlock": 152,
    "Cookbot Unlock": 153,
    "Dressbot Unlock": 154,
    "Resource Collector Unlock": 155,

    # Plants
    "Cotton Seed Unlock": 171,
    "Pigment Flower Seed Unlock": 172,
    "Potato Seed Unlock": 173,
    "Tomato Seed Unlock": 174,
    "Carrot Seed Unlock": 175,
    "Redbeet Seed Unlock": 176,
    "Banana Seed Unlock": 177,
    "Chili Seed Unlock": 178,
    "Blueberry Seed Unlock": 179,
    "Orange Seed Unlock": 180,
    "Broccoli Seed Unlock": 181,
    "Pineapple Seed Unlock": 182,



    "Extra Nothing": 1000,

}

DEFAULT_ITEM_CLASSIFICATIONS = {

    # Schematics
    "Connect Tool Schematic": ItemClassification.progression| ItemClassification.useful,
    "Paint Tool Schematic": ItemClassification.useful,
    "Weld Tool Schematic": ItemClassification.progression| ItemClassification.useful,
    "Cardboard Block Schematic": ItemClassification.useful,
    "Wood Block Level 1 Schematic": ItemClassification.progression,
    "Wood Block Level 2 Schematic": ItemClassification.useful,
    "Metal Block Level 1 Schematic": ItemClassification.progression,
    "Metal Block Level 2 Schematic": ItemClassification.progression,
    "Sand Block Schematic": ItemClassification.progression,
    "Concrete Block Level 1 Schematic": ItemClassification.progression,
    "Concrete Block Level 2 Schematic": ItemClassification.useful,
    "Glass Block Schematic": ItemClassification.progression,
    "Bearing Schematic": ItemClassification.progression| ItemClassification.useful,
    "Switch Schematic": ItemClassification.progression| ItemClassification.useful,
    "Button Schematic": ItemClassification.progression| ItemClassification.useful,
    "Sport Suspension Schematic": ItemClassification.progression,
    "Off-Road Suspension Schematic": ItemClassification.progression,
    "Gas Engine Schematic": ItemClassification.progression| ItemClassification.useful,
    "Driver's Seat Schematic": ItemClassification.progression| ItemClassification.useful,
    "Seat Schematic": ItemClassification.useful,
    "Controller Schematic": ItemClassification.progression| ItemClassification.useful,
    "Small Digital Sign Schematic": ItemClassification.useful,
    "Medium Digital Sign Schematic": ItemClassification.useful,
    "Large Digital Sign Schematic": ItemClassification.useful,
    "Radio Schematic": ItemClassification.useful,
    "Horn Schematic": ItemClassification.useful,
    "Scrap Chest Schematic": ItemClassification.progression| ItemClassification.useful,
    "Small Chest Schematic": ItemClassification.progression| ItemClassification.useful,
    "Vacuum Pump Schematic": ItemClassification.progression| ItemClassification.useful,
    "Vacuum Pipe Schematic": ItemClassification.useful,
    "Vacuum Pipe Corner Schematic": ItemClassification.useful,
    "Vacuum Pipe T Schematic": ItemClassification.useful,
    "Water Bucket Schematic": ItemClassification.progression,
    "Soil Bag Schematic": ItemClassification.useful,
    "Water Schematic": ItemClassification.progression,
    "Chemical Schematic": ItemClassification.progression,
    "Crude Oil Schematic": ItemClassification.progression,
    "Gasoline Schematic": ItemClassification.progression| ItemClassification.useful,
    "Glue Schematic": ItemClassification.progression,
    "Paint Ammo Schematic": ItemClassification.progression,
    "Ember Schematic": ItemClassification.useful,
    "Wheel Schematic": ItemClassification.progression| ItemClassification.useful,
    "Big Wheel Schematic": ItemClassification.progression| ItemClassification.useful,
    "Beacon Schematic": ItemClassification.useful,
    "Portable Craftbot Schematic": ItemClassification.useful,
    "Headlight Schematic": ItemClassification.useful,
    "Solid Net Block Schematic": ItemClassification.useful,
    "Small Pipe Short Schematic": ItemClassification.useful,
    "Small Pipe Long Schematic": ItemClassification.useful,
    "Small Pipe Bend Schematic": ItemClassification.useful,
    "Small Pipe Tee Schematic": ItemClassification.useful,
    "Small Pipe Corner Schematic": ItemClassification.useful,
    "Small Pipe Four Way Schematic": ItemClassification.useful,
    "Small Pipe Four Way Tee Schematic": ItemClassification.useful,
    "Small Pipe Five Way Schematic": ItemClassification.useful,
    "Small Pipe Six Way Schematic": ItemClassification.useful,
    "Large Windshield Schematic": ItemClassification.filler,
    "Small Windshield Schematic": ItemClassification.filler,

    # Growlabs
    "GrowLab Key 1": ItemClassification.progression,
    "GrowLab Key 2": ItemClassification.progression,
    "GrowLab Key 3": ItemClassification.progression,
    "GrowLab Key 4": ItemClassification.progression,
    "GrowLab Key 5": ItemClassification.progression,
    "GrowLab Key 6": ItemClassification.progression,
    "GrowLab Key 7": ItemClassification.progression,





    "Extra Nothing": ItemClassification.filler,
}

item_name_groups = {
    "Craftbot Schematics": [
        "Connect Tool Schematic",
        "Paint Tool Schematic",
        "Weld Tool Schematic",
        "Scrap Spud Gun Schematic",
        "Spud Gun Schematic",
        "Cardboard Block Schematic",
        "Wood Block Level 1 Schematic",
        "Wood Block Level 2 Schematic",
        "Metal Block Level 1 Schematic",
        "Metal Block Level 2 Schematic",
        "Sand Block Schematic",
        "Concrete Block Level 1 Schematic",
        "Concrete Block Level 2 Schematic",
        "Glass Block Schematic",
        "Bearing Schematic",
        "Switch Schematic",
        "Button Schematic",
        "Sport Suspension Schematic",
        "Off-Road Suspension Schematic",
        "Gas Engine Schematic",
        "Driver's Seat Schematic",
        "Seat Schematic",
        "Controller Schematic",
        "Small Digital Sign Schematic",
        "Medium Digital Sign Schematic",
        "Large Digital Sign Schematic",
        "Radio Schematic",
        "Horn Schematic",
        "Scrap Chest Schematic",
        "Small Chest Schematic",
        "Vacuum Pump Schematic",
        "Vacuum Pipe Schematic",
        "Vacuum Pipe Corner Schematic",
        "Vacuum Pipe T Schematic",
        "Water Bucket Schematic",
        "Soil Bag Schematic",
        "Water Schematic",
        "Chemical Schematic",
        "Crude Oil Schematic",
        "Gasoline Schematic",
        "Glue Schematic",
        "Paint Ammo Schematic",
        "Ember Schematic",
        "Wheel Schematic",
        "Big Wheel Schematic",
        "Beacon Schematic",
        "Portable Craftbot Schematic",
        "Headlight Schematic",
        "Solid Net Block Schematic",
        "Small Pipe Short Schematic",
        "Small Pipe Long Schematic",
        "Small Pipe Bend Schematic",
        "Small Pipe Tee Schematic",
        "Small Pipe Corner Schematic",
        "Small Pipe Four Way Schematic",
        "Small Pipe Four Way Tee Schematic",
        "Small Pipe Five Way Schematic",
        "Small Pipe Six Way Schematic",
        "Large Windshield Schematic",
        "Small Windshield Schematic",
    ],

    "Growlab Keys": [

        "GrowLab Key 1",
        "GrowLab Key 2",
        "GrowLab Key 3",
        "GrowLab Key 4",
        "GrowLab Key 5",
        "GrowLab Key 6",
        "GrowLab Key 7",
    ],

}


class ScrapMechanicItem(Item):
    game = "Scrap Mechanic"


def get_random_filler_item_name(world: ScrapMechanicWorld) -> str:
    return "Extra Nothing"

#def create_item_with_correct_classification(world: ScrapMechanicWorld, name: str) -> ScrapMechanicItem:
#    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
#    if name == "Elena's Revenge Unlock":
#        classification = ItemClassification.progression

#    return ScrapMechanicItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: ScrapMechanicWorld) -> None:
    itempool: list[Item] = [

        world.create_item("GrowLab Key 1"),
    ]


    if world.options.GrowlabAmount == 2:
        itempool.append(world.create_item("GrowLab Key 2"))
    elif world.options.GrowlabAmount == 3:
        itempool.append(world.create_item("GrowLab Key 2"))
        itempool.append(world.create_item("GrowLab Key 3"))
    elif world.options.GrowlabAmount == 4:
        itempool.append(world.create_item("GrowLab Key 2"))
        itempool.append(world.create_item("GrowLab Key 3"))
        itempool.append(world.create_item("GrowLab Key 4"))
    elif world.options.GrowlabAmount == 5:
        itempool.append(world.create_item("GrowLab Key 2"))
        itempool.append(world.create_item("GrowLab Key 3"))
        itempool.append(world.create_item("GrowLab Key 4"))
        itempool.append(world.create_item("GrowLab Key 5"))
    elif world.options.GrowlabAmount == 6:
        itempool.append(world.create_item("GrowLab Key 2"))
        itempool.append(world.create_item("GrowLab Key 3"))
        itempool.append(world.create_item("GrowLab Key 4"))
        itempool.append(world.create_item("GrowLab Key 5"))
        itempool.append(world.create_item("GrowLab Key 6"))
    elif world.options.GrowlabAmount == 7:
        itempool.append(world.create_item("GrowLab Key 2"))
        itempool.append(world.create_item("GrowLab Key 3"))
        itempool.append(world.create_item("GrowLab Key 4"))
        itempool.append(world.create_item("GrowLab Key 5"))
        itempool.append(world.create_item("GrowLab Key 6"))
        itempool.append(world.create_item("GrowLab Key 7"))

    if world.options.RandomizePlantUnlocks:
        itempool.append(world.create_item("Cotton Seed Unlock"))
        itempool.append(world.create_item("Pigment Flower Seed Unlock"))
        itempool.append(world.create_item("Potato Seed Unlock"))
        itempool.append(world.create_item("Tomato Seed Unlock"))
        itempool.append(world.create_item("Carrot Seed Unlock"))
        itempool.append(world.create_item("Redbeet Seed Unlock"))
        itempool.append(world.create_item("Banana Seed Unlock"))
        itempool.append(world.create_item("Chili Seed Unlock"))
        itempool.append(world.create_item("Blueberry Seed Unlock"))
        itempool.append(world.create_item("Orange Seed Unlock"))
        itempool.append(world.create_item("Broccoli Seed Unlock"))
        itempool.append(world.create_item("Pineapple Seed Unlock"))
    else:
        world.push_precollected(world.create_item("Cotton Seed Unlock"))
        world.push_precollected(world.create_item("Pigment Flower Seed Unlock"))
        world.push_precollected(world.create_item("Potato Seed Unlock"))
        world.push_precollected(world.create_item("Tomato Seed Unlock"))
        world.push_precollected(world.create_item("Carrot Seed Unlock"))
        world.push_precollected(world.create_item("Redbeet Seed Unlock"))
        world.push_precollected(world.create_item("Banana Seed Unlock"))
        world.push_precollected(world.create_item("Chili Seed Unlock"))
        world.push_precollected(world.create_item("Blueberry Seed Unlock"))
        world.push_precollected(world.create_item("Orange Seed Unlock"))
        world.push_precollected(world.create_item("Broccoli Seed Unlock"))
        world.push_precollected(world.create_item("Pineapple Seed Unlock"))

    if world.options.TraderSanity:
        world.push_precollected(world.create_item("Sledge Hammer Unlock"))

    if world.options.SchematicSanity:
        world.push_precollected(world.create_item("Sledge Hammer Unlock"))

    if world.options.SchematicIntensity:
        world.push_precollected(world.create_item("Sledge Hammer Unlock"))

    if world.options.BotSanity:
        itempool.append(world.create_item("Craftbot Unlock"))
        itempool.append(world.create_item("Refinebot Unlock"))
        itempool.append(world.create_item("Cookbot Unlock"))
        itempool.append(world.create_item("Dressbot Unlock"))
        itempool.append(world.create_item("Resource Collector Unlock"))
    else:
        world.push_precollected(world.create_item("Craftbot Unlock"))
        world.push_precollected(world.create_item("Refinebot Unlock"))
        world.push_precollected(world.create_item("Cookbot Unlock"))
        world.push_precollected(world.create_item("Dressbot Unlock"))
        world.push_precollected(world.create_item("Resource Collector Unlock"))

    if world.options.SpudGunSanity:
        itempool.append(world.create_item("Scrap Spudgun Unlock"))
        itempool.append(world.create_item("Spudgun Unlock"))
    else:
        world.push_precollected(world.create_item("Scrap Spudgun Unlock"))
        world.push_precollected(world.create_item("Spudgun Unlock"))

    if world.options.LiftSanity:
        itempool.append(world.create_item("Lift Unlock"))
    else:
        world.push_precollected(world.create_item("Lift Unlock"))

    if world.options.HammerSanity:
        itempool.append(world.create_item("Sledge Hammer Unlock"))
    else:
        world.push_precollected(world.create_item("Sledge Hammer Unlock"))






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