from .bases import TeardownTestBase


class BasicTestLogic(TeardownTestBase):
    # Our test base is a subclass of WorldTestBase.
    # WorldTestBase takes a dict of options and sets up a multiworld for you with a single world of your game.
    # The world will have the options you specified.
    options = {
        "Mission Amount": 30,
        "Randomize Starting Tools": False,
        "Randomize Starting Level": True,
        "Tool Upgrades": True,
        "Valuable Sanity": True,

    }
