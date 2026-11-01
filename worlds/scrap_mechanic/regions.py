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
    startingvehicle = Region("Starting Vehicle", world.player, world.multiworld)
    basicvehicle = Region("Basic Vehicle", world.player, world.multiworld)
    goodvechicle = Region("Good Vehicle", world.player, world.multiworld)
    earlytrader = Region("Early Trader", world.player, world.multiworld)
    trader = Region("Trader", world.player, world.multiworld)

    craftbot = Region("Craftbot", world.player, world.multiworld)
    refinebot = Region("Refinebot", world.player, world.multiworld)
    cookbot = Region("Cookbot", world.player, world.multiworld)
    dressbot = Region("Dressbot", world.player, world.multiworld)
    schematicbot = Region("Schematicbot", world.player, world.multiworld)

    lift = Region("Lift", world.player, world.multiworld)
    sledgehammer = Region("Sledge Hammer", world.player, world.multiworld)
    scrapspudgun = Region("Scrap Spud Gun", world.player, world.multiworld)
    spudgun = Region("Spud Gun", world.player, world.multiworld)
    bettergun = Region("Better Gun", world.player, world.multiworld)

    metal1 = Region("Metal 1", world.player, world.multiworld)
    metal2 = Region("Metal 2", world.player, world.multiworld)
    metal3 = Region("Metal 3", world.player, world.multiworld)
    wood1 = Region("Wood 1", world.player, world.multiworld)
    wood2 = Region("Wood 2", world.player, world.multiworld)
    wood3 = Region("Wood 3", world.player, world.multiworld)

    glass = Region("Glass", world.player, world.multiworld)
    ember = Region("Ember", world.player, world.multiworld)
    honeycomb = Region("Honeycomb", world.player, world.multiworld)
    crudeoil = Region("Crude Oil", world.player, world.multiworld)
    chemicals = Region("Chemicals", world.player, world.multiworld)

    mainquest1 = Region("Main Quest 1", world.player, world.multiworld)
    mainquest2 = Region("Main Quest 2", world.player, world.multiworld)
    mainquest3 = Region("Main Quest 3", world.player, world.multiworld)
    mainquest4 = Region("Main Quest 4", world.player, world.multiworld)
    mainquest5 = Region("Main Quest 5", world.player, world.multiworld)
    mainquest6 = Region("Main Quest 6", world.player, world.multiworld)
    mainquest7 = Region("Main Quest 7", world.player, world.multiworld)
    mainquest8 = Region("Main Quest 8", world.player, world.multiworld)
    mainquest9 = Region("Main Quest 9", world.player, world.multiworld)

    # Lists all regions
    regions = [

        ship,
        mechanic_station,
        basicfarm,
        startingvehicle,
        basicvehicle,
        goodvechicle,
        earlytrader,
        trader,

        craftbot,
        refinebot,
        cookbot,
        dressbot,
        schematicbot,

        lift,
        sledgehammer,
        scrapspudgun,
        spudgun,
        bettergun,

        metal1,
        metal2,
        metal3,
        wood1,
        wood2,
        wood3,

        glass,
        ember,
        honeycomb,
        crudeoil,
        chemicals,

        mainquest1,
        mainquest2,
        mainquest3,
        mainquest4,
        mainquest5,
        mainquest6,
        mainquest7,
        mainquest8,
        mainquest9,

    ]

# Creates region if option is enabled
    for i in range(1, world.options.GrowlabAmount + 1):
        growlab = Region(f"Growlab {i}", world.player, world.multiworld)
        regions.append(growlab)


    # Not Setup!!!!
    #if world.options.SchematicBoxes:
        #cottonplant = Region("Cotton Plant", world.player, world.multiworld)
