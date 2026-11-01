from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


LOCATION_NAME_TO_ID = {

    # Growlab Locations
    "Growlab Completion 1": 101,
    "Growlab Completion 2": 102,
    "Growlab Completion 3": 103,
    "Growlab Completion 4": 104,
    "Growlab Completion 5": 105,
    "Growlab Completion 6": 106,
    "Growlab Completion 7": 107,

    # Quest Locations
    "Quest: Getting Started": 121,
    "Quest: The Mechanic Station": 122,
    "Quest: A Stranger in Need": 123,
    "Quest: Palette Cleanser": 124,
    "Quest: A Farmer's Side Hustle": 125,
    "Quest: Home is Where Your Couch is": 126,
    "Quest: Lost and Found": 127,
    "Quest: The Warehouse": 128,
    "Quest: Wonk-Y business": 129,
    "Quest: Where's the Fire?": 130,
    "Quest: Built to Last": 131,
    "Quest: Down Below": 132,
    "Quest: The Mining Hub": 133,
    "Quest: The Vault": 134,
    "Quest: Deep Pockets": 135,

    # Supply Quests
    "Supply: Supply The Farmers Tomato": 161,
    "Supply: Supply The Farmers Carrot": 161,
    "Supply: Supply The Farmers Redbeet 1": 161,
    "Supply: Supply The Farmers Redbeet 2": 161,
    "Supply: Supply The Farmers Banana 1": 161,
    "Supply: Supply The Farmers Banana 2": 161,
    "Supply: Supply The Farmers Blueberry": 161,
    "Supply: Supply The Farmers Orange": 161,
    "Supply: Supply The Farmers Broccoli": 161,
    "Supply: Supply The Farmers Pineapple": 161,

    # Side Quests
    "Build: Your First Car": 164,
    "Build: Your Nice Car": 161,
    "Build: Your Work Car": 165,
    "Build: Cardboard Munchies": 162,
    "Build: Just a Bot in a Cage": 163,

    # Farmer Quests
    "Build: A Place to Dump Your Scrap": 161,
    "Build: Any Which Way But Home": 162,
    "Build: Bee Like Me": 163,
    "Build: Cageball Rock": 164,
    "Build: Every Bot Looks Like a Nail": 165,
    "Build: Heart Of Corn": 166,
    "Build: Home is Where the Woc Is": 166,
    "Build: Home is Where You Go to Bed": 166,
    "Build: Make Some Noise": 166,
    "Build: Now the Flowers Will Grow": 166,
    "Build: The Important Meal": 166,
    "Build: The Pop Don't Stop": 166,

    # Scrapper Quests
    "Build: Building Bridges": 161,
    "Build: If You Can't Take the Heat": 162,
    "Build: Itty Bitty Ditty": 163,
    "Build: Onwards and Upwards": 164,
    "Build: Round She Goes": 165,
    "Build: Timber!": 166,

    # Bot Construction
    "Craftbot Construction": 191,
    "Cookbot Construction": 192,
    "Refinebot Construction": 193,
    "Dressbot Construction": 194,
    "Resource Collector Construction": 195,

    # Plant Locations
    "Cotton Seed Unlock": 221,
    "Pigment Flower Seed Unlock": 222,
    "Potato Seed Unlock": 223,
    "Tomato Seed Unlock": 224,
    "Carrot Seed Unlock": 225,
    "Redbeet Seed Unlock": 226,
    "Banana Seed Unlock": 227,
    "Chili Seed Unlock": 228,
    "Blueberry Seed Unlock": 229,
    "Orange Seed Unlock": 230,
    "Broccoli Seed Unlock": 231,
    "Pineapple Seed Unlock": 232,

    # Hostile Bots
    "Green Totebot Kill": 251,
    "Red Totebot Kill": 252,
    "Blue Totebot Kill": 253,
    "Yellow Totebot Kill": 254,
    "Haybot Kill": 255,
    "Blue Tapebot Kill": 256,
    "Red Tapebot Kill": 257,
    "Green Tapebot Kill": 258,
    "Yellow Tapebot Kill": 259,
    "Farmbot Kill": 260,
    "Cablebot Kill": 261,
    "Minerbot Kill": 262,

    # Trader Sanity
    "Trade Farmers 1": 321,
    "Trade Farmers 2": 322,
    "Trade Farmers 3": 323,
    "Trade Farmers 4": 324,
    "Trade Tomatoes 1": 325,
    "Trade Tomatoes 2": 326,
    "Trade Carrots 1": 327,
    "Trade Carrots 2": 328,
    "Trade Redbeets 1": 329,
    "Trade Redbeets 2": 330,
    "Trade Bananas 1": 331,
    "Trade Bananas 2": 332,
    "Trade Blueberries 1": 333,
    "Trade Blueberries 2": 334,
    "Trade Oranges 1": 335,
    "Trade Oranges 2": 336,
    "Trade Broccoli 1": 337,
    "Trade Broccoli 2": 338,
    "Trade Pineapples 1": 339,
    "Trade Pineapples 2": 340,

    # Spud Gun Sanity
    "Scrap Spud Gun Unlock": 321,
    "Spud Gun Unlock": 321,
    "Spud Shotgun Unlock": 321,
    "Spudling Gun Unlock": 321,
    "Fire Launcher Unlock": 321,

    # Garment Sanity
    "Garment Sanity 1": 321,
    "Garment Sanity 2": 321,
    "Garment Sanity 3": 321,
    "Garment Sanity 4": 321,
    "Garment Sanity 5": 321,
    "Garment Sanity 6": 321,
    "Garment Sanity 7": 321,
    "Garment Sanity 8": 321,
    "Garment Sanity 9": 321,
    "Garment Sanity 10": 321,
    "Garment Sanity 11": 321,
    "Garment Sanity 12": 321,
    "Garment Sanity 13": 321,
    "Garment Sanity 14": 321,
    "Garment Sanity 15": 321,
    "Garment Sanity 16": 321,
    "Garment Sanity 17": 321,
    "Garment Sanity 18": 321,
    "Garment Sanity 19": 321,
    "Garment Sanity 20": 321,
    "Garment Sanity 21": 321,
    "Garment Sanity 22": 321,
    "Garment Sanity 23": 321,
    "Garment Sanity 24": 321,
    "Garment Sanity 25": 321,
    "Garment Sanity 26": 321,
    "Garment Sanity 27": 321,
    "Garment Sanity 28": 321,
    "Garment Sanity 29": 321,
    "Garment Sanity 30": 321,

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


    #oldbuildingproblem_locations = get_location_names_with_ids([
    #    "Old Building Problem",
    #])
    #oldbuildingproblem.add_locations(oldbuildingproblem_locations, ScrapMechanicLocation)


    for i in range(1, world.options.GrowlabAmount + 1):
        if i == 1:
            growlab_1 = world.get_region("Growlab 1")
            growlab_1_locations = get_location_names_with_ids(["Growlab Completion 1"])

            growlab_1.add_locations(growlab_1_locations, ScrapMechanicLocation)
            continue

        if i == 7:
            growlab_7 = world.get_region("Growlab 7")
            growlab_7_locations = get_location_names_with_ids(["Growlab Completion 7"])

            growlab_7.add_locations(growlab_7_locations, ScrapMechanicLocation)
            break

        growlab = world.get_region(f"Growlab {i}")
        growlab_locations = get_location_names_with_ids([f"Growlab Completion {i}"])

        growlab.add_locations(growlab_locations, ScrapMechanicLocation)


    # More Work!!!! Add Quest locations from basegame unlock
    if world.options.RandomizePlantUnlocks:
        cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        pigmentflowerplant_locations = get_location_names_with_ids(["Pigment Flower Plant"])
        potatoplant_locations = get_location_names_with_ids(["Potato Plant"])
        tomatoplant_locations = get_location_names_with_ids(["Tomato Plant"])
        carrotplant_locations = get_location_names_with_ids(["Carrot Plant"])
        redbeetplant_locations = get_location_names_with_ids(["Redbeet Plant"])
        bananaplant_locations = get_location_names_with_ids(["Banana Plant"])
        chiliplant_locations = get_location_names_with_ids(["Chili Plant"])
        blueberryplant_locations = get_location_names_with_ids(["Blueberry Plant"])
        orangeplant_locations = get_location_names_with_ids(["Orange Plant"])
        broccoliplant_locations = get_location_names_with_ids(["Broccoli Plant"])
        pineappleplant_locations = get_location_names_with_ids(["Pineapple Plant"])

        basicfarm.add_locations(cottonplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(pigmentflowerplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(potatoplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(tomatoplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(carrotplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(redbeetplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(bananaplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(chiliplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(blueberryplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(orangeplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(broccoliplant_locations, ScrapMechanicLocation)
        basicfarm.add_locations(pineappleplant_locations, ScrapMechanicLocation)


    #if world.options.InitialSchematics:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    #if world.options.SchematicBoxes:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    if world.options.MainQuestSanity:
        quest1 = world.get_region("Main Quest 1")
        quest2 = world.get_region("Main Quest 2")
        quest3 = world.get_region("Main Quest 3")
        quest4 = world.get_region("Main Quest 4")
        quest5 = world.get_region("Main Quest 5")
        quest6 = world.get_region("Main Quest 6")
        quest7 = world.get_region("Main Quest 7")
        quest8 = world.get_region("Main Quest 8")
        quest9 = world.get_region("Main Quest 9")

        ship_locations = get_location_names_with_ids(["Quest: Getting Started"])
        quest1_locations = get_location_names_with_ids(["Quest: The Mechanic Station", "Quest: A Stranger in Need"])
        quest2_locations = get_location_names_with_ids(["Quest: Palette Cleanser"])
        quest3_locations = get_location_names_with_ids(["Quest: A Farmer's Side Hustle", "Quest: Home is Where Your Couch is", "Quest: Lost and Found"])
        quest4_locations = get_location_names_with_ids(["Quest: The Warehouse", "Quest: Wonk-Y business", "Quest: Where's the Fire?"])
        quest5_locations = get_location_names_with_ids(["Quest: Built to Last", ])
        quest6_locations = get_location_names_with_ids(["Quest: Down Below"])
        quest7_locations = get_location_names_with_ids(["Quest: The Mining Hub"])
        quest8_locations = get_location_names_with_ids(["Quest: The Vault"])
        quest9_locations = get_location_names_with_ids(["Quest: Deep Pockets"])

        ship.add_locations(ship_locations, ScrapMechanicLocation)
        quest1.add_locations(quest1_locations, ScrapMechanicLocation)
        quest2.add_locations(quest2_locations, ScrapMechanicLocation)
        quest3.add_locations(quest3_locations, ScrapMechanicLocation)
        quest4.add_locations(quest4_locations, ScrapMechanicLocation)
        quest5.add_locations(quest5_locations, ScrapMechanicLocation)
        quest6.add_locations(quest6_locations, ScrapMechanicLocation)
        quest7.add_locations(quest7_locations, ScrapMechanicLocation)
        quest8.add_locations(quest8_locations, ScrapMechanicLocation)
        quest9.add_locations(quest9_locations, ScrapMechanicLocation)


    #if world.options.SupplyQuestSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    #if world.options.SideQuestSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    #if world.options.FarmerQuestSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    #if world.options.ScrapperQuestSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    if world.options.BuildBotSanity:
        buildbot = world.get_region("Build Bots")
        buildbot_locations = get_location_names_with_ids(["Craftbot Construction","Cookbot Construction","Refinebot Construction","Dressbot Construction","Resource Collector Construction"])
        buildbot.add_locations(buildbot_locations, ScrapMechanicLocation)


    #if world.options.Schembot:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)


    # Redo
    if world.options.BadBotSanity:
        green_totebot_kill = world.get_region("Green Totebot Kill")
        green_totebot_kill_locations = get_location_names_with_ids(["Green Totebot Kill"])
        green_totebot_kill.add_locations(green_totebot_kill_locations, ScrapMechanicLocation)

        red_totebot = world.get_region("Red Totebot Kill")
        red_totebot_kill_locations = get_location_names_with_ids(["Red Totebot Kill"])
        red_totebot.add_locations(red_totebot_kill_locations, ScrapMechanicLocation)

        blue_totebot_kill = world.get_region("Blue Totebot Kill")
        blue_totebot_kill_locations = get_location_names_with_ids(["Blue Totebot Kill"])
        blue_totebot_kill.add_locations(blue_totebot_kill_locations, ScrapMechanicLocation)

        yellow_totebot_kill = world.get_region("Yellow Totebot Kill")
        yellow_totebot_kill_locations = get_location_names_with_ids(["Yellow Totebot Kill"])
        yellow_totebot_kill.add_locations(yellow_totebot_kill_locations, ScrapMechanicLocation)

        haybot_kill = world.get_region("Haybot Kill")
        haybot_kill_locations = get_location_names_with_ids(["Haybot Kill"])
        haybot_kill.add_locations(haybot_kill_locations, ScrapMechanicLocation)

        blue_tapebot_kill = world.get_region("Blue Tapebot Kill")
        blue_tapebot_kill_locations = get_location_names_with_ids(["Blue Tapebot Kill"])
        blue_tapebot_kill.add_locations(blue_tapebot_kill_locations, ScrapMechanicLocation)

        red_tapebot_kill = world.get_region("Red Tapebot Kill")
        red_tapebot_kill_locations = get_location_names_with_ids(["Red Tapebot Kill"])
        red_tapebot_kill.add_locations(red_tapebot_kill_locations, ScrapMechanicLocation)

        green_tapebot_kill = world.get_region("Green Tapebot Kill")
        green_tapebot_kill_locations = get_location_names_with_ids(["Green Tapebot Kill"])
        green_tapebot_kill.add_locations(green_tapebot_kill_locations, ScrapMechanicLocation)

        yellow_tapebot_kill = world.get_region("Yellow Tapebot Kill")
        yellow_tapebot_kill_locations = get_location_names_with_ids(["Yellow Tapebot Kill"])
        yellow_tapebot_kill.add_locations(yellow_tapebot_kill_locations, ScrapMechanicLocation)

        farmbot_kill = world.get_region("Farmbot Kill")
        farmbot_kill_locations = get_location_names_with_ids(["Farmbot Kill"])
        farmbot_kill.add_locations(farmbot_kill_locations, ScrapMechanicLocation)

        cablebot_kill = world.get_region("Cablebot Kill")
        cablebot_kill_locations = get_location_names_with_ids(["Cablebot Kill"])
        cablebot_kill.add_locations(cablebot_kill_locations, ScrapMechanicLocation)

        minerbot_kill = world.get_region("Minerbot Kill")
        minerbot_kill_locations = get_location_names_with_ids(["Minerbot Kill"])
        minerbot_kill.add_locations(minerbot_kill_locations, ScrapMechanicLocation)


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

        tradefarmers_locations = get_location_names_with_ids(["Trade Farmers 1", "Trade Farmers 2", "Trade Farmers 3", "Trade Farmers 4"])
        tradetomatoes_locations = get_location_names_with_ids(["Trade Tomatoes 1", "Trade Tomatoes 2"])
        tradecarrots_locations = get_location_names_with_ids(["Trade Carrots 1", "Trade Carrots 2"])
        traderedbeets_locations = get_location_names_with_ids(["Trade Redbeets 1", "Trade Redbeets 2"])
        tradebananas_locations = get_location_names_with_ids(["Trade Bananas 1", "Trade Bananas 2"])
        tradeblueberries_locations = get_location_names_with_ids(["Trade Blueberries 1", "Trade Blueberries 2"])
        tradeoranges_locations = get_location_names_with_ids(["Trade Oranges 1", "Trade Oranges 2"])
        tradebroccoli_locations = get_location_names_with_ids(["Trade Broccoli 1", "Trade Broccoli 2"])
        tradepineapples_locations = get_location_names_with_ids(["Trade Pineapples 1", "Trade Pineapples 2"])

        tradefarmers.add_locations(tradefarmers_locations, ScrapMechanicLocation)
        tradetomatoes.add_locations(tradetomatoes_locations, ScrapMechanicLocation)
        tradecarrots.add_locations(tradecarrots_locations, ScrapMechanicLocation)
        traderedbeets.add_locations(traderedbeets_locations, ScrapMechanicLocation)
        tradebananas.add_locations(tradebananas_locations, ScrapMechanicLocation)
        tradeblueberries.add_locations(tradeblueberries_locations, ScrapMechanicLocation)
        tradeoranges.add_locations(tradeoranges_locations, ScrapMechanicLocation)
        tradebroccoli.add_locations(tradebroccoli_locations, ScrapMechanicLocation)
        tradepineapples.add_locations(tradepineapples_locations, ScrapMechanicLocation)

# More Work!!!
    if world.options.GarmentSanity:
        dressbot = world.get_region("Dressbot")
        dressbot_locations = get_location_names_with_ids(["Cotton Plant"])
        dressbot.add_locations(dressbot_locations, ScrapMechanicLocation)


    #if world.options.SpudGunSanity:
        #cottonplant = world.get_region("Cotton Plant")
        #cottonplant_locations = get_location_names_with_ids(["Cotton Plant"])
        #cottonplant.add_locations(cottonplant_locations, ScrapMechanicLocation)








