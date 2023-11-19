from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import GenericItem, UniqueItem
from ..strings.regions_entrances import Region


@dataclass(frozen=True)
class Item(GameItem):
    name: str
    unique: bool
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Unique: {self.unique} |" \
               f"(Classification: {self.classification})"


all_items: List[Item] = []


def create_item(name: str, unique: bool, classification: ItemClassification):
    item = Item(name, unique, classification)
    all_items.append(item)
    return item


health_vial = create_item(GenericItem.health_vial, False, ItemClassification.filler)
mana_vial = create_item(GenericItem.mana_vial, False, ItemClassification.filler)
antidote = create_item(GenericItem.antidote, False, ItemClassification.filler)
blood_wine = create_item(GenericItem.blood_wine, False, ItemClassification.filler)
crystal_shard = create_item(GenericItem.crystal_shard, False, ItemClassification.filler)
ocean_elixir = create_item(GenericItem.ocean_elixir, False, ItemClassification.useful)
earth_elixir = create_item(GenericItem.earth_elixir, False, ItemClassification.useful)
poison_throwing_knife = create_item(GenericItem.poison_throwing_knife, False, ItemClassification.filler)
black_book = create_item(GenericItem.black_book, False, ItemClassification.progression)
holy_water = create_item(GenericItem.holy_water, False, ItemClassification.filler)
fairy_moss = create_item(GenericItem.fairy_moss, False, ItemClassification.filler)
light_urn = create_item(GenericItem.light_urn, False, ItemClassification.filler)
ashes = create_item(GenericItem.ashes, False, ItemClassification.filler)
cloth_bandage = create_item(GenericItem.cloth_bandage, False, ItemClassification.filler)
moonlight_vial = create_item(GenericItem.moonlight_vial, False, ItemClassification.filler)
spectral_candle = create_item(GenericItem.spectral_candle, False, ItemClassification.filler)
dark_urn = create_item(GenericItem.dark_urn, False, ItemClassification.filler)
wisp_heart = create_item(GenericItem.wisp_heart, False, ItemClassification.filler)
staff_of_osiris = create_item(GenericItem.staff_of_osiris, False, ItemClassification.filler)
white_tape = create_item(UniqueItem.white_tape, True, ItemClassification.useful)
vhs_tape = create_item(UniqueItem.vhs_tape, True, ItemClassification.progression)
corrupted_key = create_item(UniqueItem.corrupted_key, True, ItemClassification.progression)
skull_of_josiah = create_item(UniqueItem.skull_of_josiah, True, ItemClassification.progression)
vampiric_symbol_w = create_item(UniqueItem.vampiric_symbol_w, True, ItemClassification.progression)
vampiric_symbol_a = create_item(UniqueItem.vampiric_symbol_a, True, ItemClassification.progression)
vampiric_symbol_e = create_item(UniqueItem.vampiric_symbol_e, True, ItemClassification.progression)
crystal_lantern = create_item(UniqueItem.crystal_lantern, True, ItemClassification.useful)
terminus_prison_key = create_item(UniqueItem.terminus_prison_key, True, ItemClassification.progression)
enchanted_key = create_item(GenericItem.enchanted_key, False, ItemClassification.progression)

options_item_count = {
    "Base": {
        health_vial: 6 + 1 + 4 + 2 + 2 + 1 + 3 + 2 + 1 + 2 + 3 + 1,
        mana_vial: 1,
        antidote: 1,
        blood_wine: 1,
        crystal_shard: 1,
        ocean_elixir: 1,
        earth_elixir: 1,
        poison_throwing_knife: 1,
        black_book: 3,
        holy_water: 1,
        fairy_moss: 1,
        light_urn: 1,
        ashes: 1,
        cloth_bandage: 1,
        moonlight_vial: 3,
        spectral_candle: 2,
        dark_urn: 1,
        wisp_heart: 1,
        staff_of_osiris: 1,
        enchanted_key: 1

    }
}