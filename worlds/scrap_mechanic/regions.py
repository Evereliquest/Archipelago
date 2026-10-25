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

    # World
    ship = Region("Crashed Ship", world.player, world.multiworld) # Sphere 1 Locations
    mechanic_station = Region("Mechanic Station", world.player, world.multiworld) # Sphere 2
    basicfarm = Region("Basic Farm", world.player, world.multiworld)
    basicvehicle = Region("Basic Vehicle", world.player, world.multiworld)

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

    # Quests
    #mechanic_station = Region("Mechanic", world.player, world.multiworld)



# Lists all regions
    regions = [

        ship,
        mechanic_station,
        basicfarm,
        basicvehicle,

 # Delete these???
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
    for i in range(1, world.options.GrowlabAmount + 1):
        growlab = Region(f"Growlab {i}", world.player, world.multiworld)
        regions.append(growlab)


    if world.options.RandomizePlantUnlocks:
        cottonplant = Region("Cotton Plant", world.player, world.multiworld)
        pigmentflowerplant = Region("Pigment Flower Plant", world.player, world.multiworld)
        potatoplant = Region("Potato Plant", world.player, world.multiworld)
        tomatoplant = Region("Tomato Plant", world.player, world.multiworld)
        carrotplant = Region("Carrot Plant", world.player, world.multiworld)
        redbeetplant = Region("Redbeet Plant", world.player, world.multiworld)
        bananaplant = Region("Banana Plant", world.player, world.multiworld)
        chiliplant = Region("Chili Plant", world.player, world.multiworld)
        blueberryplant = Region("Blueberry Plant", world.player, world.multiworld)
        orangeplant = Region("Orange Plant", world.player, world.multiworld)
        broccoliplant = Region("Broccoli Plant", world.player, world.multiworld)
        pineappleplant = Region("Pineapple Plant", world.player, world.multiworld)

        regions.append(cottonplant)
        regions.append(pigmentflowerplant)
        regions.append(potatoplant)
        regions.append(tomatoplant)
        regions.append(carrotplant)
        regions.append(redbeetplant)
        regions.append(bananaplant)
        regions.append(chiliplant)
        regions.append(blueberryplant)
        regions.append(orangeplant)
        regions.append(broccoliplant)
        regions.append(pineappleplant)


    # Not Setup!!!!
    #if world.options.TraderSanity:
        #cottonplant = Region("Cotton Plant", world.player, world.multiworld)


    # Not Setup!!!!
    #if world.options.QuestPlatform:
        #cottonplant = Region("Cotton Plant", world.player, world.multiworld)


    # Not Setup!!!!
    #if world.options.GarmentSanity:
        #cottonplant = Region("Cotton Plant", world.player, world.multiworld)


    if world.options.SchematicSanity:

        if world.options.SchematicIntensity == 1:
            initialschematics = Region("Initial Schematics", world.player, world.multiworld)
            regions.append(initialschematics)

        # More Work!!!!
        if world.options.SchematicIntensity == 2:
            schematicboxes = Region("Schematic Boxes", world.player, world.multiworld)
            regions.append(schematicboxes)

        # More Work!!!!
        if world.options.SchematicIntensity == 3:
            questschematics = Region("Quest Schematics", world.player, world.multiworld)
            regions.append(questschematics)


    if world.options.BuildBotSanity:
        craftbotbuild = Region("Craftbot Build", world.player, world.multiworld)
        cookbotbuild = Region("Cookbot Build", world.player, world.multiworld)
        refinebotbuild = Region("Refinebot Build", world.player, world.multiworld)
        dressbotbuild = Region("Dressbot Build", world.player, world.multiworld)
        resourcecollectorbuild = Region("Resource Collector Build", world.player, world.multiworld)

        regions.append(craftbotbuild)
        regions.append(cookbotbuild)
        regions.append(refinebotbuild)
        regions.append(dressbotbuild)
        regions.append(resourcecollectorbuild)


    if world.options.BadBotSanity:
        earlybots= Region("Early Bots", world.player, world.multiworld)
        redtotebot= Region("Red Totebot", world.player, world.multiworld)
        yellowtotebot= Region("Yellow Totebot", world.player, world.multiworld)
        bluetapebot= Region("Blue Tapebot", world.player, world.multiworld)
        redtapebot= Region("Red Tapebot", world.player, world.multiworld)
        greentapebot= Region("Green Tapebot", world.player, world.multiworld)
        yellowtapebot= Region("Yellow Tapebot", world.player, world.multiworld)
        farmbot= Region("Farmbot", world.player, world.multiworld)
        cablebot= Region("Cablebot", world.player, world.multiworld)
        minerbot= Region("Minerbot", world.player, world.multiworld)

        regions.append(earlybots)
        regions.append(redtotebot)
        regions.append(yellowtotebot)
        regions.append(bluetapebot)
        regions.append(redtapebot)
        regions.append(greentapebot)
        regions.append(yellowtapebot)
        regions.append(farmbot)
        regions.append(cablebot)
        regions.append(minerbot)


    # Not Setup!!!!
    #if world.options.SpudGunSanity:
        #cottonplant = Region("Cotton Plant", world.player, world.multiworld)


# Adds all regions to list
    world.multiworld.regions += regions

# Renames the objects we lost creating them
def connect_regions(world: ScrapMechanicWorld) -> None:

    ship = world.get_region("Crashed Ship")
    mechanic_station = world.get_region("Mechanic Station")
    basicfarm = world.get_region("Basic Farm")
    basicvehicle = world.get_region("Basic Vehicle")


    # Connects the regions
    ship.connect(mechanic_station, "Crashed Ship to Mechanic Station")
    mechanic_station.connect(basicfarm, "Mechanic Station to Basic Farm")
    mechanic_station.connect(basicvehicle, "Mechanic Station to Basic Vehicle")


    for i in range(1, world.options.GrowlabAmount + 1):
        if i == 1:
            growlab_1 = world.get_region("Growlab 1")
            mechanic_station.connect(growlab_1, "Mechanic Station to Growlab 1")
            continue

        if i == 7:
            break

        growlab_1 = world.get_region(f"Growlab {i}")
        growlab_2 = world.get_region(f"Growlab {i+1}")

        growlab_1.connect(growlab_2, f"Growlab {i} to Growlab {i+1}")


    if world.options.RandomizePlantUnlocks:
        cottonplant = world.get_region("Cotton Plant")
        pigmentflowerplant = world.get_region("Pigment Flower Plant")
        potatoplant = world.get_region("Potato Plant")
        tomatoplant = world.get_region("Tomato Plant")
        carrotplant = world.get_region("Carrot Plant")
        redbeetplant = world.get_region("Redbeet Plant")
        bananaplant = world.get_region("Banana Plant")
        chiliplant = world.get_region("Chili Plant")
        blueberryplant = world.get_region("Blueberry Plant")
        orangeplant = world.get_region("Orange Plant")
        broccoliplant = world.get_region("Broccoli Plant")
        pineappleplant = world.get_region("Pineapple Plant")

        basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")
        basicfarm.connect(pigmentflowerplant, "Basic Farm to Pigment Flower Plant")
        basicfarm.connect(potatoplant, "Basic Farm to Potato Plant")
        basicfarm.connect(tomatoplant, "Basic Farm to Tomato Plant")
        basicfarm.connect(carrotplant, "Basic Farm to Carrot Plant")
        basicfarm.connect(redbeetplant, "Basic Farm to Redbeet Plant")
        basicfarm.connect(bananaplant, "Basic Farm to Banana Plant")
        basicfarm.connect(chiliplant, "Basic Farm to Chili Plant")
        basicfarm.connect(blueberryplant, "Basic Farm to Blueberry Plant")
        basicfarm.connect(orangeplant, "Basic Farm to Orange Plant")
        basicfarm.connect(broccoliplant, "Basic Farm to Broccoli Plant")
        basicfarm.connect(pineappleplant, "Basic Farm to Pineapple Plant")


    # Not Setup!!!!
    #if world.options.TraderSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")


    # Not Setup!!!!
    #if world.options.QuestPlatform:
        #cottonplant = world.get_region("Cotton Plant")
        #basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")


    # Not Setup!!!!
    #if world.options.GarmentSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")


    if world.options.BuildBotSanity:
        craftbotbuild = world.get_region("Craftbot Build")
        cookbotbuild = world.get_region("Cookbot Build")
        refinebotbuild = world.get_region("Refinebot Build")
        dressbotbuild = world.get_region("Dressbot Build")
        resourcecollectorbuild = world.get_region("Resource Collector Build")

        mechanic_station.connect(craftbotbuild, "Mechanic Station to Craftbot Build")
        mechanic_station.connect(cookbotbuild, "Mechanic Station to Cookbot Build")
        mechanic_station.connect(refinebotbuild, "Mechanic Station to Refinebot Build")
        mechanic_station.connect(dressbotbuild, "Mechanic Station to Dressbot Build")
        mechanic_station.connect(resourcecollectorbuild, "Mechanic Station to Resource Collector Build")


    if world.options.SchematicSanity:
        initialschematics = world.get_region("Initial Schematics")

        if world.options.BuildBotSanity:
            craftbotbuild = world.get_region("Craftbot Build")
            craftbotbuild.connect(initialschematics, "Craftbot Build to Initial Schematics")

            # More Work!!!!
            if world.options.SchematicIntensity > 1:
                schematicboxes = world.get_region("Schematic Boxes")

                # More Work!!!!
                if world.options.SchematicIntensity > 2:
                    questschematics = world.get_region("Quest Schematics")

        if not world.options.BuildBotSanity:
            mechanic_station.connect(initialschematics, "Mechanic Station to Initial Schematics")

            # More Work!!!!
            if world.options.SchematicIntensity > 1:
                schematicboxes = world.get_region("Schematic Boxes")

                # More Work!!!!
                if world.options.SchematicIntensity > 2:
                    questschematics = world.get_region("Quest Schematics")


    if world.options.BadBotSanity:
        earlybots = world.get_region("Early Bots")
        redtotebot = world.get_region("Red Totebot")
        yellowtotebot = world.get_region("Yellow Totebot")
        bluetapebot = world.get_region("Blue Tapebot")
        redtapebot = world.get_region("Red Tapebot")
        greentapebot = world.get_region("Green Tapebot")
        yellowtapebot = world.get_region("Yellow Tapebot")
        farmbot = world.get_region("Farmbot")
        cablebot = world.get_region("Cablebot")
        minerbot = world.get_region("Minerbot")

        ship.connect(earlybots, "Crashed Ship to Early Bots")
        # More Setup!!!!

    # Not Setup!!!!
    #if world.options.SpudGunSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")












