from dataclasses import dataclass
from BaseClasses import ItemClassification
from random import Random
from typing import List, TypedDict, Dict, Protocol, Optional, Tuple
from .strings.regions_entrances import LunacidRegion
from .data.location_data import base_locations, shop_locations, events
from .data.item_data import all_item_data_by_name, Item, all_filler_items
from .data.spell_data import all_spells_by_name
from .data.weapon_data import all_weapons_by_name
from .Options import LunacidOptions

LOCATION_CODE_START = 771111110


@dataclass(frozen=True)
class LocationDict:
    code: Optional[int]
    name: str
    region: str


class LunacidLocationCollector(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


all_game_items_by_name = all_item_data_by_name + all_spells_by_name + all_weapons_by_name

all_locations = base_locations
locations_by_name = {location.name: location for location in all_locations}


def create_event_locations():
    location_data = []
    for location in events:
        location_data.append(LocationDict(None, location.name, location.region))
    return location_data


all_event_locations = create_event_locations()


def extend_base_locations(location_data: List[LocationDict]):
    for location in base_locations:
        location_data.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))


def extend_shop_locations(options: LunacidOptions, location_data: List[LocationDict]):
    shop = options.shopsanity
    if shop:
        return
    for location in shop_locations:
        location_data.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))


def create_locations(location_collector: LunacidLocationCollector, options: LunacidOptions):
    world_locations: List[LocationDict] = []
    extend_base_locations(world_locations)
    extend_shop_locations(options, world_locations)
    for location_data in world_locations:
        location_collector(location_data.name, location_data.code, location_data.region)
