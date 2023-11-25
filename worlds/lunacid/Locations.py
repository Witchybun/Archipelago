from dataclasses import dataclass
from typing import List, Optional
from .data.location_data import base_locations, shop_locations, events
from .Options import LunacidOptions

LOCATION_CODE_START = 771111110


@dataclass(frozen=True)
class LocationDict:
    code: Optional[int]
    name: str
    region: str


def create_event_locations():
    location_data = []
    for location in events:
        location_data.append(LocationDict(None, location.name, location.region))
    return location_data


def initialize_locations():
    locations = []
    for location in base_locations:
        locations.append(LocationDict(location.id, location.name, location.region))
    for location in shop_locations:
        locations.append(LocationDict(location.id, location.name, location.region))
    locations.extend(create_event_locations())
    return locations


location_table = initialize_locations()
locations_by_name = {location.name: location for location in location_table}


def extend_base_locations(location_data):
    for location in base_locations:
        location_data.append({
            'code': location.code,
            'name': location.name,
            'region': location.region
        })


def extend_shop_locations(options: LunacidOptions, location_data):
    shop = options.shopsanity
    if shop:
        return
    for location in shop_locations:
        location_data.append({
            'code': location.code,
            'name': location.name,
            'region': location.region
        })


def create_locations(options: LunacidOptions):
    world_locations: List[LocationDict] = []
    extend_base_locations(world_locations)
    extend_shop_locations(options, world_locations)
    return world_locations

