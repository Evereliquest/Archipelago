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
    If enabled, plant unlocks are randomized
    """
    display_name = "Randomize Plant Unlocks"


class InitialSchematics(Toggle):
   """
   Randomizes Initial Schematics (excluding Mini Craftbot recipes)
   """
   display_name = "Inital Schematics Sanity"


class SchematicBoxes(Toggle):
   """
   Randomizes the Schematics from Schematic Boxes
   """
   display_name = "Inital Schematics Sanity"


class QuestSanity(Toggle):
   """
   Randomizes All Quests, including the rewards for said quests
   """
   display_name = "Quest Sanity"

# Then if something like quests are off and spud guns are rewards, and they are turned off (not random)
# then reward them as normal, quests on reward as normal, no locations. Guns on quests off give Location
# If both on give one location

class QuestPlatform(Toggle):
   """
   Creates a location for all Quest Platforms
   """
   display_name = "Quest Platform Sanity"


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


class TraderSanity(Toggle):
   """
   Adds Locations to the trader
   """
   display_name = "Trader Sanity"


class GarmentSanity(Range):
    """
    Amount of Garment locations to add to the Dress Bot
    """
    display_name = "Garment Sanity"

    range_start = 0
    range_end = 50
    default = 5


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
class ScrapMechanicOptions(PerGameCommonOptions):
    GrowlabAmount: GrowlabAmount
    RandomizePlantUnlocks: RandomizePlantUnlocks
    InitialSchematics: InitialSchematics
    SchematicBoxes: SchematicBoxes
    QuestSanity: QuestSanity
    QuestPlatform: QuestPlatform
    BuildBotSanity: BuildBotSanity
    BadBotSanity: BadBotSanity
    TraderSanity: TraderSanity
    GarmentSanity: GarmentSanity
    SpudGunSanity: SpudGunSanity
    LiftSanity: LiftSanity
    HammerSanity: HammerSanity

