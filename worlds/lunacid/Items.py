from dataclasses import dataclass
from BaseClasses import ItemClassification, Item
from random import Random
from typing import Optional, Dict, List
from .data.location_data import base_locations, shop_locations, LocationData
from .data.item_data import all_items
from .data.weapon_data import all_weapons
from .data.spell_data import all_spells
from .strings.items import UniqueItem
from .Options import LunacidOptions

ITEM_CODE_START = 771111110


@dataclass(frozen=True)
class ItemDict:
    code: Optional[int]
    name: str
    classification: ItemClassification


all_locations = base_locations + shop_locations


def initialize_items_by_name() -> List[ItemDict]:
    items = []
    for item in all_items:
        items.append(ItemDict(item.code, item.name, item.classification))
    for weapon in all_weapons:
        items.append(ItemDict(weapon.code, weapon.name, weapon.classification))
    for spell in all_spells:
        items.append(ItemDict(spell.code, spell.name, spell.classification))
    return items


complete_items = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in complete_items}


def create_item_dict(locations: List[LocationData]) -> List[ItemDict]:
    item_data_list: List[Item] = []
    for location in locations:
        item_name = location.original_item
        item_data = complete_items_by_name[item_name]
        item_data_list.append(item_data)
    return [ItemDict(item_data.code, item_data.name, item_data.classification) for item_data in item_data_list]


item_table = create_item_dict(all_locations)
all_filler = [item for item in item_table if item.classification is ItemClassification.filler]


def extend_items_by_locations(options: LunacidOptions, locations: List[LocationData], incoming_items, random: Random):
    items = create_item_dict(locations)
    for item_data in items:
        if item_data.classification is not ItemClassification.filler:
            incoming_items.append({
                'code': item_data.code,
                'name': item_data.name,
                'classification': item_data.classification
            })
        if options.arbitraryfiller == options.arbitraryfiller.option_shuffled:
            incoming_items.extend({
                'code': item_data.code,
                'name': item_data.name,
                'classification': item_data.classification
            })
        elif options.arbitraryfiller == options.arbitraryfiller.option_random:
            random_filler = random.choice(all_filler)
            incoming_items.append({
                'code': random_filler.code,
                'name': random_filler.name,
                'classification': random_filler.classification
            })


def create_items(options: LunacidOptions, random: Random):
    items = []
    extend_items_by_locations( options, base_locations, items, random)
    if options.shopsanity == options.shopsanity.option_true:
        extend_items_by_locations(options, shop_locations, items, random)
    return items


group_table: Dict[str, List[str]] = {
    "vampiric symbol": [UniqueItem.vampiric_symbol_a, UniqueItem.vampiric_symbol_e, UniqueItem.vampiric_symbol_w],

    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],

    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
