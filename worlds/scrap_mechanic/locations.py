from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


LOCATION_NAME_TO_ID = {

    # Initial Schematic Locations
    "Build: Connect Tool": 11,
    "Build: Paint Tool": 12,
    "Build: Weld Tool": 13,
    "Build: Cardboard Block": 16,
    "Build: Wood Block Level 1": 17,
    "Build: Wood Block Level 2": 18,
    "Build: Metal Block Level 1": 19,
    "Build: Metal Block Level 2": 20,
    "Build: Sand Block": 21,
    "Build: Concrete Block Level 1": 22,
    "Build: Concrete Block Level 2": 23,
    "Build: Glass Block": 24,
    "Build: Bearing": 25,
    "Build: Switch": 26,
    "Build: Button": 27,
    "Build: Sport Suspension": 28,
    "Build: Off-Road Suspension": 29,
    "Build: Gas Engine": 30,
    "Build: Driver's Seat": 31,
    "Build: Seat": 32,
    "Build: Controller": 33,
    "Build: Small Digital Sign": 34,
    "Build: Medium Digital Sign": 35,
    "Build: Large Digital Sign": 36,
    "Build: Radio": 37,
    "Build: Horn": 38,
    "Build: Scrap Chest": 39,
    "Build: Small Chest": 40,
    "Build: Vacuum Pump": 41,
    "Build: Vacuum Pipe": 42,
    "Build: Vacuum Pipe Corner": 43,
    "Build: Vacuum Pipe T": 44,
    "Build: Water Bucket": 45,
    "Build: Soil Bag": 46,
    "Build: Water": 47,
    "Build: Chemical": 48,
    "Build: Crude Oil": 49,
    "Build: Gasoline": 50,
    "Build: Glue": 51,
    "Build: Paint Ammo": 52,
    "Build: Ember": 53,
    "Build: Wheel": 54,
    "Build: Big Wheel": 55,
    "Build: Beacon": 56,
    "Build: Portable Craftbot": 57,
    "Build: Headlight": 58,
    "Build: Solid Net Block": 59,
    "Build: Small Pipe Short": 60,
    "Build: Small Pipe Long": 61,
    "Build: Small Pipe Bend": 62,
    "Build: Small Pipe Tee": 63,
    "Build: Small Pipe Corner": 64,
    "Build: Small Pipe Four Way": 65,
    "Build: Small Pipe Four Way Tee": 66,
    "Build: Small Pipe Five Way": 67,
    "Build: Small Pipe Six Way": 68,
    "Build: Large Windshield": 69,
    "Build: Small Windshield": 70,

    # Growlab Locations
    "Growlab Completion 1": 100,
    "Growlab Completion 2": 101,
    "Growlab Completion 3": 102,
    "Growlab Completion 4": 103,
    "Growlab Completion 5": 104,
    "Growlab Completion 6": 105,
    "Growlab Completion 7": 106,

    # Quest Locations
    "Tutorial Quest": 121,
    "Mechanic Station Quest": 122,
    "Mysterious Caller Quest": 123,
    "Feed the Farmers Quest ": 124,
    "Clear Mini Dungeon Quest": 125,
    "Build Watchtower Quest": 126,
    "Find Recording Quest": 127,
    "Warehouse Destruction Quest": 128,
    "Save the Watchtower": 129,
    "Rebuild the Watchtower": 130,
    "Find Excavation Island Quest": 131,
    "Activate Mining Hub Quest": 132,
    "Boss Train Quest": 133,
    "End Game Quest": 134,
    "Scrapyard Quest": 135,

    # Side Quest Locations
    "Build Big Fan Quest": 161,
    "Build Carousel Quest": 162,
    "Build Catapult Quest": 163,
    "Build Musicbox Quest": 164,
    "Build Saw Blade Arm Quest": 165,
    "Build Steel Bridge Quest": 166,

    "Craftbot Construction": 21,
    "Cookbot Construction": 22,
    "Refinebot Construction": 23,
    "Dressbot Construction": 24,
    "Resource Collector Construction": 25,


}



class ScrapMechanicLocation(Location):
    game = "Scrap Mechanic"


# Helper that helps later
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

# Creates all locations above
def create_all_locations(world: ScrapMechanicWorld) -> None:
    create_regular_locations(world)

def create_regular_locations(world: ScrapMechanicWorld) -> None:
    # Before we do anything, we can grab our regions we created by using world.get_region()
    oldbuildingproblem = world.get_region("Old Building Problem")


# Sets our locations to our regions, this is easier method
    oldbuildingproblem_locations = get_location_names_with_ids([
        "Old Building Problem",
    ])
    oldbuildingproblem.add_locations(oldbuildingproblem_locations, ScrapMechanicLocation)

    #if world.options.ToolUpgrades:
        #blowtorchupgrade = world.get_region("Blowtorch Upgrades")

        #blowtorchupgrade_locations = get_location_names_with_ids([
        #    "Blowtorch Fuel Upgrade 1",
        #    "Blowtorch Fuel Upgrade 2",
        #    "Blowtorch Fuel Upgrade 3",
        #    "Blowtorch Fuel Upgrade 4"
        #])
        #blowtorchupgrade.add_locations(blowtorchupgrade_locations, ScrapMechanicLocation)













