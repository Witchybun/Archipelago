from dataclasses import dataclass
from BaseClasses import ItemClassification
from random import Random
from typing import Optional, Dict, List, Protocol, Union
from .data.location_data import base_locations, shop_locations, LocationData
from .data.item_data import all_item_data_by_name, all_filler_items, Item
from .strings.items import UniqueItem
from .Options import LunacidOptions

ITEM_CODE_START = 771111110


@dataclass(frozen=True)
class ItemDict:
    code: Optional[int]
    name: str
    classification: ItemClassification


all_locations = base_locations + shop_locations


class LunacidItemFactory(Protocol):
    def __call__(self, name: Union[str, ItemDict], override_classification: ItemClassification = None) -> Item:
        raise NotImplementedError


def create_items_and_counts(locations: List[LocationData]):
    item_data_list: List[Item] = []
    item_count: Dict[str, int] = {}
    for location in locations:
        item_name = location.original_item
        item_data = all_item_data_by_name[item_name]
        if item_data in item_data_list:
            item_count[item_data] += 1
            continue
        item_data_list.append(item_data)
        item_count[item_data] = 1
    return [ItemDict(item_data.id, item_data.name, item_data.classification) for item_data in item_data_list], item_count


all_items_and_count = create_items_and_counts(all_locations)
all_items = all_items_and_count[0]
all_filler = [item for item in all_items if item.classification is ItemClassification.filler]


def extend_items_by_locations(item_factory: LunacidItemFactory, options: LunacidOptions, locations: List[LocationData], incoming_items: List[Item],
                              random: Random):
    items_and_counts = create_items_and_counts(locations)
    items_no_counts = items_and_counts[0]
    base_counts = items_and_counts[1]
    for item_data in items_no_counts:
        if item_data.classification is not ItemClassification.filler:
            incoming_items.append(item_factory(item_data.name))
        if options.fillershuffle == options.fillershuffle.option_shuffled:
            incoming_items.extend(item_factory(item) for item in [item_data.name] * base_counts[item_data.name])
        elif options.fillershuffle == options.fillershuffle.option_random:
            random_filler = random.choice(all_filler)
            incoming_items.append(item_factory(random_filler))


def create_items(item_factory: LunacidItemFactory, options: LunacidOptions, random: Random):
    items = []
    extend_items_by_locations(item_factory, options, base_locations, items, random)
    if options.shopsanity == options.shopsanity.option_true:
        extend_items_by_locations(item_factory, options, shop_locations, items, random)
    return items


group_table: Dict[str, List[str]] = {
    "vampiric symbol": [UniqueItem.vampiric_symbol_a, UniqueItem.vampiric_symbol_e, UniqueItem.vampiric_symbol_w],

    "vhs": [UniqueItem.vhs_tape, UniqueItem.white_tape],

    "talisman": [UniqueItem.earth_talisman, UniqueItem.water_talisman]
}
