from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, HasGroup, Rule
from .options import GrowlabAmount

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


def set_all_rules(world: ScrapMechanicWorld) -> None:

    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ScrapMechanicWorld) -> None:
    menu_to_oldbuildingproblem = world.get_entrance("Main Menu to Old Building Problem")


    # Now, let's make some rules!
    #if world.options.ToolUpgrades:
        #world.set_rule(menu_to_oldbuildingproblem,  Has("Old Building Problem Unlock"))
        #world.set_rule(menu_to_bluetidecomputers,   Has("The BlueTide Computers Unlock") &  HasGroup("Wall/Opening", count=1) & HasGroup("Destruction", count=1))
        #world.set_rule(menu_to_speeddeal,           Has("The Speed Deal Unlock") &         (HasGroup("Wall/Opening", count=1) | HasGroup("Destruction", count=1)))
        #world.set_rule(menu_to_finaldiversion,      HasGroup("levels", count=FromOption(MissionAmount)) & HasGroup("Destruction", count=3))


    #if world.options.ToolUpgrades:
        #menu_to_blowtorchupgrade = world.get_entrance("Main Menu to Blowtorch Upgrades")



def set_all_location_rules(world: ScrapMechanicWorld) -> None:
    # Basic Rule
    # can_defeat_basic_enemy: Rule = Has("Sword")

    # if world.options.hard_mode:
        # can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")
        # can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit

    # Finally, we set our rule
    # right_room_enemy = world.get_location("Right Room Enemy Drop")
    # world.set_rule(right_room_enemy, can_defeat_basic_enemy)

    if world.options.RandomizePlantUnlocks:
        cottonplant = world.get_location("Cotton Plant")
        world.set_rule(cottonplant, Has("Cotton Seed Unlock"))

        cottonplant = world.get_location("Pigment Flower")
        world.set_rule(cottonplant, Has("Pigment Flower Seed Unlock"))

        cottonplant = world.get_location("Potato Plant")
        world.set_rule(cottonplant, Has("Potato Seed Unlock"))

        cottonplant = world.get_location("Tomato Plant")
        world.set_rule(cottonplant, Has("Tomato Seed Unlock"))

        cottonplant = world.get_location("Carrot Plant")
        world.set_rule(cottonplant, Has("Carrot Seed Unlock"))

        cottonplant = world.get_location("Redbeet Plant")
        world.set_rule(cottonplant, Has("Redbeet Seed Unlock"))

        cottonplant = world.get_location("Banana Plant")
        world.set_rule(cottonplant, Has("Banana Seed Unlock"))

        cottonplant = world.get_location("Chili Plant")
        world.set_rule(cottonplant, Has("Chili Seed Unlock"))

        cottonplant = world.get_location("Blueberry Plant")
        world.set_rule(cottonplant, Has("Blueberry Seed Unlock"))

        cottonplant = world.get_location("Orange Plant")
        world.set_rule(cottonplant, Has("Orange Seed Unlock"))

        cottonplant = world.get_location("Broccoli Plant")
        world.set_rule(cottonplant, Has("Broccoli Seed Unlock"))

        cottonplant = world.get_location("Pineapple Plant")
        world.set_rule(cottonplant, Has("Pineapple Seed Unlock"))




def set_completion_condition(world: ScrapMechanicWorld) -> None:

    world.set_completion_rule(HasGroup("Growlab Keys", count=FromOption(GrowlabAmount)))