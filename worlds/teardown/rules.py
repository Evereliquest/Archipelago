from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, HasGroup
from .options import MissionAmount

if TYPE_CHECKING:
    from .world import TeardownWorld


def set_all_rules(world: TeardownWorld) -> None:

    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: TeardownWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    menu_to_oldbuildingproblem = world.get_entrance("Main Menu to Old Building Problem")
    menu_to_leecomputers = world.get_entrance("Main Menu to Lee Computers")
    menu_to_logindevices = world.get_entrance("Main Menu to Login Devices")
    menu_to_makingspace = world.get_entrance("Main Menu to Making Space")
    menu_to_classiccars = world.get_entrance("Main Menu to Classic Cars")
    menu_to_gpsdevices = world.get_entrance("Main Menu to The GPS Devices")
    menu_to_carwash = world.get_entrance("Main Menu to The Car Wash")
    menu_to_heavylifting = world.get_entrance("Main Menu to Heavy Lifting")
    menu_to_tower = world.get_entrance("Main Menu to The Tower")
    menu_to_finearts = world.get_entrance("Main Menu to Fine Arts")
    menu_to_toolup = world.get_entrance("Main Menu to Tool Up")
    menu_to_artreturn = world.get_entrance("Main Menu to Art Return")
    menu_to_covertchaos = world.get_entrance("Main Menu to Covert Chaos")
    menu_to_insurancefraud = world.get_entrance("Main Menu to Insurance Fraud")
    menu_to_bluetidecomputers = world.get_entrance("Main Menu to The BlueTide Computers")
    menu_to_speeddeal = world.get_entrance("Main Menu to The Speed Deal")
    menu_to_wetaffair = world.get_entrance("Main Menu to A Wet Affair")
    menu_to_poweroutage = world.get_entrance("Main Menu to Power Outage")
    menu_to_motivationalreminder = world.get_entrance("Main Menu to Motivational Reminder")
    menu_to_assortmentofdishes = world.get_entrance("Main Menu to An Assortment Of Dishes")
    menu_to_flooding = world.get_entrance("Main Menu to Flooding")
    menu_to_chase = world.get_entrance("Main Menu to The Chase")
    menu_to_roborazzi = world.get_entrance("Main Menu to Roborazzi")
    menu_to_secretingredients = world.get_entrance("Main Menu to The Secret Ingredients")
    menu_to_bluetideshortage = world.get_entrance("Main Menu to The BlueTide Shortage")
    menu_to_shippinglogs = world.get_entrance("Main Menu to The Shipping Logs")
    menu_to_alarmsystem = world.get_entrance("Main Menu to The Alarm System")
    menu_to_movingthegoods = world.get_entrance("Main Menu to Moving The Goods")
    menu_to_havocinparaside = world.get_entrance("Main Menu to Havoc In Paradise")
    menu_to_elenasrevenge = world.get_entrance("Main Menu to Elena's Revenge")
    menu_to_truckloadoftrouble = world.get_entrance("Main Menu to Truckload Of Trouble")
    menu_to_ornamentordeal = world.get_entrance("Main Menu to Ornament Ordeal")
    menu_to_quileztools = world.get_entrance("Main Menu to The Quilez Tools")
    menu_to_connectingthedots = world.get_entrance("Main Menu to Connecting The Dots")
    menu_to_pawnshop = world.get_entrance("Main Menu to The Pawn Shop")
    menu_to_droidabduction = world.get_entrance("Main Menu to The Droid Abduction")
    menu_to_maliceinwoonderland = world.get_entrance("Main Menu to Malice In Woonderland")
    menu_to_handlewithcare = world.get_entrance("Main Menu to Handle With Care")
    menu_to_droiddismount = world.get_entrance("Main Menu to Droid Dismount")
    menu_to_finaldiversion = world.get_entrance("Main Menu to The Final Diversion")


    # Now, let's make some rules!
    if world.options.ToolUpgrades:
        world.set_rule(menu_to_oldbuildingproblem,  Has("Old Building Problem Unlock"))
        world.set_rule(menu_to_leecomputers,        Has("Lee Computers Unlock"))
        world.set_rule(menu_to_logindevices,        Has("Login Devices Unlock"))
        world.set_rule(menu_to_makingspace,         Has("Making Space Unlock"))
        world.set_rule(menu_to_classiccars,         Has("Classic Cars Unlock"))
        world.set_rule(menu_to_gpsdevices,          Has("The GPS Devices Unlock"))
        world.set_rule(menu_to_carwash,             Has("The Car Wash Unlock"))
        world.set_rule(menu_to_heavylifting,        Has("Heavy Lifting Unlock") &           HasGroup("Wall Opening Tools", count=1) & HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_tower,               Has("The Tower Unlock"))
        world.set_rule(menu_to_finearts,            Has("Fine Arts Unlock"))
        world.set_rule(menu_to_toolup,              Has("Tool Up Unlock") &                (HasGroup("Wall Opening Tools", count=1) | HasGroup("Destruction Tools", count=1)) & HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_artreturn,           Has("Art Return Unlock") &              Has("Extinguisher Unlock"))
        world.set_rule(menu_to_covertchaos,         Has("Covert Chaos Unlock"))
        world.set_rule(menu_to_insurancefraud,      Has("Insurance Fraud Unlock") &         HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_bluetidecomputers,   Has("The BlueTide Computers Unlock") &  HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(menu_to_speeddeal,           Has("The Speed Deal Unlock") &         (HasGroup("Wall Opening Tools", count=1) | HasGroup("Destruction Tools", count=1)))
        world.set_rule(menu_to_wetaffair,           Has("A Wet Affair Unlock") &            HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=1))
        world.set_rule(menu_to_poweroutage,         Has("Power Outage Unlock") &            HasGroup("Wall Opening Tools", count=1) & HasGroup("Gun Tools", count=2))
        world.set_rule(menu_to_motivationalreminder, Has("Motivational Reminder Unlock") &  HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1) &  HasGroup("Gun Tools", count=1))
        world.set_rule(menu_to_assortmentofdishes,  Has("An Assortment Of Dishes Unlock") & HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1))
        world.set_rule(menu_to_flooding,            Has("Flooding Unlock") &                HasGroup("Wall Opening Tools", count=1) & Has("Plank Unlock") &               Has("Plank Max Length Upgrade", count=1) & Has("Plank Amount Upgrade", count=1))
        world.set_rule(menu_to_chase,               Has("The Chase Unlock"))
        world.set_rule(menu_to_roborazzi,           Has("Roborazzi Unlock"))
        world.set_rule(menu_to_secretingredients,   Has("The Secret Ingredients Unlock") &  HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=2))   #
        world.set_rule(menu_to_bluetideshortage,    Has("The BlueTide Shortage Unlock") &   HasGroup("Wall Opening Tools", count=1) & HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_shippinglogs,        Has("The Shipping Logs Unlock") &       HasGroup("Wall Opening Tools", count=2))

        world.set_rule(menu_to_alarmsystem,         Has("The Alarm System Unlock") &        (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_movingthegoods,      Has("Moving The Goods Unlock") &        (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_havocinparaside,     Has("Havoc In Paradise Unlock") &       (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_elenasrevenge,       Has("Elena's Revenge Unlock") &         (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))

        world.set_rule(menu_to_truckloadoftrouble,  Has("Truckload Of Trouble Unlock") &   ((Has("Plank Unlock") & Has("Plank Amount Upgrade", count=2) & Has("Plank Max Length Upgrade", count=1)) | (Has("Cable Unlock") & Has("Cable Amount Upgrade", count=2) & Has("Cable Stretch Upgrade", count=1))))
        world.set_rule(menu_to_ornamentordeal,      Has("Ornament Ordeal Unlock") &         HasGroup("Wall Opening Tools", count=3) & HasGroup("Gun Tools", count=1))
        world.set_rule(menu_to_quileztools,         Has("The Quilez Tools Unlock") &        HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1)&   Has("Plank Unlock") & Has("Plank Amount Upgrade", count=1))
        world.set_rule(menu_to_connectingthedots,   Has("Connecting The Dots Unlock") &     HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=3))
        world.set_rule(menu_to_pawnshop,            Has("The Pawn Shop Unlock") &           HasGroup("Wall Opening Tools", count=2) & Has("Plank Unlock"))
        world.set_rule(menu_to_droidabduction,      Has("The Droid Abduction Unlock") &     HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=2))
        world.set_rule(menu_to_maliceinwoonderland, Has("Malice In Woonderland Unlock") &   HasGroup("Destruction Tools", count=3) & HasGroup("Gun Tools", count=1) & Has("Nitroglycerin Unlock")& Has("Nitroglycerin Rounds Upgrade", count=2))
        world.set_rule(menu_to_handlewithcare,      Has("Handle With Care Unlock") &        HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1) & Has ("Rocket Launcher Unlock") & Has ("Rocket Launcher Rounds Upgrade", count=2))
        world.set_rule(menu_to_droiddismount,       Has("Droid Dismount Unlock") &          Has("Shotgun Unlock") & Has ("Rocket Launcher Unlock") & Has ("Rocket Launcher Rounds Upgrade", count=2))
        world.set_rule(menu_to_finaldiversion,      HasGroup("Levels", count=FromOption(MissionAmount)) & HasGroup("Destruction Tools", count=3))

    else:
        world.set_rule(menu_to_oldbuildingproblem,  Has("Old Building Problem Unlock"))
        world.set_rule(menu_to_leecomputers,        Has("Lee Computers Unlock"))
        world.set_rule(menu_to_logindevices,        Has("Login Devices Unlock"))
        world.set_rule(menu_to_makingspace,         Has("Making Space Unlock"))
        world.set_rule(menu_to_classiccars,         Has("Classic Cars Unlock"))
        world.set_rule(menu_to_gpsdevices,          Has("The GPS Devices Unlock"))
        world.set_rule(menu_to_carwash,             Has("The Car Wash Unlock"))
        world.set_rule(menu_to_heavylifting,        Has("Heavy Lifting Unlock") &           HasGroup("Wall Opening Tools", count=1) & HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_tower,               Has("The Tower Unlock"))
        world.set_rule(menu_to_finearts,            Has("Fine Arts Unlock"))
        world.set_rule(menu_to_toolup,              Has("Tool Up Unlock") &                (HasGroup("Wall Opening Tools", count=1) | HasGroup("Destruction Tools", count=1)) & HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_artreturn,           Has("Art Return Unlock") &              Has("Extinguisher Unlock"))
        world.set_rule(menu_to_covertchaos,         Has("Covert Chaos Unlock"))
        world.set_rule(menu_to_insurancefraud,      Has("Insurance Fraud Unlock") &         HasGroup("Plank/Cable Unlock", count=1))
        world.set_rule(menu_to_bluetidecomputers,   Has("The BlueTide Computers Unlock") &  HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(menu_to_speeddeal,           Has("The Speed Deal Unlock") &         (HasGroup("Wall Opening Tools", count=1) | HasGroup("Destruction Tools", count=1)))
        world.set_rule(menu_to_wetaffair,           Has("A Wet Affair Unlock") &            HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=1))
        world.set_rule(menu_to_poweroutage,         Has("Power Outage Unlock") &            HasGroup("Wall Opening Tools", count=1) & HasGroup("Gun Tools", count=2))
        world.set_rule(menu_to_motivationalreminder, Has("Motivational Reminder Unlock") &  HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1) &  HasGroup("Gun Tools", count=1))
        world.set_rule(menu_to_assortmentofdishes,  Has("An Assortment Of Dishes Unlock") & HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1))
        world.set_rule(menu_to_flooding,            Has("Flooding Unlock") &                HasGroup("Wall Opening Tools", count=1) & Has("Plank Unlock"))
        world.set_rule(menu_to_chase,               Has("The Chase Unlock"))
        world.set_rule(menu_to_roborazzi,           Has("Roborazzi Unlock"))
        world.set_rule(menu_to_secretingredients,   Has("The Secret Ingredients Unlock") &  HasGroup("Door Breaking Tools", count=1) &         HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=2))   #
        world.set_rule(menu_to_bluetideshortage,    Has("The BlueTide Shortage Unlock") &   HasGroup("Wall Opening Tools", count=1) & HasGroup("Plank/Cable Unlock", count=1))                                       #
        world.set_rule(menu_to_shippinglogs,        Has("The Shipping Logs Unlock") &       HasGroup("Wall Opening Tools", count=2))                                                                          #

        world.set_rule(menu_to_alarmsystem,         Has("The Alarm System Unlock") &        (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_movingthegoods,      Has("Moving The Goods Unlock") &        (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_havocinparaside,     Has("Havoc In Paradise Unlock") &       (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))
        world.set_rule(menu_to_elenasrevenge,       Has("Elena's Revenge Unlock") &         (Has("Sledge Hammer Unlock") | HasGroup("Destruction Tools", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Door Breaking Tools", count=1)))

        world.set_rule(menu_to_truckloadoftrouble,  Has("Truckload Of Trouble Unlock") &   (Has("Plank Unlock") | Has("Cable Unlock")))
        world.set_rule(menu_to_ornamentordeal,      Has("Ornament Ordeal Unlock") &         HasGroup("Wall Opening Tools", count=3) & HasGroup("Gun Tools", count=1))
        world.set_rule(menu_to_quileztools,         Has("The Quilez Tools Unlock") &        HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1)&   Has("Plank Unlock"))
        world.set_rule(menu_to_connectingthedots,   Has("Connecting The Dots Unlock") &     HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=3))
        world.set_rule(menu_to_pawnshop,            Has("The Pawn Shop Unlock") &           HasGroup("Wall Opening Tools", count=2) & Has("Plank Unlock"))
        world.set_rule(menu_to_droidabduction,      Has("The Droid Abduction Unlock") &     HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=2))
        world.set_rule(menu_to_maliceinwoonderland, Has("Malice In Woonderland Unlock") &   HasGroup("Destruction Tools", count=3) & HasGroup("Gun Tools", count=1) & Has("Nitroglycerin Unlock"))
        world.set_rule(menu_to_handlewithcare,      Has("Handle With Care Unlock") &        HasGroup("Wall Opening Tools", count=2) & HasGroup("Destruction Tools", count=1) & Has ("Rocket Launcher Unlock"))
        world.set_rule(menu_to_droiddismount,       Has("Droid Dismount Unlock") &          Has("Shotgun Unlock") & Has ("Rocket Launcher Unlock"))
        world.set_rule(menu_to_finaldiversion,      HasGroup("Levels", count=FromOption(MissionAmount)) & HasGroup("Destruction Tools", count=3))






    if world.options.ToolUpgrades:
        if world.options.BundleTrack:

            menu_to_blowtorchupgrade = world.get_entrance("Main Menu to Blowtorch Upgrades")
            menu_to_shotgunupgrade = world.get_entrance("Main Menu to Shotgun Upgrades")
            menu_to_plankupgrade = world.get_entrance("Main Menu to Plank Upgrades")
            menu_to_pipebombupgrade = world.get_entrance("Main Menu to Pipe Bomb Upgrades")
            menu_to_gunupgrade = world.get_entrance("Main Menu to Gun Upgrades")
            menu_to_bombupgrade = world.get_entrance("Main Menu to Bomb Upgrades")
            menu_to_rocketlauncherupgrade = world.get_entrance("Main Menu to Rocket Launcher Upgrades")
            menu_to_rocketboosterupgrade = world.get_entrance("Main Menu to Rocket Booster Upgrades")
            menu_to_leafblowerupgrade = world.get_entrance("Main Menu to Leaf Blower Upgrades")
            menu_to_cableupgrade = world.get_entrance("Main Menu to Cable Upgrades")
            menu_to_vehiclethrusterupgrade = world.get_entrance("Main Menu to Vehicle Thruster Upgrades")
            menu_to_nitroglycerinupgrade = world.get_entrance("Main Menu to Nitroglycerin Upgrades")
            menu_to_huntingrifleupgrade = world.get_entrance("Main Menu to Hunting Rifle Upgrades")
            menu_to_bluetideupgrade = world.get_entrance("Main Menu to BlueTide Upgrades")

            world.set_rule(menu_to_blowtorchupgrade, Has("Blowtorch Unlock"))
            world.set_rule(menu_to_shotgunupgrade, Has("Shotgun Unlock"))
            world.set_rule(menu_to_plankupgrade, Has("Plank Unlock"))
            world.set_rule(menu_to_pipebombupgrade, Has("Pipe Bomb Unlock"))
            world.set_rule(menu_to_gunupgrade, Has("Gun Unlock"))
            world.set_rule(menu_to_bombupgrade, Has("Bomb Unlock"))
            world.set_rule(menu_to_rocketlauncherupgrade, Has("Rocket Launcher Unlock"))
            world.set_rule(menu_to_rocketboosterupgrade, Has("Rocket Booster Unlock"))
            world.set_rule(menu_to_leafblowerupgrade, Has("Leaf Blower Unlock"))
            world.set_rule(menu_to_cableupgrade, Has("Cable Unlock"))
            world.set_rule(menu_to_vehiclethrusterupgrade, Has("Vehicle Thruster Unlock"))
            world.set_rule(menu_to_nitroglycerinupgrade, Has("Nitroglycerin Unlock"))
            world.set_rule(menu_to_huntingrifleupgrade, Has("Hunting Rifle Unlock"))
            world.set_rule(menu_to_bluetideupgrade, Has("BlueTide Unlock"))



    if world.options.ValuableSanity:
        menu_to_leevaluable = world.get_entrance("Main Menu to Lee Valuables")
        leevaluable_to_leevaluablehard = world.get_entrance("Lee Valuables to Lee Valuables Harder")
        leevaluable_to_leevaluablecomputers = world.get_entrance("Lee Valuables to Lee Valuables Computers")
        leevaluable_to_leevaluablewoonderland = world.get_entrance("Lee Valuables to Lee Valuables Woonderland")

        menu_to_marinavaluable = world.get_entrance("Main Menu to Marina Valuables")
        marinavaluable_to_marinavaluablehard = world.get_entrance("Marina Valuables to Marina Valuables Harder")
        marinavaluable_to_marinavaluablemakingspace = world.get_entrance("Marina Valuables to Marina Valuables Making Space")
        marinavaluable_to_marinavaluableafter = world.get_entrance("Marina Valuables to Marina Valuables After Art")

        menu_to_gordonvaluable = world.get_entrance("Main Menu to Gordon Valuables")
        gordonvaluable_to_gordonvaluablehard = world.get_entrance("Gordon Valuables to Gordon Valuables Harder")
        gordonvaluable_to_gordonvaluablefraud = world.get_entrance("Gordon Valuables to Gordon Valuables Fraud")

        menu_to_hollowrockvaluable = world.get_entrance("Main Menu to Hollowrock Valuables")
        hollowrockvaluable_to_hollowrockvaluablehard = world.get_entrance("Hollowrock Valuables to Hollowrock Valuables Harder")
        hollowrockvaluable_to_hollowrockvaluabledishes = world.get_entrance("Hollowrock Valuables to Hollowrock Valuables Dishes")

        menu_to_evertidesvaluable = world.get_entrance("Main Menu to Evertides Valuables")
        evertidesvaluable_to_evertidesvaluablehard = world.get_entrance("Evertides Valuables to Evertides Valuables Harder")
        evertidesvaluable_to_evertidesvaluablechaos = world.get_entrance("Evertides Valuables to Evertides Valuables Covert Chaos")

        menu_to_frustrumvaluable = world.get_entrance("Main Menu to Frustrum Valuables")
        frustrumvaluable_to_frustrumvaluablehard = world.get_entrance("Frustrum Valuables to Frustrum Valuables Harder")
        frustrumvaluable_to_frustrumvaluablechase = world.get_entrance("Frustrum Valuables to Frustrum Valuables Chase")

        menu_to_quilezvaluable = world.get_entrance("Main Menu to Quilez Valuables")
        quilezvaluable_to_quilezvaluablehard = world.get_entrance("Quilez Valuables to Quilez Valuables Harder")
        quilezvaluable_to_quilezvaluablecare = world.get_entrance("Quilez Valuables to Quilez Valuables Handle with Care")

        menu_to_islavaluable = world.get_entrance("Main Menu to Isla Valuables")
        islavaluable_to_islavaluablehard = world.get_entrance("Isla Valuables to Isla Valuables Harder")

        world.set_rule(menu_to_leevaluable, HasGroup("Lee Chemicals Unlock", count=1))
        world.set_rule(leevaluable_to_leevaluablehard, HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(leevaluable_to_leevaluablecomputers, Has("Lee Computers Unlock"))
        world.set_rule(leevaluable_to_leevaluablewoonderland, Has("Malice In Woonderland Unlock") & HasGroup("Wall Opening Tools", count=1))

        world.set_rule(menu_to_marinavaluable, HasGroup("West Point Marina Unlock", count=1))
        world.set_rule(marinavaluable_to_marinavaluablehard, HasGroup("West Point Marina Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(marinavaluable_to_marinavaluablemakingspace, Has("Making Space Unlock"))
        world.set_rule(marinavaluable_to_marinavaluableafter, Has("Art Return Unlock") & HasGroup("Wall Opening Tools", count=1))

        world.set_rule(menu_to_gordonvaluable, HasGroup("Villa Gordon Unlock", count=1))
        world.set_rule(gordonvaluable_to_gordonvaluablehard, HasGroup("Villa Gordon Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(gordonvaluable_to_gordonvaluablefraud, Has("Insurance Fraud Unlock"))

        world.set_rule(menu_to_hollowrockvaluable, HasGroup("Hollowrock Island Unlock", count=1))
        world.set_rule(hollowrockvaluable_to_hollowrockvaluablehard, HasGroup("Hollowrock Island Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(hollowrockvaluable_to_hollowrockvaluabledishes, Has("An Assortment Of Dishes Unlock"))

        world.set_rule(menu_to_evertidesvaluable, HasGroup("Evertides Mall Unlock", count=1))
        world.set_rule(evertidesvaluable_to_evertidesvaluablehard, HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(evertidesvaluable_to_evertidesvaluablechaos, Has("Covert Chaos Unlock") & HasGroup("Wall Opening Tools", count=1))

        world.set_rule(menu_to_frustrumvaluable, HasGroup("Frustrum Unlock", count=1))
        world.set_rule(frustrumvaluable_to_frustrumvaluablehard, HasGroup("Frustrum Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(frustrumvaluable_to_frustrumvaluablechase, Has("The Chase Unlock") & HasGroup("Wall Opening Tools", count=1))

        world.set_rule(menu_to_quilezvaluable, HasGroup("Quilez Security Unlock", count=1))
        world.set_rule(quilezvaluable_to_quilezvaluablehard, HasGroup("Quilez Security Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))
        world.set_rule(quilezvaluable_to_quilezvaluablecare, Has("Handle With Care Unlock"))

        world.set_rule(menu_to_islavaluable, HasGroup("Isla Estocastica Unlock", count=1))
        world.set_rule(islavaluable_to_islavaluablehard, HasGroup("Isla Estocastica Unlock", count=1) & HasGroup("Wall Opening Tools", count=1) & HasGroup("Destruction Tools", count=1))

    if world.options.ValuableSanity and world.options.ToolUpgrades:

        hollowrockvaluable_to_hollowrockvaluableevenharder = world.get_entrance("Hollowrock Valuables to Hollowrock Valuables Even Harder")
        world.set_rule(hollowrockvaluable_to_hollowrockvaluableevenharder, HasGroup("Hollowrock Island Unlock", count=1) & Has("Plank Unlock") & Has("Plank Amount Upgrade", count=3))


    if world.options.ValuableSanity and not world.options.ToolUpgrades:

        hollowrockvaluable_to_hollowrockvaluableevenharder = world.get_entrance("Hollowrock Valuables to Hollowrock Valuables Even Harder")
        world.set_rule(hollowrockvaluable_to_hollowrockvaluableevenharder, HasGroup("Hollowrock Island Unlock", count=1))



def set_completion_condition(world: TeardownWorld) -> None:

    world.set_completion_rule(HasGroup("Levels", count=FromOption(MissionAmount)))