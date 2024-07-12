from typing import List

from . import LunacidOptions
from .data.location_data import (all_locations, base_locations, shop_locations, unique_drop_locations, other_drop_locations, quench_locations, alchemy_locations,
                                 LunacidLocation)
from .strings.locations import BaseLocation

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: LunacidOptions, is_christmas: bool) -> List[LunacidLocation]:
    locations = []
    create_base_locations(options, is_christmas, locations)
    create_shop_locations(options, locations)
    create_drop_locations(options, locations)
    create_quench_locations(options, locations)
    create_alchemy_locations(options, locations)
    return locations


def create_base_locations(options: LunacidOptions, is_christmas: bool, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    for location in base_locations:
        if location.name in BaseLocation.abyss_locations and options.exclude_tower == options.exclude_tower.option_true:
            continue
        if location.name in BaseLocation.coin_locations and options.exclude_coin_locations == options.exclude_coin_locations.option_true:
            continue
        if location.name in BaseLocation.christmas_locations and not is_christmas:
            continue
        if location.name in BaseLocation.daedalus_locations and options.exclude_daedalus == options.exclude_daedalus.option_true:
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


def create_quench_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if options.quenchsanity == options.quenchsanity.option_false:
        return locations
    for location in quench_locations:
        locations.append(location)
    return locations


def create_alchemy_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if options.etnas_pupil == options.etnas_pupil.option_false:
        return locations
    for location in alchemy_locations:
        locations.append(location)
    return locations
