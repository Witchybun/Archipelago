from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List
from .strings.items import UniqueItem

from .Locations import item_total_table


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


base_id = 771111110

item_table: List[ItemDict] = []
for items in item_total_table:
    item_table.append({'name': items.name, 'count': item_total_table[items], 'classification': items.classification})

group_table: Dict[str, List[str]] = {
    "vampiric symbol": [UniqueItem.vampiric_symbol_a, UniqueItem.vampiric_symbol_e, UniqueItem.vampiric_symbol_w],

    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],

    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
