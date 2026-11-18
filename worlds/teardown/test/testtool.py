from .bases import TeardownTestBase


class BasicTestLogic(TeardownTestBase):
    # Our test base is a subclass of WorldTestBase.
    # WorldTestBase takes a dict of options and sets up a multiworld for you with a single world of your game.
    # The world will have the options you specified.
    options = {
        "MissionAmount": 39,
        "StartingTool": True,
        "AmountTools": 3,
        "StartingLevel": True,
        "AmountLevels": 1,
        "OptionalObjectives": True,
        "ToolUpgrades": True,
        "BundleTrack": False,
        "ValuableSanity": False,

    }
