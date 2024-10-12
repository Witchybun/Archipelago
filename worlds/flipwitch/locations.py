from typing import List

from . import FlipwitchOptions
from .data.locations import all_locations, gacha_locations, FlipwitchLocation, base_locations

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: FlipwitchOptions) -> List[FlipwitchLocation]:
    locations = []
    create_base_locations(locations)
    create_gacha_locations(options, locations)
    return locations


def create_base_locations(locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    for location in base_locations:
        locations.append(location)
    return locations


def create_gacha_locations(options: FlipwitchOptions, locations: List[FlipwitchLocation]) -> List[FlipwitchLocation]:
    if options.gachapon == options.gachapon.option_false:
        return locations
    for location in gacha_locations:
        locations.append(location)
    return locations
