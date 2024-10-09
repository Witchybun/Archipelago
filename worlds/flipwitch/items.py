from random import Random
import logging

from BaseClasses import ItemClassification, Item
from typing import Dict, List, Union, Protocol

from worlds.flipwitch import FlipwitchOptions
from worlds.flipwitch.data.items import FlipwitchItemData, all_items, base_items, gacha_items, filler_items
from worlds.flipwitch.strings.items import Coin, Upgrade, Goal, QuestItem

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


def create_items(item_factory: FlipwitchItemFactory, locations_count: int, items_to_exclude: List[Item], options: FlipwitchOptions, random: Random) -> List[Item]:
    items = []
    flipwitch_items = create_flipwitch_items(item_factory, options)
    for item in items_to_exclude:
        if item in flipwitch_items:
            flipwitch_items.remove(item)
    assert len(
        flipwitch_items) <= locations_count, f"There should be at least as many locations [{locations_count}] as there are mandatory items [{len(flipwitch_items)}]"
    items += flipwitch_items
    logger.debug(f"Created {len(flipwitch_items)} unique items")
    filler_slots = locations_count - len(items)
    create_filler(item_factory, random, filler_slots, items)

    return items


def create_flipwitch_items(item_factory: FlipwitchItemFactory, options: FlipwitchOptions) -> List[Item]:
    items = []
    create_base_items(item_factory, options, items)
    create_gacha_items(item_factory, options, items)
    return items


def create_base_items (item_factory: FlipwitchItemFactory, options: FlipwitchOptions, items: List[Item]):
    for item in base_items:
        if item.name == Upgrade.health or item.name == Upgrade.mana:
            upgrade_name = item.name
            items.extend([item_factory(stat) for stat in [upgrade_name]*10])
        elif item.name == Upgrade.peachy_peach:
            items.extend([item_factory(peach) for peach in [Upgrade.peachy_peach]*11])
        elif item.name == Upgrade.wand:
            items.extend([item_factory(weapon) for weapon in [Upgrade.wand]*3])
        elif item.name == Goal.chaos_piece and options.shuffle_chaos_pieces == options.shuffle_chaos_pieces.option_true:
            items.extend([item_factory(piece) for piece in [Goal.chaos_piece]*6])
        elif item.name == QuestItem.summon_stone:
            items.extend([item_factory(stone) for stone in [QuestItem.summon_stone]*3])
        elif item.name == QuestItem.soul_fragment:
            items.extend([item_factory(soul) for soul in [QuestItem.soul_fragment]*3])
        elif item.name == Coin.lucky_coin:
            items.extend(item_factory(lucky) for lucky in [Coin.lucky_coin]*44)
        else:
            items.append(item_factory(item.name))
    return items


def create_gacha_items(item_factory: FlipwitchItemFactory, options: FlipwitchOptions, items: List[Item]):
    if options.gachapon == options.gachapon.option_false:
        return items
    for item in gacha_items:
        items.append(item_factory(item.name))
    return items


def create_filler(item_factory: FlipwitchItemFactory, random: Random, filler_slots: int, items: List[Item]):
    if filler_slots == 0:
        return items
    filler_list = [item.name for item in filler_items]
    items.extend([item_factory(filler) for filler in random.choices(filler_list, k=filler_slots)])
    return items


