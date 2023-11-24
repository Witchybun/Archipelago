from typing import List, TypedDict, Dict
from .data.location_data import base_locations
from .data.item_data import all_items_by_name, Item
from .data.spell_data import all_spells_by_name
from .data.weapon_data import all_weapons_by_name


class LocationDict(TypedDict):
    name: str
    region: str


all_game_items_by_name = all_items_by_name + all_spells_by_name + all_weapons_by_name
item_total_table: Dict[Item, int] = {}
location_table: List[LocationDict] = []
for location in base_locations:
    location_table.append({'name': location.name, 'region': location.region})
    original_item = all_game_items_by_name[location.original_item]
    if original_item in item_total_table:
        item_total_table[original_item] += 1
    else:
        item_total_table[original_item] = 1
