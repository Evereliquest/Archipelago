from .bases import TeardownTestBase


class BasicTestLogic(TeardownTestBase):
    # Our test base is a subclass of WorldTestBase.
    # WorldTestBase takes a dict of options and sets up a multiworld for you with a single world of your game.
    # The world will have the options you specified.
    options = {
        "Mission Amount": 40,
        "Randomize Starting Tools": False,
        "Randomize Starting Level": False,
        "Tool Upgrades": True,
        "Valuable Sanity": False,

    }
