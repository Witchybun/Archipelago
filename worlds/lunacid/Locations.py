from typing import List, TypedDict, Dict
from .data.location_data import base_locations


class LocationDict(TypedDict):
    name: str
    region: str


item_total_table: Dict[str] = {}
location_table: List[LocationDict] = []
for location in base_locations:
    location_table.append({'name': location.name, 'region': location.region})
    if location.original_item in item_total_table:
        item_total_table[location.original_item] += 1
    else:
        item_total_table[location.original_item] = 1
