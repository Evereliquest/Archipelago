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

    # Initial
    ship = Region("Crashed Ship", world.player, world.multiworld)
    mechanic_station_1 = Region("Mechanic Station 1", world.player, world.multiworld)

    # Growlabs
    growlab_1 = Region("Grow Lab 1", world.player, world.multiworld)
    growlab_2= Region("Grow Lab 2", world.player, world.multiworld)
    growlab_3 = Region("Grow Lab 3", world.player, world.multiworld)
    growlab_4 = Region("Grow Lab 4", world.player, world.multiworld)
    growlab_5 = Region("Grow Lab 5", world.player, world.multiworld)
    growlab_6 = Region("Grow Lab 6", world.player, world.multiworld)
    growlab_7 = Region("Grow Lab 7", world.player, world.multiworld)

    # Schematics
    build_connect_tool = Region("Build: Connect Tool", world.player, world.multiworld)
    build_paint_tool = Region("Build: Paint Tool", world.player, world.multiworld)
    build_weld_tool = Region("Build: Weld Tool", world.player, world.multiworld)
    build_cardboard_block = Region("Build: Cardboard Block", world.player, world.multiworld)
    build_wood_block_level_1 = Region("Build: Wood Block Level 1", world.player, world.multiworld)
    build_wood_block_level_2 = Region("Build: Wood Block Level 2", world.player, world.multiworld)
    build_metal_block_level_1 = Region("Build: Metal Block Level 1", world.player, world.multiworld)
    build_metal_block_level_2 = Region("Build: Metal Block Level 2", world.player, world.multiworld)
    build_sand_block = Region("Build: Sand Block", world.player, world.multiworld)
    build_concrete_block_level_1 = Region("Build: Concrete Block Level 1", world.player, world.multiworld)
    build_concrete_block_level_2 = Region("Build: Concrete Block Level 2", world.player, world.multiworld)
    build_glass_block = Region("Build: Glass Block", world.player, world.multiworld)
    build_bearing = Region("Build: Bearing", world.player, world.multiworld)
    build_switch = Region("Build: Switch", world.player, world.multiworld)
    build_button = Region("Build: Button", world.player, world.multiworld)
    build_sport_suspension = Region("Build: Sport Suspension", world.player, world.multiworld)
    build_off_road_suspension = Region("Build: Off-Road Suspension", world.player, world.multiworld)
    build_gas_engine = Region("Build: Gas Engine", world.player, world.multiworld)
    build_drivers_seat = Region("Build: Driver's Seat", world.player, world.multiworld)
    build_seat = Region("Build: Seat", world.player, world.multiworld)
    build_controller = Region("Build: Controller", world.player, world.multiworld)
    build_small_digital_sign = Region("Build: Small Digital Sign", world.player, world.multiworld)
    build_medium_digital_sign = Region("Build: Medium Digital Sign", world.player, world.multiworld)
    build_large_digital_sign = Region("Build: Large Digital Sign", world.player, world.multiworld)
    build_radio = Region("Build: Radio", world.player, world.multiworld)
    build_horn = Region("Build: Horn", world.player, world.multiworld)
    build_scrap_chest = Region("Build: Scrap Chest", world.player, world.multiworld)
    build_small_chest = Region("Build: Small Chest", world.player, world.multiworld)
    build_vacuum_pump = Region("Build: Vacuum Pump", world.player, world.multiworld)
    build_vacuum_pipe = Region("Build: Vacuum Pipe", world.player, world.multiworld)
    build_vacuum_pipe_corner = Region("Build: Vacuum Pipe Corner", world.player, world.multiworld)
    build_vacuum_pipe_t = Region("Build: Vacuum Pipe T", world.player, world.multiworld)
    build_water_bucket = Region("Build: Water Bucket", world.player, world.multiworld)
    build_soil_bag = Region("Build: Soil Bag", world.player, world.multiworld)
    build_water = Region("Build: Water", world.player, world.multiworld)
    build_chemical = Region("Build: Chemical", world.player, world.multiworld)
    build_crude_oil = Region("Build: Crude Oil", world.player, world.multiworld)
    build_gasoline = Region("Build: Gasoline", world.player, world.multiworld)
    build_glue = Region("Build: Glue", world.player, world.multiworld)
    build_paint_ammo = Region("Build: Paint Ammo", world.player, world.multiworld)
    build_ember = Region("Build: Ember", world.player, world.multiworld)
    build_wheel = Region("Build: Wheel", world.player, world.multiworld)
    build_big_wheel = Region("Build: Big Wheel", world.player, world.multiworld)
    build_beacon = Region("Build: Beacon", world.player, world.multiworld)
    build_portable_craftbot = Region("Build: Portable Craftbot", world.player, world.multiworld)
    build_headlight = Region("Build: Headlight", world.player, world.multiworld)
    build_solid_net_block = Region("Build: Solid Net Block", world.player, world.multiworld)
    build_small_pipe_short = Region("Build: Small Pipe Short", world.player, world.multiworld)
    build_small_pipe_long = Region("Build: Small Pipe Long", world.player, world.multiworld)
    build_small_pipe_bend = Region("Build: Small Pipe Bend", world.player, world.multiworld)
    build_small_pipe_tee = Region("Build: Small Pipe Tee", world.player, world.multiworld)
    build_small_pipe_corner = Region("Build: Small Pipe Corner", world.player, world.multiworld)
    build_small_pipe_four_way = Region("Build: Small Pipe Four Way", world.player, world.multiworld)
    build_small_pipe_four_way_tee = Region("Build: Small Pipe Four Way Tee", world.player, world.multiworld)
    build_small_pipe_five_way = Region("Build: Small Pipe Five Way", world.player, world.multiworld)
    build_small_pipe_six_way = Region("Build: Small Pipe Six Way", world.player, world.multiworld)
    build_large_windshield = Region("Build: Large Windshield", world.player, world.multiworld)
    build_small_windshield = Region("Build: Small Windshield", world.player, world.multiworld)

    #
    #mechanic_station_1 = Region("Mechanic", world.player, world.multiworld)



