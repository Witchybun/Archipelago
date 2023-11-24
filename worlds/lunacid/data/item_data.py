from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import GenericItem, UniqueItem, Alchemy, Coins


@dataclass(frozen=True)
class Item(GameItem):
    id: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.id} {self.name} (Classification: {self.classification})"


all_items: List[Item] = []


def create_item(id: int, name: str, classification: ItemClassification):
    id = int
    item = Item(name, classification)
    all_items.append(item)
    return item


health_vial = create_item(1, GenericItem.health_vial, ItemClassification.filler)
mana_vial = create_item(2, GenericItem.mana_vial, ItemClassification.filler)
antidote = create_item(3, GenericItem.antidote, ItemClassification.filler)
blood_wine = create_item(4, GenericItem.blood_wine, ItemClassification.filler)
crystal_shard = create_item(5, GenericItem.crystal_shard, ItemClassification.filler)
ocean_elixir = create_item(6, UniqueItem.ocean_elixir, ItemClassification.useful)
earth_elixir = create_item(7, UniqueItem.earth_elixir, ItemClassification.useful)
poison_throwing_knife = create_item(8, GenericItem.poison_throwing_knife, ItemClassification.filler)
black_book = create_item(9, UniqueItem.black_book, ItemClassification.progression)
holy_water = create_item(10, GenericItem.holy_water, ItemClassification.filler)
fairy_moss = create_item(11, GenericItem.fairy_moss, ItemClassification.filler)
light_urn = create_item(12, GenericItem.light_urn, ItemClassification.filler)
ashes = create_item(13, GenericItem.ashes, ItemClassification.filler)
cloth_bandage = create_item(14, GenericItem.cloth_bandage, ItemClassification.filler)
moonlight_vial = create_item(15, GenericItem.moonlight_vial, ItemClassification.filler)
spectral_candle = create_item(16, GenericItem.spectral_candle, ItemClassification.filler)
dark_urn = create_item(17, GenericItem.dark_urn, ItemClassification.filler)
wisp_heart = create_item(18, GenericItem.wisp_heart, ItemClassification.filler)
staff_of_osiris = create_item(19, GenericItem.staff_of_osiris, ItemClassification.filler)
white_tape = create_item(20, UniqueItem.white_tape, ItemClassification.useful)
vhs_tape = create_item(21, UniqueItem.vhs_tape, ItemClassification.progression)
corrupted_key = create_item(22, UniqueItem.corrupted_key, ItemClassification.progression)
skull_of_josiah = create_item(23, UniqueItem.skull_of_josiah, ItemClassification.progression)
vampiric_symbol_w = create_item(24, UniqueItem.vampiric_symbol_w, ItemClassification.progression)
vampiric_symbol_a = create_item(25, UniqueItem.vampiric_symbol_a, ItemClassification.progression)
vampiric_symbol_e = create_item(26, UniqueItem.vampiric_symbol_e, ItemClassification.progression)
crystal_lantern = create_item(27, UniqueItem.crystal_lantern, ItemClassification.useful)
terminus_prison_key = create_item(28, UniqueItem.terminus_prison_key, ItemClassification.progression)
enchanted_key = create_item(29, UniqueItem.enchanted_key, ItemClassification.progression)
survey_banner = create_item(30, UniqueItem.survey_banner, ItemClassification.useful)
ectoplasm = create_item(31, Alchemy.ectoplasm, ItemClassification.filler)
snowflake_obsidian = create_item(32, Alchemy.snowflake_obsidian, ItemClassification.filler)
moonpetal = create_item(33, Alchemy.moonpetal, ItemClassification.filler)
fractured_life = create_item(34, Alchemy.fractured_life, ItemClassification.progression)
fractured_death = create_item(35, Alchemy.fractured_death, ItemClassification.progression)
broken_sword = create_item(36, Alchemy.broken_sword, ItemClassification.progression)
water_talisman = create_item(37, UniqueItem.water_talisman, ItemClassification.progression)
earth_talisman = create_item(38, UniqueItem.earth_talisman, ItemClassification.progression)
silver_5 = create_item(39, Coins.silver_5, ItemClassification.filler)
silver_10 = create_item(40, Coins.silver_2, ItemClassification.filler)
silver_50 = create_item(41, Coins.silver_50, ItemClassification.filler)
silver_100 = create_item(42, Coins.silver_100, ItemClassification.filler)
strange_coin = create_item(43, Coins.strange_coin, ItemClassification.progression)

item_light_sources = [UniqueItem.crystal_lantern]

all_item_data_by_name = {item.name: item for item in all_items}
all_filler_items = {item for item in all_items if item.classification == ItemClassification.filler}

