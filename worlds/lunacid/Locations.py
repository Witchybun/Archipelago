from typing import List

from . import LunacidOptions
from .data.location_data import all_locations, base_locations, shop_locations, unique_drop_locations, other_drop_locations, LunacidLocation

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: LunacidOptions) -> List[LunacidLocation]:
    locations = []
    create_base_locations(locations)
    create_shop_locations(options, locations)
    create_drop_locations(options, locations)
    return locations


def create_base_locations(locations: List[LunacidLocation]) -> List[LunacidLocation]:
    for location in base_locations:
        locations.append(location)
    return locations


def create_shop_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if options.shopsanity == options.shopsanity.option_false:
        return locations
    for location in shop_locations:
        locations.append(location)
    return locations


def create_drop_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if options.dropsanity == options.dropsanity.option_off:
        return locations
    for location in unique_drop_locations:
        locations.append(location)
    if options.dropsanity == options.dropsanity.option_randomized:
        for location in other_drop_locations:
            locations.append(location)
    return locations
