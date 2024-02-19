from dataclasses import dataclass
from random import Random
import logging

from BaseClasses import ItemClassification, Item
from typing import Dict, List, Union, Protocol

from .Options import LunacidOptions
from .data.location_data import base_locations, shop_locations, LocationData, mob_drop_locations
from .data.item_data import all_items
from .data.item_count_data import (base_weapons, base_spells, base_special_item_counts, base_unique_items, shop_weapons, shop_unique_items, shop_filler_items,
                                   drop_weapons, drop_spells, drop_filler_count, switches, filler_items)
from .data.switch_data import all_switches
from .data.weapon_data import all_weapons
from .data.spell_data import all_spells
from .strings.items import UniqueItem, Progressives, Coins
from .strings.options import Settings

logger = logging.getLogger(__name__)

ITEM_CODE_START = 771111110


@dataclass(frozen=True)
class ItemDict:
    code: int
    name: str
    classification: ItemClassification
    count: int


class LunacidItemFactory(Protocol):
    def __call__(self, name: Union[str, ItemDict]) -> Item:
        raise NotImplementedError


all_locations = base_locations + shop_locations + mob_drop_locations


def initialize_items_by_name() -> List[ItemDict]:
    items = []
    for item in all_items:
        items.append(ItemDict(ITEM_CODE_START + item.code, item.name, item.classification, 0))
    for weapon in all_weapons:
        items.append(ItemDict(ITEM_CODE_START + weapon.code, weapon.name, weapon.classification, 0))
    for spell in all_spells:
        items.append(ItemDict(ITEM_CODE_START + spell.code, spell.name, spell.classification, 0))
    for switch in all_switches:
        items.append(ItemDict(ITEM_CODE_START + switch.code, switch.name, switch.classification, 0))
    return items


item_table = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in item_table}


def create_items(item_factory: LunacidItemFactory, locations_count: int, items_to_exclude: List[Item], options: LunacidOptions, random: Random) -> List[Item]:
    items = []
    lunacid_items = create_lunacid_items(item_factory, options)
    for item in items_to_exclude:
        if item in lunacid_items:
            lunacid_items.remove(item)
    assert len(lunacid_items) <= locations_count, f"There should be at least as many locations [{locations_count}] as there are mandatory items [{len(lunacid_items)}]"
    items += lunacid_items
    logger.debug(f"Created {len(lunacid_items)} unique items")
    filler_slots = locations_count - len(lunacid_items)
    create_filler(item_factory, options, random, filler_slots, items)

    return items


def create_lunacid_items(item_factory: LunacidItemFactory, options: LunacidOptions):
    items = []
    create_weapons(item_factory, options, items)
    create_spells(item_factory, options, items)
    create_special_items(item_factory, options, items)
    create_switch_items(item_factory, options, items)
    return items


def create_weapons(item_factory: LunacidItemFactory, options: LunacidOptions, items: List[Item]):
    for item in base_weapons:
        items.append(item_factory(item))
    if options.shopsanity == options.shopsanity.option_true:
        for item in shop_weapons:
            items.append(item_factory(item))
    if options.dropsanity == options.dropsanity.option_true:
        for item in drop_weapons:
            items.append(item_factory(item))
    return items


def create_spells(item_factory: LunacidItemFactory, options: LunacidOptions, items: List[Item]):
    for item in base_spells:
        items.append(item_factory(item))
    if options.dropsanity == options.dropsanity.option_true:
        for item in drop_spells:
            items.append(item_factory(item))
    return items


def create_special_items(item_factory: LunacidItemFactory, options: LunacidOptions, items: List[Item]):
    for item in base_unique_items:
        items.append(item_factory(item))
    for item in base_special_item_counts:
        items.extend(item_factory(special_item) for special_item in [item] * base_special_item_counts[item])
    items.extend(item_factory(coin) for coin in [Coins.strange_coin] * get_coin_count(options))
    if options.shopsanity == options.shopsanity.option_true:
        for item in shop_unique_items:
            items.append(item_factory(item))
    return items


def create_switch_items(item_factory: LunacidItemFactory, options: LunacidOptions, items: List[Item]):
    if options.switchlocks == options.switchlocks.option_false:
        return items
    for item in switches:
        items.append(item_factory(item))
    return items


def create_filler(item_factory: LunacidItemFactory, options: LunacidOptions, random: Random, filler_slots: int, items: List[Item]):
    filler_list = filler_items.copy()
    if options.shopsanity == options.shopsanity.option_true:
        filler_list.extend([filler for filler in shop_filler_items if filler not in filler_list])
    if options.dropsanity == options.dropsanity.option_true:
        filler_list.extend([filler for filler in drop_filler_count if filler not in filler_list])
    items.extend([item_factory(filler) for filler in random.choices(filler_list, k=filler_slots)])
    return items


def get_coin_count(options: LunacidOptions):
    coin_setting = options.strangecoinbundle
    if coin_setting == coin_setting.option_one:
        return 30
    if coin_setting == coin_setting.option_two:
        return 15
    if coin_setting == coin_setting.option_three:
        return 10
    if coin_setting == coin_setting.option_five:
        return 6
    if coin_setting == coin_setting.option_six:
        return 5
    if coin_setting == coin_setting.option_ten:
        return 3
    if coin_setting == coin_setting.option_fifteen:
        return 2
    if coin_setting == coin_setting.option_thirty:
        return 1


all_filler = [item for item in item_table if item.classification is ItemClassification.filler]

group_table: Dict[str, List[str]] = {
    "vampiric symbol": [Progressives.vampiric_symbol],
    "switch": switches,
    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],
    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
