from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from . import LunacidWorld


def setup_options_from_slot_data(world: "LunacidWorld"):
    if hasattr(world.multiworld, "re_gen_passthrough"):
        if "Lunacid" in world.multiworld.re_gen_passthrough:
            world.using_ut = True
        else:
            world.using_ut = False
    else:
        world.using_ut = False


def map_page_index(data: Any) -> int:
    if not isinstance(data, str):
        return 0
    mapping = {
        "PITT_A1": 3,
        "SEWER_A1": 4,
        "HUB_01": 2,
        "LAKE": 5,
        "HAUNT": 6,
        "FOREST_A1": 7,
        "FOREST_B1": 8,
        "ARCHIVES": 9,
        "CAS_1": 10,
        "CAS_3": 11,
        "WALL_01": 12,
        "PITT_B1": 13,
        "CAS_2": 14,
        "CAS_PITT": 15,
        "CAVE": 16,
        "TOWER": 17,
        "PRISON": 18,
        "ARENA": 19,
        "VOID": 19,
        "ARENA2": 20,
        "END_TOWN": 21,
    }
    return mapping.get(data, 0)


TRACKER_WORLD = {
    "map_page_folder": "tracker",
    "map_page_maps": "maps/maps.json",
    "map_page_locations": "locations/locations.json",
    "map_page_setting_key": "Slot:{player}:Current Scene",
    "map_page_index": map_page_index,
}
