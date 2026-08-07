from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


def create_and_connect_regions(world: ScrapMechanicWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

# Creates all regions
def create_all_regions(world: ScrapMechanicWorld) -> None:
    ship = Region("Crashed Ship", world.player, world.multiworld)
    mechanic_station_1 = Region("Mechanic Station 1", world.player, world.multiworld)



# Lists all regions
    regions = [ship, mechanic_station_1,
               ]

# Creates region if option is enabled
    #if world.options.ToolUpgrades:
        #blowtorchupgrade = Region("Blowtorch Upgrades", world.player, world.multiworld)

        #regions.append(blowtorchupgrade)

# Adds all regions to list
    world.multiworld.regions += regions

# Renames the objects we lost creating them
def connect_regions(world: ScrapMechanicWorld) -> None:

    ship = world.get_region("Crashed Ship")
    mechanic_station_1 = world.get_region("Mechanic Station 1")


    # Connects the regions
    ship.connect(mechanic_station_1, "Crashed Ship to Mechanic Station 1")


    #if world.options.ToolUpgrades:
        #blowtorchupgrade = world.get_region("Blowtorch Upgrades")

        #menu.connect(blowtorchupgrade, "Main Menu to Blowtorch Upgrades")