# Check new save, write down all items, erase blocks/quest items?

    if world.options.SupplyQuestSanity:
        supplyquest1 = Region("Supply Quest 1", world.player, world.multiworld)
        supplyquest2 = Region("Supply Quest 2", world.player, world.multiworld)
        supplyquest3 = Region("Supply Quest 3", world.player, world.multiworld)
        supplyquest4 = Region("Supply Quest 4", world.player, world.multiworld)
        supplyquest5 = Region("Supply Quest 5", world.player, world.multiworld)
        supplyquest6 = Region("Supply Quest 6", world.player, world.multiworld)
        supplyquest7 = Region("Supply Quest 7", world.player, world.multiworld)
        supplyquest8 = Region("Supply Quest 8", world.player, world.multiworld)

        regions.append(supplyquest1)
        regions.append(supplyquest2)
        regions.append(supplyquest3)
        regions.append(supplyquest4)
        regions.append(supplyquest5)
        regions.append(supplyquest6)
        regions.append(supplyquest7)
        regions.append(supplyquest8)


    if world.options.FarmerQuestSanity:
        farmquestearly = Region("Farmer Quests Early", world.player, world.multiworld)
        farmquestlate = Region("Farmer Quests Late", world.player, world.multiworld)

        regions.append(farmquestearly)
        regions.append(farmquestlate)


    if world.options.ScrapperQuestSanity:
        scrapperquest = Region("Scrapper Quests", world.player, world.multiworld)

        regions.append(scrapperquest)


    if world.options.BadBotSanity:
        earlybots= Region("Early Bots", world.player, world.multiworld)
        totebots= Region("Totebots", world.player, world.multiworld)
        tapebots= Region("Tapebots", world.player, world.multiworld)
        farmbot= Region("Farmbot", world.player, world.multiworld)
        undergroundbots= Region("Under Ground Bots", world.player, world.multiworld)

        regions.append(earlybots)
        regions.append(totebots)
        regions.append(tapebots)
        regions.append(farmbot)
        regions.append(undergroundbots)


    if world.options.TraderSanity:
        tradefarmers = Region("Trade Farmers", world.player, world.multiworld)
        tradetomatoes = Region("Trade Tomatoes", world.player, world.multiworld)
        tradecarrots = Region("Trade Carrots", world.player, world.multiworld)
        traderedbeets = Region("Trade Redbeets", world.player, world.multiworld)
        tradebananas = Region("Trade Bananas", world.player, world.multiworld)
        tradeblueberries = Region("Trade Blueberries", world.player, world.multiworld)
        tradeoranges = Region("Trade Oranges", world.player, world.multiworld)
        tradebroccoli = Region("Trade Broccoli", world.player, world.multiworld)
        tradepineapples = Region("Trade Pineapples", world.player, world.multiworld)

        regions.append(tradefarmers)
        regions.append(tradetomatoes)
        regions.append(tradecarrots)
        regions.append(traderedbeets)
        regions.append(tradebananas)
        regions.append(tradeblueberries)
        regions.append(tradeoranges)
        regions.append(tradebroccoli)
        regions.append(tradepineapples)


# -------------


# Adds all regions to list
    world.multiworld.regions += regions

