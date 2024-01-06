from dataclasses import dataclass
from typing import List, Optional
from .data.location_data import base_locations, shop_locations, switch_locations, mob_drop_locations, events

LOCATION_CODE_START = 771111110


@dataclass(frozen=True)
class LocationDict:
    name: str
    region: str


def initialize_locations():
    loc_1 = []
    loc_2 = []
    loc_3 = []
    loc_4 = []
    for location in base_locations:
        loc_1.append(LocationDict(location.name, location.region))
    base_locations_cleaned = loc_1
    for location in shop_locations:
        loc_2.append(LocationDict(location.name, location.region))
    for location in switch_locations:
        loc_3.append(LocationDict(location.name, location.region))
    for location in mob_drop_locations:
        loc_4.append(LocationDict(location.name, location.region))
    shop_locations_cleaned = loc_2
    switch_locations_cleaned = loc_3
    mob_drop_locations_cleaned = loc_4
    locations = loc_1 + loc_2 + loc_3 + loc_4
    return locations, base_locations_cleaned, shop_locations_cleaned, switch_locations_cleaned, mob_drop_locations_cleaned


total_table = initialize_locations()
location_table = total_table[0]
base_location_table = total_table[1]
shop_locations_table = total_table[2]
switch_locations_table = total_table[3]
mob_drop_locations_table = total_table[4]
locations_by_name = {location.name: location for location in location_table}

