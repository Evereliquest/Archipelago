import asyncio
import subprocess
import os
import json
import time
import xml.etree.ElementTree as ET
from Utils import gui_enabled, open_filename, user_path
from CommonClient import CommonContext, get_base_parser, server_loop
from NetUtils import ClientStatus
from typing import Any
import typing
import re
import traceback


SETTINGS_PATH = user_path("teardownsettings.json")
Missionindex = {
        "mall_intro": 0,
        "lee_computers": 1,
        "lee_login": 2,
        "marina_demolish": 3,
        "marina_cars": 4,
        "mansion_pool": 5,
        "lee_safe": 6,
        "marina_gps": 7,
        "lee_tower": 8,
        "mansion_art": 9,
        "marina_tools": 10,
        "marina_art_back": 11,
        "mall_foodcourt": 12,
        "mansion_fraud": 13,
        "caveisland_computers": 14,
        "mansion_race": 15,
        "mansion_safe": 16,
        "lee_powerplant": 17,
        "caveisland_propane": 18,
        "caveisland_dishes": 19,
        "lee_flooding": 20,
        "frustrum_chase": 21,
        "factory_espionage": 22,
        "caveisland_ingredients": 23,
        "frustrum_tornado": 24,
        "mall_shipping": 25,
        "carib_alarm": 26,
        "carib_barrels": 27,
        "carib_destroy": 28,
        "carib_yacht": 29,
        "frustrum_vehicle": 30,
        "mall_decorations": 31,
        "factory_tools": 32,
        "mall_radiolink": 33,
        "frustrum_pawnshop": 34,
        "factory_robot": 35,
        "lee_woonderland": 36,
        "factory_explosive": 37,
        "caveisland_roboclear": 38,
        "cullington_bomb": 39,
}

Missionmap = {
    1: "message/mall_intro",
    2: "message/lee_computers",
    3: "message/lee_login",
    4: "message/marina_demolish",
    5: "message/marina_cars",
    6: "message/marina_gps",
    7: "message/mansion_pool",
    8: "message/lee_safe",
    9: "message/lee_tower",
    10: "message/mansion_art",
    11: "message/marina_tools",
    12: "message/marina_art_back",
    13: "message/mall_foodcourt",
    14: "message/mansion_fraud",
    15: "message/caveisland_computers",
    16: "message/mansion_race",
    17: "message/mansion_safe",
    18: "message/lee_powerplant",
    19: "message/caveisland_propane",
    20: "message/caveisland_dishes",
    21: "message/lee_flooding",
    22: "message/frustrum_chase",
    23: "message/factory_espionage",
    24: "message/caveisland_ingredients",
    25: "message/frustrum_tornado",
    26: "message/mall_shipping",
    27: "message/carib_alarm",
    28: "message/carib_barrels",
    29: "message/carib_destroy",
    30: "message/carib_yacht",
    31: "message/frustrum_vehicle",
    32: "message/mall_decorations",
    33: "message/factory_tools",
    34: "message/mall_radiolink",
    35: "message/frustrum_pawnshop",
    36: "message/factory_robot",
    37: "message/lee_woonderland",
    38: "message/factory_explosive",
    39: "message/caveisland_roboclear",
    40: "message/cullington_bomb",
}

Toolmap = {
    41: "tool/sledge/enabled",
    42: "tool/spraycan/enabled",
    43: "tool/extinguisher/enabled",
    51: "tool/blowtorch/enabled",
    52: "tool/shotgun/enabled",
    53: "tool/plank/enabled",
    54: "tool/pipebomb/enabled",
    55: "tool/gun/enabled",
    56: "tool/bomb/enabled",
    57: "tool/rocket/enabled",
    58: "tool/booster/enabled",
    59: "tool/leafblower/enabled",
    60: "tool/wire/enabled",
    61: "tool/turbo/enabled",
    62: "tool/explosive/enabled",
    63: "tool/rifle/enabled",
    64: "tool/steroid/enabled",
}

Upgrademap = {
    71: ["tool/blowtorch/ammo", 10, 20],
    81: ["tool/shotgun/ammo", 12, 12],
    82: ["tool/shotgun/range", 20, 20],
    83: ["tool/shotgun/damage", 1, 3],
    91: ["tool/plank/ammo", 8, 8],
    92: ["tool/plank/width", 1, 3],
    93: ["tool/plank/length", 8, 36],
    101: ["tool/pipebomb/ammo", 6, 6],
    102: ["tool/pipebomb/damage", 1, 2],
    111: ["tool/gun/ammo", 6, 6],
    112: ["tool/gun/range", 20, 40],
    113: ["tool/gun/damage", 1, 1],
    121: ["tool/bomb/ammo", 6, 6],
    122: ["tool/bomb/damage", 1, 4],
    131: ["tool/rocket/ammo", 6, 6],
    132: ["tool/rocket/damage", 1, 3],
    141: ["tool/booster/ammo", 6, 6],
    142: ["tool/booster/power", 100, 200],
    143: ["tool/booster/time", 2, 4],
    151: ["tool/leafblower/power", 10, 20],
    161: ["tool/wire/ammo", 6, 6],
    162: ["tool/wire/stretch", 1, 3],
    171: ["tool/turbo/ammo", 6, 6],
    172: ["tool/turbo/power", 100, 200],
    181: ["tool/explosive/ammo", 4, 4],
    182: ["tool/explosive/damage", 1, 5],
    191: ["tool/rifle/ammo", 6, 6],
    201: ["tool/steroid/ammo", 1, 2],
    202: ["tool/steroid/time", 1, 4],

}

Cashmap = {
    251: 20,
    252: 50,
    253: 100,
    254: 250,
    255: 500,
    256: 750,
    257: 1000,
    258: 3000
}

Mission_upgrade_send_map = {
    "mall_intro": 1,
    "lee_computers": 11,
    "lee_login": 21,
    "marina_demolish": 31,
    "marina_cars": 41,
    "mansion_pool": 61,
    "lee_safe": 71,
    "marina_gps": 51,
    "lee_tower": 81,
    "mansion_art": 91,
    "marina_tools": 101,
    "marina_art_back": 111,
    "mall_foodcourt": 121,
    "mansion_fraud": 131,
    "caveisland_computers": 141,
    "mansion_race": 151,
    "mansion_safe": 161,
    "lee_powerplant": 171,
    "caveisland_propane": 181,
    "caveisland_dishes": 191,
    "lee_flooding": 201,
    "frustrum_chase": 211,
    "factory_espionage": 221,
    "caveisland_ingredients": 231,
    "frustrum_tornado": 241,
    "mall_shipping": 251,
    "carib_alarm": 261,
    "carib_barrels": 271,
    "carib_destroy": 281,
    "carib_yacht": 291,
    "frustrum_vehicle": 301,
    "mall_decorations": 311,
    "factory_tools": 321,
    "mall_radiolink": 331,
    "frustrum_pawnshop": 341,
    "factory_robot": 351,
    "lee_woonderland": 361,
    "factory_explosive": 371,
    "caveisland_roboclear": 381,
    "cullington_bomb": 393,
}

