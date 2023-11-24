from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import GenericItem, UniqueItem, Alchemy, Coins


@dataclass(frozen=True)
class Item(GameItem):
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.name} (Classification: {self.classification})"


all_items: List[Item] = []


def create_item(name: str, classification: ItemClassification):
    item = Item(name, classification)
    all_items.append(item)
    return item


health_vial = create_item(GenericItem.health_vial, ItemClassification.filler)
mana_vial = create_item(GenericItem.mana_vial, ItemClassification.filler)
antidote = create_item(GenericItem.antidote, ItemClassification.filler)
blood_wine = create_item(GenericItem.blood_wine, ItemClassification.filler)
crystal_shard = create_item(GenericItem.crystal_shard, ItemClassification.filler)
ocean_elixir = create_item(UniqueItem.ocean_elixir, ItemClassification.useful)
earth_elixir = create_item(UniqueItem.earth_elixir, ItemClassification.useful)
poison_throwing_knife = create_item(GenericItem.poison_throwing_knife, ItemClassification.filler)
black_book = create_item(UniqueItem.black_book, ItemClassification.progression)
holy_water = create_item(GenericItem.holy_water, ItemClassification.filler)
fairy_moss = create_item(GenericItem.fairy_moss, ItemClassification.filler)
light_urn = create_item(GenericItem.light_urn, ItemClassification.filler)
ashes = create_item(GenericItem.ashes, ItemClassification.filler)
cloth_bandage = create_item(GenericItem.cloth_bandage, ItemClassification.filler)
moonlight_vial = create_item(GenericItem.moonlight_vial, ItemClassification.filler)
spectral_candle = create_item(GenericItem.spectral_candle, ItemClassification.filler)
dark_urn = create_item(GenericItem.dark_urn, ItemClassification.filler)
wisp_heart = create_item(GenericItem.wisp_heart, ItemClassification.filler)
staff_of_osiris = create_item(GenericItem.staff_of_osiris, ItemClassification.filler)
white_tape = create_item(UniqueItem.white_tape, ItemClassification.useful)
vhs_tape = create_item(UniqueItem.vhs_tape, ItemClassification.progression)
corrupted_key = create_item(UniqueItem.corrupted_key, ItemClassification.progression)
skull_of_josiah = create_item(UniqueItem.skull_of_josiah, ItemClassification.progression)
vampiric_symbol_w = create_item(UniqueItem.vampiric_symbol_w, ItemClassification.progression)
vampiric_symbol_a = create_item(UniqueItem.vampiric_symbol_a, ItemClassification.progression)
vampiric_symbol_e = create_item(UniqueItem.vampiric_symbol_e, ItemClassification.progression)
crystal_lantern = create_item(UniqueItem.crystal_lantern, ItemClassification.useful)
terminus_prison_key = create_item(UniqueItem.terminus_prison_key, ItemClassification.progression)
enchanted_key = create_item(UniqueItem.enchanted_key, ItemClassification.progression)
survey_banner = create_item(UniqueItem.survey_banner, ItemClassification.useful)
ectoplasm = create_item(Alchemy.ectoplasm, ItemClassification.filler)
snowflake_obsidian = create_item(Alchemy.snowflake_obsidian, ItemClassification.filler)
moonpetal = create_item(Alchemy.moonpetal, ItemClassification.filler)
fractured_life = create_item(Alchemy.fractured_life, ItemClassification.progression)
fractured_death = create_item(Alchemy.fractured_death, ItemClassification.progression)
broken_sword = create_item(Alchemy.broken_sword, ItemClassification.progression)
water_talisman = create_item(UniqueItem.water_talisman, ItemClassification.progression)
earth_talisman = create_item(UniqueItem.earth_talisman, ItemClassification.progression)
silver_5 = create_item(Coins.silver_5, ItemClassification.filler),
silver_10 = create_item(Coins.silver_2, ItemClassification.filler)
silver_100 = create_item(Coins.silver_100, ItemClassification.filler)

item_light_sources = [UniqueItem.crystal_lantern]

all_items_by_name = {item.name: item for item in all_items}

