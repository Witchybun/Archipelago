from dataclasses import dataclass
from .data.location_data import base_locations, shop_locations, unique_drop_locations, other_drop_locations

LOCATION_CODE_START = 771111110


@dataclass(frozen=True)
class LocationDict:
    code: int
    name: str
    region: str


def initialize_locations():
    base_locations_cleaned = []
    shop_locations_cleaned = []
    unique_drop_locations_cleaned = []
    other_drop_locations_cleaned = []

    for location in base_locations:
        base_locations_cleaned.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))
    for location in shop_locations:
        shop_locations_cleaned.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))
    for location in unique_drop_locations:
        unique_drop_locations_cleaned.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))
    for location in other_drop_locations:
        other_drop_locations_cleaned.append(LocationDict(LOCATION_CODE_START + location.id, location.name, location.region))
    locations = base_locations_cleaned + shop_locations_cleaned + unique_drop_locations_cleaned + other_drop_locations_cleaned
    return locations, base_locations_cleaned, shop_locations_cleaned, unique_drop_locations_cleaned, other_drop_locations_cleaned


total_table = initialize_locations()
location_table = total_table[0]
base_location_table = total_table[1]
shop_locations_table = total_table[2]
unique_drop_locations_table = total_table[3]
other_drop_locations_table = total_table[4]
locations_by_name = {location.name: location for location in location_table}