Tool_upgrade_send_map = {
    "toolupgrade/blowtorch/ammo": {
        30: 501,
        40: 502,
        50: 503,
        60: 504,
    },
    "toolupgrade/shotgun/ammo": {
        24: 511,
        36: 512,
        48: 513,
        60: 514,
        72: 515,
        84: 516,
        96: 517,
    },
    "toolupgrade/shotgun/range": {
        40: 521,
        60: 521,
    },
    "toolupgrade/shotgun/damage": {
        4: 531,
        5: 532,
    },
    "toolupgrade/plank/ammo": {
        16: 541,
        24: 542,
        32: 543,
        40: 544,
        48: 545,
        56: 546,
        64: 547,
    },
    "toolupgrade/plank/width": {
        4: 551,
        5: 552,
    },
    "toolupgrade/plank/length": {
        48: 561,
        56: 562,
        64: 563,
    },
    "toolupgrade/pipebomb/ammo": {
        12: 571,
        18: 572,
        25: 573,
        30: 574,
        36: 575,
    },
    "toolupgrade/pipebomb/damage": {
        3: 581,
        4: 582,
    },
    "toolupgrade/gun/ammo": {
        12: 591,
        18: 592,
        24: 593,
        30: 594,
        36: 595,
    },
    "toolupgrade/gun/range": {
        60: 601,
        80: 602,
        100: 603,
    },
    "toolupgrade/gun/damage": {
        2: 611,
        3: 612,
    },
    "toolupgrade/bomb/ammo": {
        12: 621,
        18: 622,
        24: 623,
        30: 624,
        36: 625,
    },
    "toolupgrade/bomb/damage": {
        5: 631,
        6: 632,
    },
    "toolupgrade/rocket/ammo": {
        12: 641,
        18: 642,
        24: 643,
    },
    "toolupgrade/rocket/damage": {
        4: 651,
        5: 652,
    },
    "toolupgrade/booster/ammo": {
        12: 661,
        18: 662,
        24: 663,
    },
    "toolupgrade/booster/power": {
        300: 671,
        400: 672,
    },
    "toolupgrade/booster/time": {
        6: 681,
        8: 682,
    },
    "toolupgrade/leafblower/power": {
        30: 691,
        40: 692,
        50: 693,
    },
    "toolupgrade/wire/ammo": {
        12: 701,
        18: 702,
        24: 703,
    },
    "toolupgrade/wire/stretch": {
        4: 711,
        5: 712,
    },
    "toolupgrade/turbo/ammo": {
        12: 721,
        18: 722,
        36: 723,
    },
    "toolupgrade/turbo/power": {
        300: 731,
        400: 732,
    },
    "toolupgrade/explosive/ammo": {
        8: 741,
        12: 742,
        16: 743,
    },
    "toolupgrade/explosive/damage": {
        6: 751,
        7: 752,
        8: 753,
    },
    "toolupgrade/rifle/ammo": {
        12: 761,
        18: 762,
    },
    "toolupgrade/steroid/ammo": {
        3: 771,
        4: 772,
    },
    "toolupgrade/steroid/time": {
        5: 781,
        6: 782,
    },

}

Valuable_First_ID = 800

valuable_items_list = [
    "hub_banana",

    "lee_trowel",
    "lee_pneumaticwrench",
    "lee_cash6",
    "lee_college",
    "lee_bits",
    "lee_tilecutter",
    "lee_disccutter",
    "lee_wrench",
    "lee_cutters",
    "lee_cash1",
    "lee_cash4",
    "lee_cash3",
    "lee_painting1",
    "lee_painting2",
    "lee_cash2",
    "lee_pension",
    "lee_painting4",
    "lee_whisky",
    "lee_circularsaw",
    "lee_screwdriver",
    "lee_bottles",
    "lee_microscope",
    "lee_cash5",
    "lee_laser2",
    "lee_wallet",
    "lee_comics",
    "lee_laser1",
    "lee_stair_toolbox",
    "lee_hammer",

    "marina_cigarbox",
    "marina_silvercoins",
    "marina_cashbag",
    "marina_sander",
    "marina_amethyst",
    "marina_callibration",
    "marina_lubrication",
    "marina_sonar",
    "marina_sparkplugs",
    "marina_propeller",
    "marina_drill",
    "marina_telescope",
    "marina_gamingconsole",
    "marina_sunglasses",
    "marina_cashregister",
    "marina_swordfish",
    "marina_hook",
    "marina_vacuum",
    "marina_sword",
    "marina_dagger",
    "marina_modelship",
    "marina_fishing",
    "marina_mp3",
    "marina_binoculars",
    "marina_compass",
    "marina_cannonball",
    "marina_cashbox",
    "marina_trophy",
    "marina_gun",
    "marina_painting1",
    "marina_flashlight",
    "marina_walkietalkie",
    "marina_sextant",
    "marina_tequila",
    "marina_lifevest",
    "marina_steeringwheel",

    "mansion_wallet1",
    "liquor1",
    "mansion_passport",
    "mansion_soup",
    "mansion_walkman",
    "vacuumcleaner",
    "mansion_gift",
    "mansion_knives",
    "mansion_caviar",
    "mansion_pan",
    "mansion_elevatormanual",
    "mansion_cash",
    "mansion_coincollection",
    "mansion_bronzestatue",
    "mansion_remote",
    "mansion_cablebox",
    "mansion_dictaphone",
    "mansion_snookerbook",
    "mansion_popcornmanual",
    "mansion_moviebook",
    "mansion_wallet3",
    "mansion_sneakers",
    "mansion_tshirt",
    "mansion_lighter2",
    "mansion_creditcard",
    "mansion_gardeningbook",
    "mansion_makeup",
    "mansion_pills",
    "mansion_wallet2",
    "mansion_silverware",
    "mansion_oysters",
    "mansion_foodprocessor",
    "guesthouse_lamp",
    "mansion_jewelry",
    "mansion_charcoal",
    "mansion_trophy",
    "mansion_lighter",
    "mansion_chocolate",
    "mansion_wine",
    "mansion_toiletbrush",
    "mansion_thermometer",
    "mansion_calibration",
    "mansion_carburetor",
    "mansion_drill",
    "mansion_model_train",
    "fraud_toolbox",
    "mansion_polishtrophy",

    "caveisland_phone",
    "caveisland_disccutter",
    "caveisland_drill",
    "caveisland_detergent",
    "caveisland_nutrition",
    "caveisland_yeast",
    "caveisland_pesticide",
    "caveisland_oldtv",
    "caveisland_crock-of-gold",
    "caveisland_carbon_lamp",
    "caveisland_tar",
    "caveisland_fishinggear",
    "caveisland_fishingscale",
    "caveisland_radio",
    "caveisland_labeling",
    "caveisland_fishingknife",
    "caveisland_cashregister1",
    "caveisland_btextra",
    "caveisland_pulsewatch",
    "caveisland_cashregister2",
    "caveisland_gin",
    "caveisland_monitor",
    "caveisland_book",
    "caveisland_alarmclock1",
    "caveisland_tv1",
    "caveisland_wallet1",
    "caveisland_chess",
    "caveisland_vacuum",
    "caveisland_projector",
    "caveisland_binoculars",
    "caveisland_gardenscissors",
    "caveisland_ragswater",
    "caveisland_drilltape",
    "caveisland_wine",
    "caveisland_airpurifier",
    "caveisland_pills",
    "caveisland_vaultgold",
    "caveisland_vaultcash",

    "mall_durablephone",
    "mall_taco",
    "mall_busybooks",
    "mall_flashlight",
    "mall_trufflejuice",
    "mall_bluetidecashbox",
    "mall_furcoat",
    "mall_democash",
    "mall_safecracking",
    "mall_pinkspray",
    "mall_wallet1",
    "mall_hoodie",
    "mall_goldwatch",
    "mall_necklace",
    "mall_tiepin",
    "mall_stapler",
    "mall_skateboard",
    "mall_civet",
    "mall_cash1",
    "mall_vram",
    "mall_vodka",
    "mall_gardenscissors",
    "mall_underwear",
    "mall_fxpedal",
    "mall_radio",
    "mall_vinegar",
    "mall_eaudetoilette",

    "frustrum_oilpaint",
    "frustrum_itbonus",
    "frustrum_oil",
    "frustrum_wallet1",
    "frustrum_reciprocating",
    "frustrum_lp",
    "frustrum_shaver",
    "frustrum_fredaward",
    "frustrum_tribalmask",
    "frustrum_darts",
    "frustrum_smokemachine",
    "frustrum_wallet3",
    "frustrum_dehumidifier",
    "frustrum_bones",
    "frustrum_fabricsoftener",
    "frustrum_wallet2",
    "frustrum_spices",
    "frustrum_lotion",
    "frustrum_filter",
    "frustrum_ring",
    "frustrum_lure",
    "frustrum_wallet4",
    "frustrum_hat",
    "frustrum_guitar",
    "frustrum_preasuremeter",
    "frustrum_bits",
    "frustrum_harmonica",

    "factory_bulletproof",
    "factory_microphone",
    "factory_aicore",
    "factory_gyroscope",
    "factory_gearmotor",
    "factory_radio",
    "factory_oldoutboardmotor",
    "factory_infraredtransmitter",
    "factory_semiconductors",
    "factory_campingguide",
    "factory_climbinghat",
    "factory_roses",
    "factory_umbrella",
    "factory_key",
    "factory_cigars",
    "factory_gillianbribe",
    "factory_distancesensor",
    "factory_cards",
    "factory_waterproof",
    "factory_roboteye",
    "factory_survivalbook",
    "factory_lightsensor",
    "factory_servo",
    "factory_ultrasonicsensor",
    "factory_infraredsensor",
    "factory_scubagear",
    "factory_watersensor",
    "factory_fishingrod",
    "factory_helicoptermanual",
    "factory_explosionproof",

    "carib_snorkel",
    "carib_volleyball",
    "carib_exoticfruit",
    "carib_rims",
    "carib_knuckles",
    "carib_wallet",
    "carib_monkeyhand",
    "carib_moneycounter",
    "carib_diamondcane",
    "carib_islandlife",
    "carib_teapot",
    "carib_grease",
    "carib_copperwire",
    "carib_jetskiengine",
    "carib_grappa",
    "carib_oldmagazines",
    "carib_skate",
    "carib_lastroll",
    "carib_chainsaw",
    "carib_carburetor",
    "carib_pegleg",
    "carib_supercharger",
    "carib_messageinabottle",
    "carib_scale",
    "carib_tuningkit",
    "carib_tropicalhelmet",
    "carib_goldenbullets",
    "carib_scubatank",
    "carib_birdegg",
    "carib_shell",
    "carib_goldengrillz",
    "carib_pineapple",
    "carib_duck",
    "carib_bayran",

]

