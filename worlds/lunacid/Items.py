from dataclasses import dataclass
from BaseClasses import ItemClassification, Item
from typing import Dict, List
from .data.location_data import base_locations, shop_locations, LocationData, switch_locations, mob_drop_locations
from .data.item_data import all_items
from .data.weapon_data import all_weapons
from .data.spell_data import all_spells
from .strings.items import UniqueItem
from .strings.options import Settings

ITEM_CODE_START = 771111110


@dataclass(frozen=True)
class ItemDict:
    name: str
    classification: ItemClassification
    count: int


all_locations = base_locations + shop_locations + switch_locations + mob_drop_locations


def initialize_items_by_name() -> List[ItemDict]:
    items = []
    for item in all_items:
        items.append(ItemDict(item.name, item.classification, 0))
    for weapon in all_weapons:
        items.append(ItemDict(weapon.name, weapon.classification, 0))
    for spell in all_spells:
        items.append(ItemDict(spell.name, spell.classification, 0))
    return items


complete_items = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in complete_items}

events = []


def create_item_table(locations: List[LocationData]) -> List[ItemDict]:
    item_data_list: List[Item] = []
    item_count: Dict[str, int] = {}
    for location in locations:
        item_name = location.original_item
        item_data = complete_items_by_name[item_name]
        if item_data in item_data_list:
            item_count[item_name] += 1
            continue
        item_data_list.append(item_data)
        item_count[item_name] = 1
    return [ItemDict(item_data.name, item_data.classification, item_count[item_data.name]) for item_data in item_data_list]


item_table = create_item_table(all_locations)
base_table = create_item_table(base_locations)
base_table_by_name = {base.name: base for base in base_table}
shop_table = create_item_table(shop_locations)
shop_table_by_name = {shop.name: shop for shop in shop_table}
switch_table = create_item_table(switch_locations)
switch_table_by_name = {switch.name: switch for switch in switch_table}
mob_drop_table = create_item_table(mob_drop_locations)
mob_drop_table_by_name = {mob_drop.name: mob_drop for mob_drop in mob_drop_table}

item_table_by_setting_by_name = {Settings.base: base_table_by_name,
                                 Settings.shopsanity: shop_table_by_name,
                                 Settings.switch_shuffle: switch_table_by_name,
                                 Settings.mob_drops: mob_drop_table_by_name}

all_filler = [item for item in item_table if item.classification is ItemClassification.filler]

group_table: Dict[str, List[str]] = {
    "vampiric symbol": [UniqueItem.vampiric_symbol_a, UniqueItem.vampiric_symbol_e, UniqueItem.vampiric_symbol_w],

    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],

    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
