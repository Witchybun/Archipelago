from dataclasses import dataclass
from BaseClasses import ItemClassification, Item
from random import Random
from typing import Optional, Dict, List, Tuple
from .data.location_data import base_locations, shop_locations, LocationData
from .data.item_data import all_items
from .data.weapon_data import all_weapons
from .data.spell_data import all_spells
from .strings.items import UniqueItem
from .Options import LunacidOptions

ITEM_CODE_START = 771111110


@dataclass(frozen=True)
class ItemDict:
    name: str
    classification: ItemClassification
    count: Optional[int]


all_locations = base_locations + shop_locations


def initialize_items_by_name() -> List[ItemDict]:
    items = []
    for item in all_items:
        items.append(ItemDict(item.name, item.classification, None))
    for weapon in all_weapons:
        items.append(ItemDict(weapon.name, weapon.classification, None))
    for spell in all_spells:
        items.append(ItemDict(spell.name, spell.classification, None))
    return items


complete_items = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in complete_items}


def create_item_dict(locations: List[LocationData]) -> List[ItemDict]:
    item_data_list: List[Item] = []
    item_count = {}
    for location in locations:
        item_name = location.original_item
        item_data = complete_items_by_name[item_name]
        if item_data in item_data_list:
            item_count[item_name] += 1
            continue
        item_data_list.append(item_data)
        item_count[item_name] = 1
    return [ItemDict(item_data.name, item_data.classification, item_count[item_data.name]) for item_data in item_data_list]


item_table = create_item_dict(all_locations)
item_table_by_name = {item.name: item for item in item_table}
all_filler = [item for item in item_table if item.classification is ItemClassification.filler]


def extend_items_by_locations(options: LunacidOptions, locations: List[LocationData], incoming_items, random: Random):
    dictionary = create_item_dict(locations)
    items = dictionary[0]
    item_counts = dictionary[1]
    possible_filler_list = all_filler
    total_filler = 0
    for item_data in items:
        if item_data.classification is not ItemClassification.filler:
            incoming_items.append({
                'name': item_data.name,
                'count': item_counts[item_data.name],
                'classification': item_data.classification
            })
        if options.arbitraryfiller == options.arbitraryfiller.option_false:
            incoming_items.append({
                'name': item_data.name,
                'count': item_counts[item_data.name],
                'classification': item_data.classification
            })
        else:
            total_filler += 1
    if options.arbitraryfiller == options.arbitraryfiller.option_true:

        while total_filler > 0:
            num = random.randint(1,5)
            item = random.choice(possible_filler_list)
            possible_filler_list.remove(item)
            if not possible_filler_list:
                num = total_filler  # if we run out of items just go ham with the last one
            incoming_items.append({
                'name': item.name,
                'count': num,
                'classification': item.classification
            })
            total_filler -= num


def create_items(options: LunacidOptions, random: Random) -> List[ItemDict]:
    items = []
    extend_items_by_locations(options, base_locations, items, random)
    if options.shopsanity == options.shopsanity.option_true:
        extend_items_by_locations(options, shop_locations, items, random)
    return items


group_table: Dict[str, List[str]] = {
    "vampiric symbol": [UniqueItem.vampiric_symbol_a, UniqueItem.vampiric_symbol_e, UniqueItem.vampiric_symbol_w],

    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],

    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
