from random import Random
import logging

from BaseClasses import ItemClassification, Item
from typing import Dict, List, Union, Protocol

from worlds.flipwitch.data.items import FlipwitchItemData, all_items, base_items, gacha_items, costume_items, quest_items
from worlds.flipwitch.strings.items import Coin

logger = logging.getLogger(__name__)


class FlipwitchItemFactory(Protocol):
    def __call__(self, name: Union[str, FlipwitchItemData], override_classification: ItemClassification = None) -> Item:
        raise NotImplementedError


def initialize_items_by_name() -> List[FlipwitchItemData]:
    items = []
    for item in all_items:
        items.append(item)
    return items


item_table = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in item_table}


def create_items(item_factory: FlipwitchItemFactory, locations_count: int, items_to_exclude: List[Item]) -> List[Item]:
    items = []
    flipwitch_items = create_flipwitch_items(item_factory)
    for item in items_to_exclude:
        if item in flipwitch_items:
            flipwitch_items.remove(item)
    assert len(
        flipwitch_items) <= locations_count, f"There should be at least as many locations [{locations_count}] as there are mandatory items [{len(flipwitch_items)}]"
    items += flipwitch_items
    logger.debug(f"Created {len(flipwitch_items)} unique items")
    filler_slots = locations_count - len(items)
    create_filler(item_factory, filler_slots, items)

    return items


def create_flipwitch_items(item_factory: FlipwitchItemFactory) -> List[Item]:
    items = []
    create_base_items(item_factory, items)
    create_gacha_items(item_factory, items)
    create_quest_items(item_factory, items)
    # create_shop_items(item_factory, options, items)
    create_costume_items(item_factory, items)
    return items


def create_base_items (item_factory: FlipwitchItemFactory, items: List[Item]):
    for item in base_items:
        if item.name == "Nothing":
            continue
        items.append(item_factory(item.name))
    return items


def create_quest_items(item_factory: FlipwitchItemFactory, items: List[Item]):
    for item in quest_items:
        items.append(item_factory(item.name))
    return items


def create_gacha_items(item_factory: FlipwitchItemFactory, items: List[Item]):
    for item in gacha_items:
        if item.name == Coin.lucky_coin:
            items.extend(item_factory(lucky) for lucky in [Coin.lucky_coin]*2)
            continue
        items.append(item_factory(item.name))
    return items


def create_costume_items(item_factory: FlipwitchItemFactory, items: List[Item]):
    for item in costume_items:
        items.append(item_factory(item.name))
    return items


def create_filler(item_factory: FlipwitchItemFactory, filler_slots: int, items: List[Item]):
    if filler_slots == 0:
        return items
    items.extend([item_factory(filler) for filler in ["Nothing"]*filler_slots])
    return items


