from typing import List

from . import DreamOptions
from .data.locations import (all_locations, DreamLocation, base_locations, nasu_locations, witch_adventure_locations,
                             ao_oni_locations)

location_table = all_locations
locations_by_name = {location.name: location for location in location_table}


def create_locations(options: DreamOptions) -> List[DreamLocation]:
    locations = base_locations.copy()
    create_game_locations(options, locations)
    return locations

def create_game_locations(options: DreamOptions, locations: List[DreamLocation]) -> List[DreamLocation]:
    if "Nasu" in options.randomize_console.value:
        locations.extend(nasu_locations)
    if "Ao Oni" in options.randomize_console.value:
        locations.extend(ao_oni_locations)
    if "Witch Adventure" in options.randomize_console.value:
        locations.extend(witch_adventure_locations)
    return locations
