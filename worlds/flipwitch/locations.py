from typing import List

from .data.locations import (all_locations, witchy_woods_locations, shop_locations, gacha_locations, costume_locations, quest_locations,
                                 FlipwitchLocation)
from .strings.locations import WitchyWoods, SpiritTown, Quest

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations() -> List[FlipwitchLocation]:
    locations = []
    create_base_locations(locations)
    create_shop_locations(locations)
    create_gacha_locations(locations)
    create_quest_locations(locations)
    create_costume_locations(locations)
    return locations


def create_base_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in witchy_woods_locations:
        locations.append(location)
    return locations


def create_shop_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in shop_locations:
        locations.append(location)
    return locations


def create_gacha_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in gacha_locations:
        locations.append(location)
    return locations


def create_quest_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in quest_locations:
        locations.append(location)
    return locations


def create_costume_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in costume_locations:
        locations.append(location)
    return locations

