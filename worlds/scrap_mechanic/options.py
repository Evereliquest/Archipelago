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


class PartSanity(Toggle):
   """
   Creates items for all initially unlocked recipes available at the Craftbot.
   Does not include the Mini Craftbot or recipes given other ways.
   """
   display_name = "Part Sanity"


class SchematicSanity(Toggle):
   """
   Randomizes all Schematic boxes and their rewards
   """
   display_name = "Schematic Box Sanity"


class BotSanity(Toggle):
   """
   Randomizes the Craft bot and similar bots
   """
   display_name = "Bot Sanity"


class LiftSanity(Toggle):
   """
   Randomizes your lift... Not Recommended, it won't be fun
   """
   display_name = "Lift Sanity"


@dataclass
class TeardownOptions(PerGameCommonOptions):
    GrowlabAmount: GrowlabAmount
    RandomizePlantUnlocks: RandomizePlantUnlocks
    TraderSanity: TraderSanity
    QuestPlatform: QuestPlatform
    GarmentSanity: GarmentSanity
    PartSanity: PartSanity
    SchematicSanity: SchematicSanity
    BotSanity: BotSanity
    LiftSanity: LiftSanity

