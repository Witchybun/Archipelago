from BaseClasses import ItemClassification
from typing import TypedDict, Dict, List

from .data.weapon_data import all_weapons
from .data.spell_data import all_spells
from .data.item_data import all_items
from .Locations import item_total_table


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


base_id = 771111110

item_table: List[ItemDict] = []
for weapon in all_weapons:
    item_table.append({'name': weapon.name, 'count': item_total_table[weapon.name], 'classification': weapon.classification})
for spell in all_spells:
    item_table.append({'name': spell.name, 'count': item_total_table[spell.name], 'classification': spell.classification})
for item in all_items:
    item_table.append({'name': item.name, 'count': item_total_table[item.name], 'classification': item.classification})

group_table: Dict[str, List[str]] = {
    "vampiric symbol": ["Vampiric Symbol (W)",
                        "Vampiric Symbol (A)",
                        "Vampiric Symbol (E)"],

    "vhs": ["VHS Tape",
            "White VHS Tape"],
}