# Renames the objects we lost creating them
def connect_regions(world: ScrapMechanicWorld) -> None:

    ship = world.get_region("Crashed Ship")
    mechanic_station = world.get_region("Mechanic Station")
    basicfarm = world.get_region("Basic Farm")
    startingvehicle = world.get_region("Starting Vehicle")
    basicvehicle = world.get_region("Basic Vehicle")
    goodvechicle = world.get_region("Good Vehicle")
    earlytrader = world.get_region("Early Trader")
    trader = world.get_region("Trader")

    craftbot = world.get_region("Craftbot")
    refinebot = world.get_region("Refinebot")
    cookbot = world.get_region("Cookbot")
    dressbot = world.get_region("Dressbot")
    schematicbot = world.get_region("Schematicbot")

    lift = world.get_region("Lift")
    sledgehammer = world.get_region("Sledge Hammer")
    scrapspudgun = world.get_region("Scrap Spud Gun")
    spudgun = world.get_region("Spud Gun")
    bettergun = world.get_region("Better Gun")

    metal1 = world.get_region("Metal 1")
    metal2 = world.get_region("Metal 2")
    metal3 = world.get_region("Metal 1")
    wood1 = world.get_region("Wood 1")
    wood2 = world.get_region("Wood 2")
    wood3 = world.get_region("Wood 3")

    glass = world.get_region("Metal 1")
    ember = world.get_region("Metal 1")
    honeycomb = world.get_region("Metal 1")
    crudeoil = world.get_region("Metal 1")
    chemicals = world.get_region("Metal 1")

    mainquest1 = world.get_region("Main Quest 1")
    mainquest2 = world.get_region("Main Quest 2")
    mainquest3 = world.get_region("Main Quest 3")
    mainquest4 = world.get_region("Main Quest 4")
    mainquest5 = world.get_region("Main Quest 5")
    mainquest6 = world.get_region("Main Quest 6")
    mainquest7 = world.get_region("Main Quest 7")
    mainquest8 = world.get_region("Main Quest 8")
    mainquest9 = world.get_region("Main Quest 9")


    # Connects the regions
    ship.connect(mechanic_station, "Crashed Ship to Mechanic Station")
    mechanic_station.connect(basicfarm, "Mechanic Station to Basic Farm")
    ship.connect(startingvehicle, "Crashed Ship to Starting Vehicle")
    startingvehicle.connect(basicvehicle, "Starting Vehicle to Basic Vehicle")
    basicvehicle.connect(goodvechicle, "Basic Vehicle to Good Vehicle")
    startingvehicle.connect(earlytrader, "Starting Vehicle to Early Trader")
    basicvehicle.connect(trader, "Basic Vehicle to Trader")

    mechanic_station.connect(craftbot, "Mechanic Station to Craftbot")
    metal1.connect(refinebot, "Metal 1 to Refinebot")
    metal2.connect(cookbot, "Metal 2 to Cookbot")
    mechanic_station.connect(dressbot, "Metal 2 to Dressbot")
    basicvehicle.connect(schematicbot, "Basic Vehicle to Schematicbot")

    ship.connect(lift, "Crashed Ship to Lift")
    ship.connect(sledgehammer, "Crashed Ship to Sledge Hammer")

    craftbot.connect(mainquest1, "Craftbot to Main Quest 1")
    mainquest1.connect(mainquest2, "Main Quest 1 to Main Quest 2")
    mainquest2.connect(mainquest3, "Main Quest 2 to Main Quest 3")
    mainquest3.connect(mainquest4, "Main Quest 3 to Main Quest 4")
    mainquest4.connect(mainquest5, "Main Quest 4 to Main Quest 5")
    mainquest5.connect(mainquest6, "Main Quest 5 to Main Quest 6")
    mainquest6.connect(mainquest7, "Main Quest 6 to Main Quest 7")
    mainquest7.connect(mainquest8, "Main Quest 7 to Main Quest 8")
    mainquest8.connect(mainquest9, "Main Quest 8 to Main Quest 9")




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


    # Not Setup!!!!
    #if world.options.SchematicBoxes:
        #cottonplant = world.get_region("Cotton Plant")
        #basicfarm.connect(cottonplant, "Basic Farm to Cotton Plant")


    if world.options.SupplyQuestSanity:
        supplyquest1 = world.get_region("Supply Quest 1")
        supplyquest2 = world.get_region("Supply Quest 2")
        supplyquest3 = world.get_region("Supply Quest 3")
        supplyquest4 = world.get_region("Supply Quest 4")
        supplyquest5 = world.get_region("Supply Quest 5")
        supplyquest6 = world.get_region("Supply Quest 6")
        supplyquest7 = world.get_region("Supply Quest 7")
        supplyquest8 = world.get_region("Supply Quest 8")

        mainquest2.connect(supplyquest1, "Main Quest 2 to Supply Quest 1")
        supplyquest1.connect(supplyquest2, "Main Quest 1 to Supply Quest 2")
        supplyquest2.connect(supplyquest3, "Main Quest 2 to Supply Quest 3")
        supplyquest3.connect(supplyquest4, "Main Quest 3 to Supply Quest 4")
        supplyquest4.connect(supplyquest5, "Main Quest 4 to Supply Quest 5")
        supplyquest5.connect(supplyquest6, "Main Quest 5 to Supply Quest 6")
        supplyquest6.connect(supplyquest7, "Main Quest 6 to Supply Quest 7")
        supplyquest7.connect(supplyquest8, "Main Quest 7 to Supply Quest 8")


    if world.options.FarmerQuestSanity:
        farmquestearly = world.get_region("Farmer Quests Early")
        farmquestlate = world.get_region("Farmer Quests Late")

        basicvehicle.connect(farmquestearly, "Basic Vehicle to Farmer Quests Early")
        mainquest5.connect(farmquestlate, "Main Quest 5 to Farmer Quests Late")
        # Return Later


    if world.options.ScrapperQuestSanity:
        scrapperquest = world.get_region("Scrapper Quests")

        mainquest5.connect(scrapperquest, "Main Quest 5 to Scrapper Quests")
        # Return Later


    if world.options.BadBotSanity:
        earlybots = world.get_region("Early Bots")
        totebots = world.get_region("Totebots")
        tapebots = world.get_region("Tapebots")
        farmbot = world.get_region("Farmbot")
        undergroundbots = world.get_region("Under Ground Bots")

        ship.connect(earlybots, "Crashed Ship to Early Bots")
        ship.connect(totebots, "Crashed Ship to Early Bots")
        ship.connect(tapebots, "Crashed Ship to Early Bots")
        ship.connect(farmbot, "Crashed Ship to Early Bots")
        ship.connect(undergroundbots, "Crashed Ship to Early Bots")


    if world.options.TraderSanity:
        tradefarmers = world.get_region("Trade Farmers")
        tradetomatoes = world.get_region("Trade Tomatoes")
        tradecarrots = world.get_region("Trade Carrots")
        traderedbeets = world.get_region("Trade Redbeets")
        tradebananas = world.get_region("Trade Bananas")
        tradeblueberries = world.get_region("Trade Blueberries")
        tradeoranges = world.get_region("Trade Oranges")
        tradebroccoli = world.get_region("Trade Broccoli")
        tradepineapples = world.get_region("Trade Pineapples")

        trader.connect(tradefarmers, "Trader to Trade Farmers")
        trader.connect(tradetomatoes, "Trader to Trade Tomatoes")
        trader.connect(tradecarrots, "Trader to Trade Carrots")
        trader.connect(traderedbeets, "Trader to Trade Redbeets")
        trader.connect(tradebananas, "Trader to Trade Bananas")
        trader.connect(tradeblueberries, "Trader to Trade Blueberries")
        trader.connect(tradeoranges, "Trader to Trade Oranges")
        trader.connect(tradebroccoli, "Trader to Trade Broccoli")
        trader.connect(tradepineapples, "Trader to Trade Pineapples")


    if world.options.SpudGunSanity:
        ship.connect(scrapspudgun, "Crashed Ship to Scrap Spud Gun")
        ship.connect(spudgun, "Crashed Ship to Spud Gun")
        ship.connect(bettergun, "Crashed Ship to Better Gun")

    if not world.options.SpudGunSanity:
        sledgehammer.connect(scrapspudgun, "Sledge Hammer to Scrap Spud Gun")
        scrapspudgun.connect(spudgun, "Scrap Spud Gun to Spud Gun")
        spudgun.connect(bettergun, "Spud Gun to Better Gun")











