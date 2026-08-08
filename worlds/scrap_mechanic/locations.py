from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


LOCATION_NAME_TO_ID = {

#   Mission Locations
    "Growlab Completion 1": 1,
    "Growlab Completion 2": 2,
    "Growlab Completion 3": 3,
    "Growlab Completion 4": 4,
    "Growlab Completion 5": 5,
    "Growlab Completion 6": 6,
    "Growlab Completion 7": 7,

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