Valuable_send_map = {
    name: Valuable_First_ID + index
    for index, name in enumerate(valuable_items_list)
}

SAVE_TEMPLATE = {
    "toolupgrade": {

        "blowtorch/enabled": "0",
        "blowtorch/ammo": "20",

        "shotgun/enabled": "0",
        "shotgun/ammo": "12",
        "shotgun/range": "20",
        "shotgun/damage": "3",

        "plank/enabled": "0",
        "plank/ammo": "8",
        "plank/width": "3",
        "plank/length": "36",

        "pipebomb/enabled": "0",
        "pipebomb/ammo": "6",
        "pipebomb/damage": "2",

        "gun/enabled": "0",
        "gun/ammo": "6",
        "gun/range": "40",
        "gun/damage": "1",

        "bomb/enabled": "0",
        "bomb/ammo": "6",
        "bomb/damage": "4",

        "rocket/enabled": "0",
        "rocket/ammo": "6",
        "rocket/damage": "3",

        "booster/enabled": "0",
        "booster/ammo": "6",
        "booster/power": "200",
        "booster/time": "4",

        "leafblower/enabled": "0",
        "leafblower/power": "20",

        "wire/enabled": "0",
        "wire/ammo": "6",
        "wire/stretch": "3",

        "turbo/enabled": "0",
        "turbo/ammo": "6",
        "turbo/power": "200",

        "explosive/enabled": "0",
        "explosive/ammo": "4",
        "explosive/damage": "5",

        "rifle/enabled": "0",
        "rifle/ammo": "6",

        "steroid/enabled": "0",
        "steroid/ammo": "2",
        "steroid/time": "4",

    },

    "tool": {
        "sledge/enabled": "0",

        "spraycan/enabled": "0",

        "extinguisher/enabled": "0",

        "blowtorch/enabled": "0",
        "blowtorch/ammo": "20",

        "shotgun/enabled": "0",
        "shotgun/ammo": "12",
        "shotgun/range": "20",
        "shotgun/damage": "3",

        "plank/enabled": "0",
        "plank/ammo": "8",
        "plank/width": "3",
        "plank/length": "36",

        "pipebomb/enabled": "0",
        "pipebomb/ammo": "6",
        "pipebomb/damage": "2",

        "gun/enabled": "0",
        "gun/ammo": "6",
        "gun/range": "40",
        "gun/damage": "1",

        "bomb/enabled": "0",
        "bomb/ammo": "6",
        "bomb/damage": "4",

        "rocket/enabled": "0",
        "rocket/ammo": "6",
        "rocket/damage": "3",

        "booster/enabled": "0",
        "booster/ammo": "6",
        "booster/power": "200",
        "booster/time": "4",

        "leafblower/enabled": "0",
        "leafblower/power": "20",

        "wire/enabled": "0",
        "wire/ammo": "6",
        "wire/stretch": "3",

        "turbo/enabled": "0",
        "turbo/ammo": "6",
        "turbo/power": "200",

        "explosive/enabled": "0",
        "explosive/ammo": "4",
        "explosive/damage": "5",

        "rifle/enabled": "0",
        "rifle/ammo": "6",

        "steroid/enabled": "0",
        "steroid/ammo": "2",
        "steroid/time": "4",

    },

    "message": {
        "boss_intro": "0",
        "mall_intro": "0",
        "boss_busted": "0",
        "lee_computers": "0",
        "lee_login": "0",
        "boss_coffee": "0",
        "marina_demolish": "0",
        "marina_cars": "0",
        "lockelle_parade_ad": "0",
        "marina_gps": "0",
        "mansion_pool": "0",
        "lee_safe": "0",
        "lee_safe_done": "0",
        "lee_tower": "0",
        "boss_encourage_1": "0",
        "mansion_art": "0",
        "marina_tools": "0",
        "marina_art_back": "0",
        "mall_foodcourt": "0",
        "marina_art_back_done": "0",
        "mansion_fraud": "0",
        "caveisland_computers": "0",
        "mansion_race": "0",
        "mansion_safe": "0",
        "lee_powerplant": "0",
        "lee_powerplant_done": "0",
        "boss_encourage_2": "0",
        "caveisland_propane": "0",
        "caveisland_dishes": "0",
        "lee_flooding": "0",
        "frustrum_chase": "0",
        "boss_part2": "0",
        "factory_espionage": "0",
        "factory_espionage_done": "0",
        "caveisland_ingredients": "0",
        "frustrum_tornado": "0",
        "mall_shipping": "0",
        "mall_shipping_done": "0",
        "carib_travel": "0",
        "carib_alarm": "0",
        "boss_vacation": "0",
        "carib_barrels": "0",
        "carib_destroy": "0",
        "carib_yacht": "0",
        "carib_last": "0",
        "frustrum_vehicle": "0",
        "mall_decorations": "0",
        "factory_tools": "0",
        "mall_radiolink": "0",
        "frustrum_pawnshop": "0",
        "factory_robot": "0",
        "lee_woonderland": "0",
        "factory_explosive": "0",
        "tracy_dinner": "0",
        "factory_explosive_done": "0",
        "caveisland_roboclear": "0",
        "caveisland_roboclear_done1": "0",
        "caveisland_roboclear_done2": "0",
        "cullington_bomb": "0",

    },

    "mission": {
        "mall_intro": "0",
        "mall_intro/score": "0",
        "lee_computers": "0",
        "lee_computers/score": "0",
        "lee_login": "0",
        "lee_login/score": "0",
        "marina_demolish": "0",
        "marina_demolish/score": "0",
        "marina_cars": "0",
        "marina_cars/score": "0",
        "mansion_pool": "0",
        "mansion_pool/score": "0",
        "lee_safe": "0",
        "lee_safe/score": "0",
        "marina_gps": "0",
        "marina_gps/score": "0",
        "lee_tower": "0",
        "lee_tower/score": "0",
        "mansion_art": "0",
        "mansion_art/score": "0",
        "marina_tools": "0",
        "marina_tools/score": "0",
        "marina_art_back": "0",
        "marina_art_back/score": "0",
        "mall_foodcourt": "0",
        "mall_foodcourt/score": "0",
        "mansion_fraud": "0",
        "mansion_fraud/score": "0",
        "caveisland_computers": "0",
        "caveisland_computers/score": "0",
        "mansion_race": "0",
        "mansion_race/score": "0",
        "mansion_safe": "0",
        "mansion_safe/score": "0",
        "lee_powerplant": "0",
        "lee_powerplant/score": "0",
        "caveisland_propane": "0",
        "caveisland_propane/score": "0",
        "caveisland_dishes": "0",
        "caveisland_dishes/score": "0",
        "lee_flooding": "0",
        "lee_flooding/score": "0",
        "frustrum_chase": "0",
        "frustrum_chase/score": "0",
        "factory_espionage": "0",
        "factory_espionage/score": "0",
        "caveisland_ingredients": "0",
        "caveisland_ingredients/score": "0",
        "frustrum_tornado": "0",
        "frustrum_tornado/score": "0",
        "mall_shipping": "0",
        "mall_shipping/score": "0",
        "carib_alarm": "0",
        "carib_alarm/score": "0",
        "carib_barrels": "0",
        "carib_barrels/score": "0",
        "carib_destroy": "0",
        "carib_destroy/score": "0",
        "carib_yacht": "0",
        "carib_yacht/score": "0",
        "frustrum_vehicle": "0",
        "frustrum_vehicle/score": "0",
        "mall_decorations": "0",
        "mall_decorations/score": "0",
        "factory_tools": "0",
        "factory_tools/score": "0",
        "mall_radiolink": "0",
        "mall_radiolink/score": "0",
        "frustrum_pawnshop": "0",
        "frustrum_pawnshop/score": "0",
        "factory_robot": "0",
        "factory_robot/score": "0",
        "lee_woonderland": "0",
        "lee_woonderland/score": "0",
        "factory_explosive": "0",
        "factory_explosive/score": "0",
        "caveisland_roboclear": "0",
        "caveisland_roboclear/score": "0",
        "cullington_bomb": "0",
        "cullington_bomb/score": "0",

    },
    "valuable": {
        "hub_banana": "0",
        "lee_cash6": "0",
        "lee_college": "0",
        "lee_cash2": "0",
        "lee_painting4": "0",
        "lee_wrench": "0",
        "marina_drill": "0",
        "marina_dagger": "0",
        "mall_durablephone": "0",
        "mall_taco": "0",
        "mall_busybooks": "0",
        "mall_flashlight": "0",
        "mall_radio": "0",
        "mall_vinegar": "0",
        "mall_eaudetoilette": "0",
        "mall_vram": "0",
        "mall_fxpedal": "0",
        "mall_underwear": "0",
        "mall_gardenscissors": "0",
        "mall_hoodie": "0",
        "mall_democash": "0",
        "mall_goldwatch": "0",
        "mall_wallet1": "0",
        "mall_tiepin": "0",
        "mall_trufflejuice": "0",
        "mall_civet": "0",
        "mall_bluetidecashbox": "0",
        "mall_cash1": "0",
        "mall_skateboard": "0",
        "mall_stapler": "0",
        "mall_vodka": "0",
        "mall_furcoat": "0",
        "mall_safecracking": "0",
        "mall_necklace": "0",
        "mall_pinkspray": "0",
        "mansion_wallet1": "0",
        "liquor1": "0",
        "mansion_calibration": "0",
        "mansion_drill": "0",
        "mansion_carburetor": "0",
        "mansion_wine": "0",
        "mansion_lighter": "0",
        "mansion_toiletbrush": "0",
        "mansion_chocolate": "0",
        "mansion_thermometer": "0",
        "mansion_trophy": "0",
        "mansion_charcoal": "0",
        "mansion_jewelry": "0",
        "guesthouse_lamp": "0",
        "mansion_foodprocessor": "0",
        "mansion_oysters": "0",
        "mansion_silverware": "0",
        "mansion_model_train": "0",
        "mansion_lighter2": "0",
        "mansion_creditcard": "0",
        "mansion_tshirt": "0",
        "mansion_sneakers": "0",
        "mansion_snookerbook": "0",
        "mansion_wallet3": "0",
        "mansion_moviebook": "0",
        "mansion_popcornmanual": "0",
        "mansion_gardeningbook": "0",
        "mansion_caviar": "0",
        "mansion_pan": "0",
        "mansion_knives": "0",
        "mansion_elevatormanual": "0",
        "mansion_bronzestatue": "0",
        "mansion_coincollection": "0",
        "mansion_cablebox": "0",
        "mansion_remote": "0",
        "mansion_gift": "0",
        "mansion_dictaphone": "0",
        "mansion_makeup": "0",
        "mansion_pills": "0",
        "mansion_wallet2": "0",
        "mansion_passport": "0",
        "vacuumcleaner": "0",
        "mansion_walkman": "0",
        "mansion_soup": "0",
        "mansion_cash": "0",
        "mansion_polishtrophy": "0",
        "fraud_toolbox": "0",
        "factory_radio": "0",
        "factory_gearmotor": "0",
        "factory_lightsensor": "0",
        "factory_survivalbook": "0",
        "factory_watersensor": "0",
        "factory_scubagear": "0",
        "factory_infraredtransmitter": "0",
        "factory_semiconductors": "0",
        "factory_climbinghat": "0",
        "factory_campingguide": "0",
        "factory_oldoutboardmotor": "0",
        "factory_cigars": "0",
        "factory_gillianbribe": "0",
        "factory_distancesensor": "0",
        "factory_infraredsensor": "0",
        "factory_servo": "0",
        "factory_ultrasonicsensor": "0",
        "factory_cards": "0",
        "factory_roses": "0",
        "factory_umbrella": "0",
        "factory_key": "0",
        "factory_waterproof": "0",
        "factory_roboteye": "0",
        "factory_fishingrod": "0",
        "factory_gyroscope": "0",
        "factory_aicore": "0",
        "factory_bulletproof": "0",
        "factory_microphone": "0",
        "factory_explosionproof": "0",
        "factory_helicoptermanual": "0",
        "marina_lifevest": "0",
        "marina_tequila": "0",
        "marina_trophy": "0",
        "marina_cannonball": "0",
        "marina_cashbox": "0",
        "marina_gun": "0",
        "marina_flashlight": "0",
        "marina_walkietalkie": "0",
        "marina_sextant": "0",
        "marina_binoculars": "0",
        "marina_compass": "0",
        "marina_mp3": "0",
        "marina_modelship": "0",
        "marina_swordfish": "0",
        "marina_vacuum": "0",
        "marina_hook": "0",
        "marina_sword": "0",
        "marina_sander": "0",
        "marina_cashbag": "0",
        "marina_cigarbox": "0",
        "marina_silvercoins": "0",
        "marina_lubrication": "0",
        "marina_callibration": "0",
        "marina_amethyst": "0",
        "marina_telescope": "0",
        "marina_propeller": "0",
        "marina_sparkplugs": "0",
        "marina_sonar": "0",
        "marina_gamingconsole": "0",
        "marina_fishing": "0",
        "marina_sunglasses": "0",
        "marina_cashregister": "0",
        "marina_painting1": "0",
        "marina_steeringwheel": "0",
        "caveisland_binoculars": "0",
        "caveisland_projector": "0",
        "caveisland_gardenscissors": "0",
        "caveisland_drilltape": "0",
        "caveisland_vacuum": "0",
        "caveisland_vaultgold": "0",
        "caveisland_vaultcash": "0",
        "caveisland_disccutter": "0",
        "caveisland_drill": "0",
        "caveisland_detergent": "0",
        "caveisland_carbon_lamp": "0",
        "caveisland_fishingscale": "0",
        "caveisland_radio": "0",
        "caveisland_labeling": "0",
        "caveisland_fishingknife": "0",
        "caveisland_btextra": "0",
        "caveisland_pulsewatch": "0",
        "caveisland_cashregister1": "0",
        "caveisland_ragswater": "0",
        "caveisland_wine": "0",
        "caveisland_alarmclock1": "0",
        "caveisland_book": "0",
        "caveisland_cashregister2": "0",
        "caveisland_monitor": "0",
        "caveisland_gin": "0",
        "caveisland_tv1": "0",
        "caveisland_fishinggear": "0",
        "caveisland_phone": "0",
        "caveisland_chess": "0",
        "caveisland_wallet1": "0",
        "caveisland_tar": "0",
        "caveisland_yeast": "0",
        "caveisland_nutrition": "0",
        "caveisland_pesticide": "0",
        "caveisland_oldtv": "0",
        "caveisland_crock-of-gold": "0",
        "caveisland_airpurifier": "0",
        "caveisland_pills": "0",
        "frustrum_itbonus": "0",
        "frustrum_oil": "0",
        "frustrum_fabricsoftener": "0",
        "frustrum_wallet2": "0",
        "frustrum_spices": "0",
        "frustrum_preasuremeter": "0",
        "frustrum_bits": "0",
        "frustrum_guitar": "0",
        "frustrum_hat": "0",
        "frustrum_ring": "0",
        "frustrum_wallet4": "0",
        "frustrum_filter": "0",
        "frustrum_lure": "0",
        "frustrum_harmonica": "0",
        "frustrum_oilpaint": "0",
        "frustrum_reciprocating": "0",
        "frustrum_lp": "0",
        "frustrum_wallet1": "0",
        "frustrum_fredaward": "0",
        "frustrum_shaver": "0",
        "frustrum_smokemachine": "0",
        "frustrum_darts": "0",
        "frustrum_wallet3": "0",
        "frustrum_lotion": "0",
        "frustrum_tribalmask": "0",
        "frustrum_bones": "0",
        "frustrum_dehumidifier": "0",
        "lee_tilecutter": "0",
        "lee_bits": "0",
        "lee_comics": "0",
        "lee_wallet": "0",
        "lee_laser1": "0",
        "lee_laser2": "0",
        "lee_cash5": "0",
        "lee_microscope": "0",
        "lee_bottles": "0",
        "lee_screwdriver": "0",
        "lee_stair_toolbox": "0",
        "lee_circularsaw": "0",
        "lee_whisky": "0",
        "lee_pension": "0",
        "lee_trowel": "0",
        "lee_cash4": "0",
        "lee_cash1": "0",
        "lee_cutters": "0",
        "lee_disccutter": "0",
        "lee_pneumaticwrench": "0",
        "lee_cash3": "0",
        "lee_painting1": "0",
        "lee_painting2": "0",
        "lee_hammer": "0",
        "carib_snorkel": "0",
        "carib_pineapple": "0",
        "carib_birdegg": "0",
        "carib_supercharger": "0",
        "carib_goldenbullets": "0",
        "carib_messageinabottle": "0",
        "carib_carburetor": "0",
        "carib_shell": "0",
        "carib_duck": "0",
        "carib_diamondcane": "0",
        "carib_moneycounter": "0",
        "carib_monkeyhand": "0",
        "carib_wallet": "0",
        "carib_rims": "0",
        "carib_volleyball": "0",
        "carib_knuckles": "0",
        "carib_islandlife": "0",
        "carib_teapot": "0",
        "carib_copperwire": "0",
        "carib_bayran": "0",
        "carib_exoticfruit": "0",
        "carib_goldengrillz": "0",
        "carib_tropicalhelmet": "0",
        "carib_scale": "0",
        "carib_chainsaw": "0",
        "carib_lastroll": "0",
        "carib_grappa": "0",
        "carib_oldmagazines": "0",
        "carib_jetskiengine": "0",
        "carib_grease": "0",
        "carib_skate": "0",
        "carib_pegleg": "0",
        "carib_tuningkit": "0",
        "carib_scubatank": "0",
    }

}



