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


class AmountTools(Range):
    """
    Amount of Starting Tools between 0 and 17. Default is 3, only used if tools are randomized
    """
    display_name = "Number of Starting Tools"

    range_start = 0
    range_end = 17
    default = 3


class RandomizeStartingLevel(DefaultOnToggle):
    """
    If enabled, the starting level is randomized, if not it is Old Building Problem.
    """
    display_name = "Randomize Starting Level"


class AmountLevels(Range):
    """
    Amount of Starting Levels between 1 and 39, default is 1.
    """
    display_name = "Number of Starting Levels"

    range_start = 1
    range_end = 39
    default = 1




class ToolUpgrades(DefaultOnToggle):
   """
   Enables Tool Upgrades in the Terminal as locations.
   """
   display_name = "Tool Upgrades"


class ValuableSanity(Toggle):
   """
   Creates a location for every valuable in the game (269).
   """
   display_name = "Valuable Sanity"



@dataclass
class TeardownOptions(PerGameCommonOptions):
    MissionAmount: MissionAmount
    StartingTool: RandomizeStartingTools
    AmountTools: AmountTools
    StartingLevel: RandomizeStartingLevel
    AmountLevels: AmountLevels
    ToolUpgrades: ToolUpgrades
    ValuableSanity: ValuableSanity

