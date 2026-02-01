from random import Random
from typing import List

from BaseClasses import Item
from worlds.uktena64.data.items import all_items, UktenaItemData, jeb_base_items, jeeb_base_items
from worlds.uktena64.options import UktenaOptions
from worlds.uktena64.strings.items import JebItem, JeebItem, BaseItem, PhotoItem, MeatItem

def initialize_items_by_name() -> List[UktenaItemData]:
    items = []
    for item in all_items:
        items.append(item)
    return items

item_table = initialize_items_by_name()
complete_items_by_name = {item.name: item for item in item_table}

def create_items(item_factory, exclude: List[Item], options: UktenaOptions, random: Random, location_count: int):
    items = []
    uktena_items = create_uktena_items(item_factory, options, random, items)
    for uktena_item in exclude:
        if uktena_item in uktena_items:
            uktena_items.remove(uktena_item)
    assert len(
        uktena_items) <= location_count, f"There should be at least as many locations [{location_count}] as there are mandatory items [{len(uktena_items)}]"
    filler_slots = location_count - len(items)
    create_filler(item_factory, filler_slots, random, items)
    return items

def create_uktena_items(item_factory, options: UktenaOptions, random: Random, items: List[Item]) -> List[Item]:
    create_base_items(item_factory, options, items)
    create_jeb_items(item_factory, options, items)
    create_jeeb_items(item_factory, options, items)
    create_photo_items(item_factory, options, items)
    create_meat_items(item_factory, options, items)
    if options.hyenas:
        items.extend([item_factory(hyena) for hyena in [BaseItem.hyena]*5])
    return items

def create_base_items(item_factory, options: UktenaOptions, items: List[Item]):
    coffee_count = 0
    if options.campaign != options.campaign.option_jeeb:
        coffee_count += 5
    if options.campaign != options.campaign.option_jebidiah:
        coffee_count += 5
    items.extend([item_factory(coffee) for coffee in [BaseItem.instant_coffee]*coffee_count])
    return items

def create_jeb_items(item_factory, options: UktenaOptions, items: List[Item]):
    if options.campaign == options.campaign.option_jeeb:
        return items
    for item in jeb_base_items:
        if item.name == JebItem.starting_rifle_ammo:
            items.extend([item_factory(ammo) for ammo in [JebItem.starting_rifle_ammo]*7])
            continue
        if item.name == JebItem.starting_revolver_ammo:
            items.extend([item_factory(ammo) for ammo in [JebItem.starting_revolver_ammo]*7])
            continue
        if item.name == JebItem.camera and not options.randomize_camera_knife:
            continue
        items.append(item_factory(item.name))
    return items

def create_jeeb_items(item_factory, options: UktenaOptions, items: List[Item]):
    if options.campaign == options.campaign.option_jebidiah:
        return items
    for item in jeeb_base_items:
        if item.name == JeebItem.starting_ruger_ammo:
            items.extend([item_factory(ammo) for ammo in [JeebItem.starting_ruger_ammo] * 7])
            continue
        if item.name == JeebItem.starting_bear_traps:
            items.extend([item_factory(ammo) for ammo in [JeebItem.starting_bear_traps] * 7])
            continue
        if item.name == JeebItem.starting_crossbow_bolts:
            items.extend([item_factory(ammo) for ammo in [JeebItem.starting_crossbow_bolts] * 7])
            continue
        if item.name == JeebItem.butcher_knives and not options.randomize_camera_knife:
            continue
        items.append(item_factory(item.name))
    return items

def create_photo_items(item_factory, options: UktenaOptions, items: List[Item]):
    if not options.photographer or options.campaign == options.campaign.option_jeeb:
        return items
    items.append(item_factory(PhotoItem.cabin))
    items.extend([item_factory(photo) for photo in [PhotoItem.turkey]*10])
    items.extend([item_factory(photo) for photo in [PhotoItem.frigid_valley]*13])
    items.extend([item_factory(photo) for photo in [PhotoItem.howling_marsh]*6])
    items.append(item_factory(PhotoItem.bleeding_grove))
    return items

def create_meat_items(item_factory, options: UktenaOptions, items: List[Item]):
    if not options.bbq_chef or options.campaign == options.campaign.option_jebidiah:
        return items
    items.append(item_factory(MeatItem.bbq))
    items.extend([item_factory(meat) for meat in [MeatItem.ritual]*10])
    items.extend([item_factory(meat) for meat in [MeatItem.lake]*16])
    items.extend([item_factory(meat) for meat in [MeatItem.pallid]*9])
    items.extend([item_factory(meat) for meat in [MeatItem.burning]*7])
    return items

def create_filler(item_factory, filler_count: int, random: Random, items: List[Item]):
    items.extend([item_factory(stim) for stim in [BaseItem.stim]*filler_count])
    return items
