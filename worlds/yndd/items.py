from random import Random
import logging

from BaseClasses import ItemClassification, Item
from typing import Dict, List, Union, Protocol

from .options import DreamOptions
from .data.items import (all_items, DreamItemData, base_items, nasu_items, ao_oni_items, witch_adventure_items,
                         song_items, connector_items)
from .strings.items import SchoolItem, DockItem, Filler, NasuItem, WitchAdventureItem, NexusDoors, Movement, GoalItems, \
    BlockItem

logger = logging.getLogger(__name__)


class DreamItemFactory(Protocol):
    def __call__(self, name: Union[str, DreamItemData], override_classification: ItemClassification = None) -> Item:
        raise NotImplementedError


def initialize_items_by_name() -> List[DreamItemData]:
    items = []
    for item in all_items:
        items.append(item)
    return items


item_table = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in item_table}

def create_items(item_factory: DreamItemFactory, locations_count: int, items_to_exclude: List[Item],
                 doors: Dict[str, bool], options: DreamOptions, random: Random) -> List[Item]:
    items = []
    dream_items = create_dream_items(item_factory, doors, options)
    for item in items_to_exclude:
        if item in dream_items:
            dream_items.remove(item)
    assert len(
        dream_items) <= locations_count, (f"There should be at least as many locations [{locations_count}] "
                                            f"as there are mandatory items [{len(dream_items)}]")
    items += dream_items

    logger.debug(f"Created {len(dream_items)} unique items")
    filler_slots = locations_count - len(items)
    create_filler(item_factory, options, random, filler_slots, items)

    return items

def create_dream_items(item_factory, doors: Dict[str, bool], options: DreamOptions):
    items = []
    create_base_items(item_factory, options, items)
    create_game_items(item_factory, options, items)
    create_locked_door_items(item_factory, doors, options, items)
    create_movement_items(item_factory, options, items)
    create_song_items(item_factory, options, items)
    return items

def create_base_items(item_factory, options: DreamOptions, items: List[Item]) -> List[Item]:
    for item in base_items:
        if item.name in GoalItems.eggs:
            if "Eggs" in options.local_goals.value:
                continue
        if item.name in GoalItems.jellyfish:
            if "Jellyfish" in options.local_goals.value:
                continue
        if item.name == SchoolItem.photo:
            items.extend([item_factory(picture) for picture in [SchoolItem.photo]*4])
            continue
        if item.name == DockItem.yen:
            items.extend([item_factory(coin) for coin in [DockItem.yen]*10])
            continue
        if item.name == BlockItem.girl:
            items.extend([item_factory(girl) for girl in [item.name]*6])
            continue
        if item.name == Filler.nothing:
            continue
        items.append(item_factory(item.name))
    return items

def create_game_items(item_factory, options: DreamOptions, items: List[Item]) -> List[Item]:
    if "Nasu" in options.randomize_console.value:
        for item in nasu_items:
            if item.name == NasuItem.starting_points:
                items.extend([item_factory(points) for points in [NasuItem.starting_points]*4])
                continue
            items.append(item_factory(item.name))
    if "Ao Oni" in options.randomize_console.value:
        for item in ao_oni_items:
            items.extend([item_factory(demon) for demon in [item.name]*5])
    if "Witch Adventure" in options.randomize_console.value:
        for item in witch_adventure_items:
            if item.name == WitchAdventureItem.heart_container:
                items.extend([item_factory(heart) for heart in [item.name]*4])
                continue
            items.append(item_factory(item.name))
    return items

def create_locked_door_items(item_factory, doors: Dict[str, bool], options: DreamOptions, items: List[Item]) -> List[Item]:
    for door in doors:
        if doors[door]:
            continue
        items.append(item_factory(NexusDoors.door_to_key[door]))
    if options.lock_connectors:
        for key in connector_items:
            items.append(item_factory(key.name))
    return items

def create_movement_items(item_factory, options: DreamOptions, items: List[Item]) -> List[Item]:
    basic_movement = ["Jump", "Climb", "Run"]
    for mov in basic_movement:
        if mov not in options.starting_basic_movement.value:
            items.append(item_factory(Movement.movement_to_item[mov]))
    return items

def create_song_items(item_factory, options: DreamOptions, items: List[Item]) -> List[Item]:
    if not options.song_lock:
        return items
    for song in song_items:
        items.append(item_factory(song.name))
    return items

def create_filler(item_factory, options: DreamOptions, random: Random, filler_slots: int, items: List[Item]) -> List[Item]:
    filler_count = filler_slots
    if filler_count == 0:
        return items
    # For now there's no other filler.
    items.extend(item_factory(filler) for filler in [Filler.nothing]*filler_count)
    return items
