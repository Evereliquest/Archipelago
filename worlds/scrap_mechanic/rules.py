from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has, HasGroup
from .options import GrowlabAmount

if TYPE_CHECKING:
    from .world import ScrapMechanicWorld


def set_all_rules(world: ScrapMechanicWorld) -> None:

    set_all_entrance_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: ScrapMechanicWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.
    menu_to_oldbuildingproblem = world.get_entrance("Main Menu to Old Building Problem")


    # Now, let's make some rules!
    #if world.options.ToolUpgrades:
        #world.set_rule(menu_to_oldbuildingproblem,  Has("Old Building Problem Unlock"))
        #world.set_rule(menu_to_bluetidecomputers,   Has("The BlueTide Computers Unlock") &  HasGroup("Wall/Opening", count=1) & HasGroup("Destruction", count=1))
        #world.set_rule(menu_to_speeddeal,           Has("The Speed Deal Unlock") &         (HasGroup("Wall/Opening", count=1) | HasGroup("Destruction", count=1)))
        #world.set_rule(menu_to_finaldiversion,      HasGroup("levels", count=FromOption(MissionAmount)) & HasGroup("Destruction", count=3))


    #if world.options.ToolUpgrades:
        #menu_to_blowtorchupgrade = world.get_entrance("Main Menu to Blowtorch Upgrades")






def set_completion_condition(world: ScrapMechanicWorld) -> None:

    world.set_completion_rule(HasGroup("levels", count=FromOption(GrowlabAmount)))