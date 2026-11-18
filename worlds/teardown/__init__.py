
from worlds.LauncherComponents import Component, components, launch as launch_component, icon_paths



def launch_client():
    from .client.teardownclient import launch
    launch_component(launch, name="TeardownClient")

components.append(Component(
    display_name="Teardown Client",
    func=launch_client,
    icon='Teardown Archipelago',
    description="Teardown's AP Client"
))

icon_paths['Teardown Archipelago'] = f"ap:{__name__}/teardownap.jpg"

from .world import TeardownWorld as TeardownWorld