class TeardownContext(CommonContext):
    game = "Teardown"
    tags = CommonContext.tags | {"AP"}
    items_handling = 0b111
    want_slot_data = True
    slot_data: dict[str, Any]
    last_connected_slot: int | None = None
    stored_data: dict[str, typing.Any]
    stored_data_notification_keys: set[str]
    items_received: int = 0




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_known_item_count = None
        self.last_mtime = None
        self.game_exe_path = ""
        self.savegame_path = ""
        self.player_data = None
        self.first_sync_done = False
        self.loadsettings()
        self.MissionAmount = 0
        self.mission_count = 0
        self.finished_game = False
        self.location_name_to_id = ""
        self.items_received_event = asyncio.Event()
        self.auth_event = asyncio.Event()
        self.locations_checked = []
        self.applied_cash_counts = {}
        self.last_cash = None
        self.last_received_count = None

    def loadsettings(self):
        # Load our settings from our json file
        if os.path.exists(SETTINGS_PATH):
            with open(SETTINGS_PATH, "r") as f:
                data = json.load(f)
                self.game_exe_path = data.get("game_exe_path", "")
                self.savegame_path = data.get("savegame_path", "")


    def checkgamepath(self):
        # Ask for exe if not found
        if not self.game_exe_path or not os.path.exists(self.game_exe_path):
            if gui_enabled:
                new_path = open_filename(
                    "Select Teardown Executable",
                    (("Teardown Executable", ".exe"), ("All Files", "*"))
                )
                if new_path:
                    self.game_exe_path = new_path
                    self.savesettings()

        if not self.savegame_path or not os.path.exists(self.savegame_path):
            if gui_enabled:
                new_save = open_filename(
                    "Select Teardown savegame.xml",
                    (("Teardown Save File", ".xml"), ("All Files", "*"))
                )
                if new_save:
                    self.savegame_path = new_save
                    self.savesettings()


    def savesettings(self):
        # Save our settings to our json file
        data = {
            "game_exe_path": self.game_exe_path,
            "savegame_path": self.savegame_path
        }
        with open(SETTINGS_PATH, "w") as f:
            json.dump(data, f, indent=4)


    async def reset_and_initialize_save(self):
        print("Initializing: Resetting the Save")

        if not self.savegame_path or not os.path.exists(self.savegame_path):
            return

        with open(self.savegame_path, 'r', encoding='utf-8') as f:
            text_data = f.read()
        clean_text = re.sub(r'^\s*<\d+[^>]*/>.*\n?', '', text_data, flags=re.MULTILINE)

        try:
            with open(self.savegame_path, "w", encoding='utf-8') as f:
                f.write(clean_text)

            tree = ET.parse(self.savegame_path)
            root = tree.getroot()

            self.player_data = root.find("savegame/mod/steam-3708322400")
            print(f"Initializing: player_data found: {self.player_data is not None}")

            if self.player_data is None:
                mod_node = root.find("mod")
                if mod_node is None:
                    mod_node = ET.SubElement(root, "mod")
                self.player_data = ET.SubElement(mod_node, "steam-3708322400")


            for category, nodes in SAVE_TEMPLATE.items():

                print(f"Initializing: Processing Category: {category}")
                cat_node = self.player_data.find(category)
                if cat_node is None:
                    print(f"Initializing: Category '{category}' not found, creating new SubElement.")

                cat_node = self.player_data.find(category)
                if cat_node is None:
                    cat_node = ET.SubElement(self.player_data, category)

                for path, val in nodes.items():
                    parts = path.split('/')
                    current = cat_node
                    for i, part in enumerate(parts):
                        child = current.find(part)
                        if child is None:
                            child = ET.SubElement(current, part)
                        if i == len(parts) - 1:
                            full_path = f"{category} -> {' -> '.join(parts)}"

                            print(f"Initializing:  [{full_path}] to value: {val}")
                            child.set("value", str(val))

                        current = child
            last_node = self.player_data.find("lastcompleted")
            if last_node is None:
                last_node = ET.SubElement(self.player_data, "lastcompleted")
            last_node.set("value", "")

            for message_node in self.player_data.findall("message"):
                self.player_data.remove(message_node)
                print(f"Initializing: Pruned message node: {message_node.tag}")

            for mission_node in self.player_data.findall("mission"):
                self.player_data.remove(mission_node)
                print(f"Initializing: Pruned message node: {mission_node.tag}")

            await self.apply_server_state_to_xml(self.player_data)

            bigint = getattr(self, "mission_bitmask", 0)
            current_count = bigint.bit_count()
            goal_required = getattr(self, 'MissionAmount', 20)
            print(f"Archipelago: Current Missions Count {current_count} Goal Required Count {goal_required}")

            if current_count >= goal_required:
                message_path = self.player_data.find("message")
                cullington_path = self.player_data.find("cullington_bomb")

                if cullington_path is None:
                    cullington_path = ET.SubElement(message_path, "cullington_bomb")

                cullington_path.set("value", "1")
                print("Archipelago: Final Mission Unlocked.")


            for i in range(5):  # Try 5 times
                try:
                    print(f"Initializing: Attempting initialization write {i + 1}/5")
                    ET.indent(tree, space="          ", level=0)
                    tree.write(self.savegame_path, encoding="UTF-8", xml_declaration=False)

                    print("Teardown Save: Player Data initialized and globally set.")
                    return True

                except PermissionError:
                    print("Initializing: File locked during init, retrying")
                    await asyncio.sleep(0.2)
                except Exception as e:
                    print(f"Failed to initialize player_data: {e}")
                    traceback.print_exc()
                    break

            return False

        except Exception as e:
            print(f"Failed to initialize player_data: {e}")
            traceback.print_exc()

    async def apply_server_state_to_xml(self, player_data):

        print("Initializing: Waiting for items to be received from server")
        while not hasattr(self, 'items_received') or not self.items_received:
            await asyncio.sleep(0.5)
        await asyncio.sleep(0.5)

        received_counts = {}
        print(f"First Apply: Total items in self.items_received: {len(self.items_received)}")
        self.last_received_count = len(self.items_received)

        for item in self.items_received:
            item_id = item.item
            received_counts[item_id] = received_counts.get(item_id, 0) + 1
            print(f"First Apply: Counted Item ID {item_id}")

        def update_node(path, value):
            node = player_data.find(path)
            if node is None:
                # Creation logic
                curr = player_data
                for part in path.split('/'):
                    child = curr.find(part)
                    if child is None: child = ET.SubElement(curr, part)
                    curr = child
                node = curr
            node.set("value", str(value))
            print(f"First Apply: Initial XML Setting - {path} set to {value}")

        # 1. Sync Tools & Missions
        for mapping in [Toolmap, Missionmap]:
            for ap_id, xml_path in mapping.items():
                count = received_counts.get(ap_id, 0)
                if count > 0:
                    update_node(xml_path, "1")

        for ap_id, config in Upgrademap.items():
            count = received_counts.get(ap_id, 0)
            path, mult, base = config
            final_val = (count * mult) + base
            update_node(path, final_val)

            print(f"First Apply: Initial Setting {ap_id} -> {path} is now {final_val} (Base {base} + {count} items)")
            update_node(path, final_val)



        current_cash = getattr(self, "cash_total", 0)
        cash_node = player_data.find("cash")
        self.last_cash = current_cash

        print(f"First Apply: Current Cash {current_cash}")
        if cash_node is None:
            print("First Apply: 'cash' node not found, creating new SubElement.")
            cash_node = ET.SubElement(player_data, "cash")

        cash_node.set("value", str(current_cash))
        print(f"First Apply: Cash XML node successfully synchronized to {current_cash}")


    async def sync_savegame(self):
        if not self.savegame_path or not os.path.exists(self.savegame_path):
            return False

        print(f"Sync: Starting Sync")

        try:
            tree = ET.parse(self.savegame_path)
            root = tree.getroot()
            self.player_data = root.find("savegame/mod/steam-3708322400")
            original_xml_string = ET.tostring(root, encoding="unicode")
            print("Sync: Parse successful.")

        except Exception as e:
            print(f"Sync: Parse FAILED with error: {e}")
            return


        self.check_missions()
        self.check_tools()
        self.check_valuables()
        self.apply_received_items(self.player_data)
        print("Sync: Functions ran.")

        new_xml_string = ET.tostring(root, encoding="unicode")

        if original_xml_string == new_xml_string:
            print("Sync: No changes in XML, skipping save.")
            return True

        print("Sync: XML Differences, Now Saving.")
        for i in range(5):
            try:
                print(f"Sync: Save started, attempt {i + 1}")
                ET.indent(tree, space="          ", level=0)
                tree.write(self.savegame_path, encoding="UTF-8", xml_declaration=False)
                return True  # Exit function and return to loop
            except PermissionError:
                print("Sync: File locked, waiting...")
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Sync: Critical Write Error: {e}")
                return False

        return False


    def check_missions(self):
        print("Sync Mission: Entering check_missions")
        if self.player_data is None:
            print("Sync Mission: Player Data is None")
            return

        last_node = self.player_data.find("lastcompleted")
        if last_node is None:
            print("Sync Mission: lastcompleted isn't found")
            return

        mission_id = last_node.get("value")
        if mission_id is None:
            print("Sync Mission: lastcompleted is none")
            return

        print(f"Sync Missions: Starting check_missions, lastcompleted: {mission_id}")

        if mission_id and mission_id in Mission_upgrade_send_map:
            start_id = Mission_upgrade_send_map[mission_id]

            print("Sync Mission: Trigger mission_counter")
            self.mission_counter(mission_id)

            mission_container = self.player_data.find("mission")
            if mission_container is not None:
                score_node = mission_container.find(f"{mission_id}/score")

                if score_node is not None:
                    current_score = int(score_node.get("value", "0"))
                    print(f"Sync Mission: Current Score is: {current_score}")

                    # Loop through the score
                    for i in range(current_score):
                        # Calculate the specific ID for this check
                        location_id = start_id + i

                        # Send the ID directly to your check function
                        self.send_upgrade_check(location_id)

            # 4. Clear the trigger in the XML data so it doesn't fire again
            last_node.set("value", "")

    def check_tools(self):
        print("Sync Tools: Entering check_tools")
        if self.player_data is None:
            return

        for xml_path, thresholds in Tool_upgrade_send_map.items():
            node = self.player_data.find(xml_path)
            if node is not None:
                try:
                    current_val_str = node.get("value", "0")
                    current_val = int(current_val_str)

                    for threshold_val, location_id in thresholds.items():
                        if location_id in self.locations_checked:
                            continue
                        if current_val >= threshold_val:
                            print(f"Sync Tools: {xml_path} reached {current_val} (Target: {threshold_val}). Sending ID {location_id}")

                            self.send_upgrade_check(location_id)


                except (ValueError, TypeError) as e:
                    print(f"Sync Tools: Error processing value at {xml_path}: {e}")
            else:
                pass

    def check_valuables(self):
        print("Sync Valuables: Entering check_valuables")
        if self.player_data is None:
            return

        cash_node = self.player_data.find("cash")
        if cash_node is None:
            print("Sync Valuables: cash isn't found")
            return
        try:
            current_cash = int(cash_node.get("value", "0"))
        except (ValueError, TypeError):
            return
        if not hasattr(self, "last_cash"):
            self.last_cash = None

        print(f"Sync Valuables: Current Cash {current_cash} Last Cash {self.last_cash}")
        if current_cash != self.last_cash:
            print(f"Sync Valuables: Cash changed from {self.last_cash} to {current_cash}. Scanning valuables...")
            self.watch_cash()

            # 3. Locate the 'valuable' base block in the XML
            valuable_base = self.player_data.find("valuable")
            if valuable_base is None:
                return
            print(f"Sync Valuables: No Valuable Base")
            # 4. Iterate over the valuable names and their sequential integer IDs
            for xml_path, location_id in Valuable_send_map.items():
                # Skip if this location check was already completed/sent
                if location_id in self.locations_checked:
                    continue

                # Look for the valuable item element inside the valuable block
                node = valuable_base.find(xml_path)
                if node is not None:
                    try:
                        current_val = int(node.get("value", "0"))

                        # If the valuable item has been collected (value is 1 or greater)
                        if current_val >= 1:
                            print(f"Sync Valuables: {xml_path} collected. Sending ID {location_id}")
                            self.send_upgrade_check(location_id)

                    except (ValueError, TypeError) as e:
                        print(f"Sync Valuables: Error processing value at {xml_path}: {e}")

    def watch_cash(self):
        print("Sync Cash: Entering watch_cash")

        if self.player_data is None:
            return

        cash_node = self.player_data.find("cash")
        if cash_node is None:
            print("Watch Cash: Cash isn't found")
            return
        try:
            current_cash = int(cash_node.get("value", "0"))
        except (ValueError, TypeError):
            return

        if current_cash != self.last_cash:
            print(f"Sync Cash: Current Cash {current_cash}, Last Cash {self.last_cash}")

            asyncio.create_task(self.send_msgs([{
                "cmd": "Set",
                "key": f"Teardown-{self.auth}-Cash",
                "default": 0,
                "want_reply": True,
                "operations": [{"operation": "replace", "value": current_cash}]
            }]))
            self.last_cash = current_cash
            print(f"Sync Cash: Updated cash on server to {current_cash}.")



    def send_upgrade_check(self, location_id):
        print(f"Sync Check: Entering send_upgrade_check location {location_id}")

        if location_id not in self.locations_checked:
            print(f"Sync Missions: Queuing Location ID {location_id}")

            asyncio.create_task(self.check_locations({location_id}))

            self.locations_checked.append(location_id)
            print(f"Success: Task created for {location_id}")


    def apply_received_items(self, player_data):
        print("Entering Apply Received Items")

        current_count = len(self.items_received)

        if current_count == self.last_received_count:
            print("No New Items")
            return

        received_item_counts = {}
        for item in self.items_received:
            item_id = item.item
            received_item_counts[item_id] = received_item_counts.get(item_id, 0) + 1
            print(f"DEBUG: Counted Item ID {item_id}")

        print(f"Sync Apply Items: Starting apply_received_items, total items in queue: {len(self.items_received)}")


        def update_node(path2, value):
            node = player_data.find(path2)
            if node is None:
                curr = player_data
                for part in path2.split('/'):
                    child = curr.find(part)
                    if child is None: child = ET.SubElement(curr, part)
                    curr = child
                node = curr
            node.set("value", str(value))
            print(f"DEBUG: XML Update - {path2} set to {value}")

        for mapping in [Toolmap, Missionmap]:
            for ap_id, xml_path in mapping.items():
                count = received_item_counts.get(ap_id, 0)
                if count > 0:
                    update_node(xml_path, "1")

        for ap_id, config in Upgrademap.items():
            count = received_item_counts.get(ap_id, 0)
            path, mult, base = config
            final_val = (count * mult) + base
            update_node(path, final_val)

            self.last_received_count = current_count
            print(f"DEBUG: {ap_id} -> {path} is now {final_val} (Base {base} + {count} items)")
            update_node(path, final_val)

        if not hasattr(self, 'applied_cash_counts'):
            self.applied_cash_counts = {ap_id: 0 for ap_id in Cashmap.keys()}

        cash_to_add = 0
        cash_counts_changed = False

        for ap_id, cash_val in Cashmap.items():
            total_received = received_item_counts.get(ap_id, 0)
            already_applied = self.applied_cash_counts.get(ap_id, 0)

            if total_received > already_applied:
                new_items = total_received - already_applied
                cash_to_add += new_items * cash_val

                # Update separate tracker for this item ID
                self.applied_cash_counts[ap_id] = total_received
                cash_counts_changed = True

            # If there is new cash to award, read current balance and increment it
        if cash_to_add > 0:
            cash_node = player_data.find("cash")
            current_cash = 0
            if cash_node is not None:
                try:
                    current_cash = int(cash_node.get("value", "0"))
                except (ValueError, TypeError):
                    pass

            new_cash_total = current_cash + cash_to_add
            update_node("cash", new_cash_total)
            print(f"DEBUG: Added {cash_to_add} cash. New total savegame cash: {new_cash_total}")

            # Sync the separate tracking counts back up to the server storage key
        if cash_counts_changed:
            asyncio.create_task(self.send_msgs([{
                "cmd": "Set",
                "key": f"Teardown_Applied_Cash_{self.team}_{self.slot}",
                "default": {},
                "want_reply": True,
                "operations": [{"operation": "replace", "value": self.applied_cash_counts}]
            }]))
            print(f"Archipelago: Synchronized separate cash counts to server: {self.applied_cash_counts}")


    def mission_counter(self, mission_id: str):
        # 1. Get the index (e.g., lee_login is 2)
        index = Missionindex.get(mission_id)

        if index is not None:
            # 1 << 2 becomes 00000100 in binary
            bit_to_set = 1 << index
            current_mask = getattr(self, 'mission_bitmask', 0)
            #if current_mask & bit_to_set:
                #print(f"Archipelago: Bit at index {index} is already 1. No update needed.")
                #return

            asyncio.create_task(self.send_msgs([{
                "cmd": "Set",
                "key": f"Teardown_Missions_Counter{self.team}_{self.slot}",
                "default": 0,
                "want_reply": True,
                "operations": [{"operation": "or", "value": bit_to_set}]
            }]))
            self.mission_bitmask = current_mask | bit_to_set
            print(f"Archipelago: Flipped bit {index} to 1.")

    def handle_victory_unlock(self, bitmask):
        if self.player_data is None:
            return

        final_mission = self.player_data.find("mission/cullington_bomb/score")
        final_score = final_mission.get("value")

        print(f"Final Score {final_score}")
        if final_score is not None and final_score == "1":
            asyncio.create_task(self.send_msgs([{
                "cmd": "StatusUpdate",
                "status": 30,
            }]))
            print("Goal Sent!!...?")

        current_count = bitmask.bit_count()
        goal_required = getattr(self, 'MissionAmount', 20)
        print(f"Archipelago: Current Missions Count {current_count} Goal Required Count {goal_required}")

        if current_count >= goal_required:
            message_path = self.player_data.find("message")
            cullington_path = self.player_data.find("cullington_bomb")

            if cullington_path is None:
                cullington_path = ET.SubElement(message_path, "cullington_bomb")

            cullington_path.set("value", "1")
            print("Archipelago: Final Mission Unlocked.")

            tree = ET.parse(self.savegame_path)

            for i in range(5):  # Try 5 times
                try:
                    print(f"Initializing: Attempting initialization write {i + 1}/5")
                    ET.indent(tree, space="          ", level=0)
                    tree.write(self.savegame_path, encoding="UTF-8", xml_declaration=False)

                    print("Teardown Save: Player Data initialized and globally set.")
                    return True

                except PermissionError:
                    print("Initializing: File locked during init, retrying")
                    time.sleep(0.2)
                except Exception as e:
                    print(f"Failed to initialize player_data: {e}")
                    traceback.print_exc()
                    break
        return None

    async def launch_game(self):
        if self.game_exe_path and os.path.exists(self.game_exe_path):
            subprocess.Popen([self.game_exe_path])
        else:
            print("Cannot launch: Valid executable path not found.")



    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.MissionAmount = args.get("slot_data", {}).get("MissionAmount", 20)
            self.location_name_to_id = args.get("slot_info", {}).get("location_name_to_id", {})
            self.last_connected_slot = self.slot


            async def init_sequence():
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown-{self.auth}-Missions"]}])
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown-{self.auth}-Cash"]}])
                await self.send_msgs([{"cmd": "Get", "keys": [f"Teardown_Missions_Counter{self.team}_{self.slot}"]}])

                await self.reset_and_initialize_save()
                self.auth_event.set()
                await self.launch_game()

            asyncio.create_task(init_sequence())


        elif cmd == "Retrieved":
            keys = args.get("keys", {})

            self.mission_count = keys.get(f"Teardown-{self.auth}-Missions") or 0
            self.mission_bitmask = keys.get(f"Teardown_Missions_Counter{self.team}_{self.slot}") or 0
            self.applied_cash_counts = keys.get(f"Teardown_Applied_Cash_{self.team}_{self.slot}") or {}
            self.cash_total = keys.get(f"Teardown-{self.auth}-Cash") or 0

        elif cmd == "SetReply":
            target_key = args.get("key")
            new_count = args.get("value")

            if target_key == f"Teardown_Missions_Counter{self.team}_{self.slot}":
                self.mission_bitmask = new_count
                self.handle_victory_unlock(new_count)

            elif target_key == f"Teardown_Applied_Cash_{self.team}_{self.slot}":
                self.applied_cash_counts = new_count


    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(TeardownContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game="Teardown")

    async def disconnect(self, allow_autoreconnect: bool = False):
        self.game = ""
        await super().disconnect(allow_autoreconnect)



async def main(args):
    ctx = TeardownContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.checkgamepath()
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    async def sync_loop():
        await ctx.auth_event.wait()
        print("DEBUG: Sync loop started!")
        await asyncio.sleep(10)
        while not ctx.exit_event.is_set():
            print("DEBUG: Loop tick...")
            if ctx.savegame_path and os.path.exists(ctx.savegame_path):
                await ctx.sync_savegame()
            await asyncio.sleep(3)

    ctx.sync_task = asyncio.create_task(sync_loop(), name="save sync loop")

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()

import colorama

def launch():
    parser = get_base_parser()

    parser.add_argument('--name', default=None, help="Slot Name to connect as.")

    args = parser.parse_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()


if __name__ == "__main__":
    launch()