# Lists all regions
    regions = [

        ship,
        mechanic_station_1,

        growlab_1,
        growlab_2,
        growlab_3,
        growlab_4,
        growlab_5,
        growlab_6,
        growlab_7,

        build_connect_tool,
        build_paint_tool,
        build_weld_tool,
        build_cardboard_block,
        build_wood_block_level_1,
        build_wood_block_level_2,
        build_metal_block_level_1,
        build_metal_block_level_2,
        build_sand_block,
        build_concrete_block_level_1,
        build_concrete_block_level_2,
        build_glass_block,
        build_bearing,
        build_switch,
        build_button,
        build_sport_suspension,
        build_off_road_suspension,
        build_gas_engine,
        build_drivers_seat,
        build_seat,
        build_controller,
        build_small_digital_sign,
        build_medium_digital_sign,
        build_large_digital_sign,
        build_radio,
        build_horn,
        build_scrap_chest,
        build_small_chest,
        build_vacuum_pump,
        build_vacuum_pipe,
        build_vacuum_pipe_corner,
        build_vacuum_pipe_t,
        build_water_bucket,
        build_soil_bag,
        build_water,
        build_chemical,
        build_crude_oil,
        build_gasoline,
        build_glue,
        build_paint_ammo,
        build_ember,
        build_wheel,
        build_big_wheel,
        build_beacon,
        build_portable_craftbot,
        build_headlight,
        build_solid_net_block,
        build_small_pipe_short,
        build_small_pipe_long,
        build_small_pipe_bend,
        build_small_pipe_tee,
        build_small_pipe_corner,
        build_small_pipe_four_way,
        build_small_pipe_four_way_tee,
        build_small_pipe_five_way,
        build_small_pipe_six_way,
        build_large_windshield,
        build_small_windshield,
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

