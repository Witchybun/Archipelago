from typing import List

from . import LunacidOptions
from .data.location_data import all_locations, base_locations, shop_locations, unique_drop_locations, other_drop_locations, LunacidLocation
from .strings.locations import BaseLocation

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: LunacidOptions) -> List[LunacidLocation]:
    locations = []
    create_base_locations(options, locations)
    create_shop_locations(options, locations)
    create_drop_locations(options, locations)
    return locations


def create_base_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    for location in base_locations:
        if location.name in BaseLocation.abyss_locations and options.exclude_tower == options.exclude_tower.option_true:
            continue
        if location.name in BaseLocation.coin_locations and options.exclude_coin_locations == options.exclude_coin_locations.option_true:
            continue
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
