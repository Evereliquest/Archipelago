from dataclasses import dataclass

from Options import PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class GrowlabAmount(Range):
    """
    Amount of Growlabs required to goal
    """
    display_name = "Growlab Amount"

    range_start = 1
    range_end = 7
    default = 3


class RandomizePlantUnlocks(DefaultOnToggle):
    """
    If enabled, plant unlocks from Growlabs will be randomized
    """
    display_name = "Randomize Plant Unlocks"


class TraderSanity(Toggle):
   """
   Randomizes schematics bought from the trader and introduces locations there instead
   """
   display_name = "Trader Sanity"


class QuestPlatform(Toggle):
   """
   Creates a location for all Quest Platforms
   """
   display_name = "Quest Platform Sanity"


class GarmentSanity(Range):
    """
    Amount of Garment locations to add to the Dress Bot
    """
    display_name = "Garment Sanity"

    range_start = 0
    range_end = 50
    default = 5


class SchematicSanity(Toggle):
   """
   Randomizes Schematics with an option below to control which
   """
   display_name = "Schematic Sanity"


class SchematicIntensity(Range):
    """
    Which Schematics get Randomized
    Has No Effect if Schematic Sanity is disabled
    1 is Initial Craftbot Schematics
    2 is Schematic-box Schematics (+ 1)
    3 is All Schematics (1 + 2 + Quests)
    """
    display_name = "Schematic Intensity"

    range_start = 1
    range_end = 3
    default = 1


class BuildBotSanity(Toggle):
   """
   Randomizes the Craftbot and similar bots (and resource collector)
   """
   display_name = "Build Bot Sanity"

class BadBotSanity(Toggle):
   """
   Makes locations for killing each hostile bot type
   """
   display_name = "Hostile Bot Sanity"

class SpudGunSanity(Toggle):
   """
   Randomizes Spud Guns (Makes the schematic pickups locations)
   """
   display_name = "Spud Gun Sanity"


class LiftSanity(Toggle):
   """
   Randomizes your lift... Not Recommended, it won't be fun
   """
   display_name = "Lift Sanity"
#Not Doing logic for up 1 down 1 yet

class HammerSanity(Toggle):
   """
   Randomizes your Hammer, not a good idea, probably worse than your lift
   """
   display_name = "Tool Sanity"


@dataclass
class TeardownOptions(PerGameCommonOptions):
    GrowlabAmount: GrowlabAmount
    RandomizePlantUnlocks: RandomizePlantUnlocks
    TraderSanity: TraderSanity
    QuestPlatform: QuestPlatform
    GarmentSanity: GarmentSanity
    SchematicSanity: SchematicSanity
    SchematicIntensity: SchematicIntensity
    BuildBotSanity: BuildBotSanity
    BadBotSanity: BadBotSanity
    SpudGunSanity: SpudGunSanity
    LiftSanity: LiftSanity
    HammerSanity: HammerSanity

