from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class MissionAmount(Range):
    """
    Amount of levels required to complete goal
    """
    display_name = "Mission Amount"

    range_start = 1
    range_end = 39
    default = 20


class RandomizeStartingTools(Toggle):
    """
    If enabled, the starting tools will be randomized.
    """
    display_name = "Randomize Starting Tools"


class RandomizeStartingLevel(DefaultOnToggle):
    """
    If enabled, the starting level is randomized, if not it is Old Building Problem.
    """
    display_name = "Randomize Starting Level"


class ToolUpgrades(DefaultOnToggle):
   """
   Enables Tool Upgrades
   """
   display_name = "Tool Upgrades"


class ValuableSanity(Toggle):
   """
   Enables Valuable Sanity
   """
   display_name = "Valuable Sanity"



@dataclass
class TeardownOptions(PerGameCommonOptions):
    MissionAmount: MissionAmount
    StartingTool: RandomizeStartingTools
    StartingLevel: RandomizeStartingLevel
    ToolUpgrades: ToolUpgrades
    ValuableSanity: ValuableSanity

