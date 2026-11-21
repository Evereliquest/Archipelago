from dataclasses import dataclass
from schema import Schema, And

from Options import PerGameCommonOptions, OptionGroup, Range, Toggle, DefaultOnToggle, OptionSet, Choice


class CampaignSelection(OptionSet):
    """
    What Campaigns are Enabled?
    Choose as many or as few as you want (Must have 1 at least)

    Possible values are:
    - Base Campaign
    - Time Campers
    """
    #- Relics of Barkuna
    #- Greenwash Gambit
    #- Folkrace
    #- Art Vandels
    #"""
    display_name = "Campaign Selection"
    valid_keys = {
        "Base Campaign",
        "Time Campers",
        #"Relics of Barkuna",
        #"Greenwash Gambit",
        #"Folkrace",
        #"Art Vandels",
    }
    default = {"Base Campaign"}
    schema = Schema(And(set, len),
                    error="Teardown option 'Campaign Selection' is empty. Add at least one campaign")

class GoalSelection(Choice):
    """
    Which goals are enabled?
    Choose as many or as few as you want (Must have 1 at least)

    Possible values are:
    - Missions Goal
        - Makes part of your goal completing a determined amount of missions counted from all enabled campaigns

    - Campaigns Goal
        - Makes part of your goal completing a determined amount of campaigns from all enabled campaigns

    - Items Goal
        - Makes part of your goal collecting a determined amount of 'Destruction Fragment' items from the multiworld
        (Item only affects goal, no effect on gameplay)
    """

    display_name = "Goal Selection"
    valid_keys = {
        "Missions Goal",
        "Campaigns Goal",
        "Items Goal",
    }
    default = {"Missions Goal"}
    schema = Schema(And(set, len),
                    error="Teardown option 'Goal Selection' is empty. Add at least one Goal")


class MissionAmount(Range):
    """
    Amount of Missions to Complete Missions Goal, If Enabled

    Keep in mind the campaigns you have enabled, too many levels for the campaigns you have enabled will error

    Base Campaign has 40 Missions
    Time Keepers has 7 Missions
    """
    display_name = "Mission Goal Amount"

    range_start = 1
    range_end = 47
    default = 20

class CampaignAmount(Range):
    """
    Amount of Campaigns to Complete Missions Goal, If Enabled
    """
    display_name = "Campaign Goal Amount "

    range_start = 1
    range_end = 2
    default = 1

class ItemPercentage(Range):
    """
    What Percentage Items to Complete Items Goal, If Enabled
        20 'Destruction Fragment' Items will be created
    """
    display_name = "Items Goal Percentage"

    range_start = 60
    range_end = 100
    default = 80


class FastGoal(Toggle):
   """
   Completes Missions goal and Campaigns goal when you receive the required amount of mission unlocks for either/both

   For Example
        When you have a missions goal of 30, and have 30 missions unlocked, missions goal will send
        When you have a campaign goal of 1, and have all 7 Time Camper missions unlocked, campaign goal will send
   """
   display_name = "Fast Goal"

#class EasyGoal(Toggle):
#   """
#   Immidiently goals the slot upon unlocking the final level instead of requiring completion of it (I prefer the cinimatic ending of the level personally).
#   """
#   display_name = "Easy Goal"

#---

class RandomizeStartingTools(Toggle):
    """
    If enabled, the starting tools will be randomized for each enabled campaign.
    """
    display_name = "Randomize Starting Tools"

class AmountTools(Range):
    """
    Amount of Starting Tools between 0 and 17. Default is 3, only used if tools are randomized
    Each campaign is randomized independently
    If set above a campaign's maximum it will be reduced for that campaign (Above max reduces to max)
    """
    display_name = "Number of Starting Tools"

    range_start = 0
    range_end = 17
    default = 3


class RandomizeStartingLevel(DefaultOnToggle):
    """
    If enabled, the starting level for each campaign is randomized
    If not it is the first level of each campaign
    """
    display_name = "Randomize Starting Level"

class AmountLevels(Range):
    """
    Amount of starting levels if levels are randomized
    Will randomly give easy levels from any enabled campaign
    """
    display_name = "Number of Starting Levels"

    range_start = 1
    range_end = 39
    default = 1


class OptionalObjectives(DefaultOnToggle):
    """
    Creates locations for optional objectives across all campaigns
    Turning this off makes a more relaxed experience (logic doesn't change)
    """
    display_name = "Randomize Optional Objectives"

#---

class ToolUpgrades(DefaultOnToggle):
   """
   Randomizes tool upgrades for the base campaign
   This means an item and location are created for each upgrade
   """
   display_name = "Tool Upgrades"

class BundleTrack(Toggle):
   """
   Uses Cash Bundles for tool upgrade logic, if Tool Upgrades are enabled
   This will treat tool upgrades as only in-logic once you've received enough cash from the bundles, and ignore possible valuable collection
   There are bigger cash bundles included to make logic easier for generation ($41,000~ with $33,000~ Needed)
   """
   display_name = "Cash Bundle Tracking"


class ValuableSanity(Toggle):
   """
   Creates a location for every valuable in the basegame campaign (269).
   """
   display_name = "Valuable Sanity"

#---

class TimeValuableSanity(Toggle):
   """
   Creates a location for every souvenir in the Time Campers campaign (----).
   """
   display_name = "Time Campers Souvenir Sanity"



@dataclass
class TeardownOptions(PerGameCommonOptions):
    CampaignSelection: CampaignSelection
    GoalSelection: GoalSelection
    MissionAmount: MissionAmount
    CampaignAmount: CampaignAmount
    ItemPercentage: ItemPercentage
    FastGoal: FastGoal
#    EasyGoal: EasyGoal

    StartingTool: RandomizeStartingTools
    AmountTools: AmountTools
    StartingLevel: RandomizeStartingLevel
    AmountLevels: AmountLevels
    OptionalObjectives: OptionalObjectives

    ToolUpgrades: ToolUpgrades
    BundleTrack: BundleTrack
    ValuableSanity: ValuableSanity

    TimeValuableSanity: TimeValuableSanity


option_groups = [
    OptionGroup("Goal Options",[
        CampaignSelection,
        GoalSelection,
        MissionAmount,
        CampaignAmount,
        ItemPercentage,
        FastGoal,
#        EasyGoal
    ],),

    OptionGroup("Overall Gameplay Options", [
        RandomizeStartingTools,
        AmountTools,
        RandomizeStartingLevel,
        AmountLevels,
    ], ),

    OptionGroup("Basegame Campaign Options", [
        ToolUpgrades,
        BundleTrack,
        ValuableSanity,
    ], ),

    OptionGroup("Time Campers Options", [
        TimeValuableSanity,
    ], ),
]



