from typing import List

from . import LunacidOptions
from .data.location_data import (all_locations, base_locations, shop_locations, unique_drop_locations,
                                 other_drop_locations, quench_locations, alchemy_locations,
                                 LunacidLocation, spooky_locations, crimpus_locations, stat_locations)
from .strings.locations import SpookyLocation

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: LunacidOptions, month: int) -> List[LunacidLocation]:
    locations = base_locations.copy()
    create_shop_locations(options, locations)
    create_drop_locations(options, locations)
    create_quench_locations(options, locations)
    create_alchemy_locations(options, locations)
    create_spooky_locations(options, month, locations)
    create_crimpus_locations(month, locations)
    return locations


def create_shop_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if not options.shopsanity:
        return locations
    for location in shop_locations:
        locations.append(location)
    return locations


def create_drop_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if not options.dropsanity:
        return locations
    for location in unique_drop_locations:
        locations.append(location)
    if options.dropsanity == options.dropsanity.option_randomized:
        for location in other_drop_locations:
            locations.append(location)
    return locations


def create_quench_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if not options.quenchsanity:
        return locations
    for location in quench_locations:
        locations.append(location)
    return locations


def create_alchemy_locations(options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if not options.etnas_pupil:
        return locations
    for location in alchemy_locations:
        locations.append(location)
    return locations


def create_spooky_locations(options: LunacidOptions, month: int, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if month != 10:
        return locations
    for location in spooky_locations:
        if location.name == SpookyLocation.headless_horseman and not options.dropsanity:
            continue
        locations.append(location)
    return locations


def create_crimpus_locations(month: int, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if month != 12:
        return locations
    for location in crimpus_locations:
        locations.append(location)
    return locations


def create_stat_locations(total_stats: int, options: LunacidOptions, locations: List[LunacidLocation]) -> List[LunacidLocation]:
    if not options.statsanity:
        return locations
    counter = 1
    for location in stat_locations:
        if counter >= total_stats:
            break
        locations.append(location)
    return locations
