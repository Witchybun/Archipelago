from dataclasses import dataclass
from typing import List
from BaseClasses import ItemClassification

from .game_item import GameItem
from ..strings.items import GenericItem, UniqueItem, Alchemy, Coins, Creation, Progressives, RareDrops, UnusedItems


@dataclass(frozen=True)
class GeneralItem(GameItem):
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.code} {self.name} (Classification: {self.classification})"


all_items: List[GeneralItem] = []


def create_item(code: int, name: str, classification: ItemClassification):
    item = GeneralItem(name, code, classification)
    all_items.append(item)

    return item


health_vial = create_item(1, Creation.health_vial, ItemClassification.filler)
mana_vial = create_item(2, Creation.mana_vial, ItemClassification.filler)
antidote = create_item(3, Creation.antidote, ItemClassification.filler)
blood_wine = create_item(4, GenericItem.blood_wine, ItemClassification.filler)
crystal_shard = create_item(5, Creation.crystal_shard, ItemClassification.filler)
ocean_elixir = create_item(6, UniqueItem.ocean_elixir, ItemClassification.useful)
earth_elixir = create_item(7, UniqueItem.earth_elixir, ItemClassification.useful)
poison_throwing_knife = create_item(8, Creation.poison_throwing_knife, ItemClassification.filler)
black_book = create_item(9, UniqueItem.black_book, ItemClassification.progression)
holy_water = create_item(10, Creation.holy_water, ItemClassification.filler)
fairy_moss = create_item(11, Creation.fairy_moss, ItemClassification.filler)
light_urn = create_item(12, GenericItem.light_urn, ItemClassification.filler)
ashes = create_item(13, Alchemy.ashes, ItemClassification.filler)
cloth_bandage = create_item(14, GenericItem.cloth_bandage, ItemClassification.filler)
moonlight_vial = create_item(15, Creation.moonlight_vial, ItemClassification.filler)
spectral_candle = create_item(16, Creation.spectral_candle, ItemClassification.filler)
dark_urn = create_item(17, GenericItem.dark_urn, ItemClassification.filler)
wisp_heart = create_item(18, Creation.wisp_heart, ItemClassification.filler)
staff_of_osiris = create_item(19, Creation.staff_of_osiris, ItemClassification.filler)
white_tape = create_item(20, UniqueItem.white_tape, ItemClassification.useful)
vhs_tape = create_item(21, UniqueItem.vhs_tape, ItemClassification.progression)
corrupted_key = create_item(22, UniqueItem.corrupted_key, ItemClassification.progression)
skull_of_josiah = create_item(23, UniqueItem.skull_of_josiah, ItemClassification.progression)
vampiric_symbol = create_item(24, Progressives.vampiric_symbol, ItemClassification.progression)
crystal_lantern = create_item(27, UniqueItem.crystal_lantern, ItemClassification.useful)
terminus_prison_key = create_item(28, UniqueItem.terminus_prison_key, ItemClassification.progression)
enchanted_key = create_item(29, UniqueItem.enchanted_key, ItemClassification.progression)
survey_banner = create_item(30, UniqueItem.survey_banner, ItemClassification.filler)
ectoplasm = create_item(31, Alchemy.ectoplasm, ItemClassification.filler)
snowflake_obsidian = create_item(32, Alchemy.snowflake_obsidian, ItemClassification.filler)
moon_petal = create_item(33, Alchemy.moon_petal, ItemClassification.filler)
fractured_life = create_item(34, Alchemy.fractured_life, ItemClassification.progression)
fractured_death = create_item(35, Alchemy.fractured_death, ItemClassification.progression)
broken_sword = create_item(36, Alchemy.broken_sword, ItemClassification.progression)
water_talisman = create_item(37, UniqueItem.water_talisman, ItemClassification.progression)
earth_talisman = create_item(38, UniqueItem.earth_talisman, ItemClassification.progression)
strange_coin = create_item(39, Coins.strange_coin, ItemClassification.useful)
oil_lantern = create_item(40, UniqueItem.oil_lantern, ItemClassification.progression)
bomb = create_item(41, Creation.bomb, ItemClassification.filler)
poison_urn = create_item(42, Creation.poison_urn, ItemClassification.filler)
silver = create_item(43, Coins.silver, ItemClassification.filler)
skeleton_egg = create_item(44, UniqueItem.skeleton_egg, ItemClassification.progression)
dried_rat = create_item(45, UniqueItem.dried_rat, ItemClassification.useful)
dusty_crystal_orb = create_item(46, UniqueItem.dusty_crystal_orb, ItemClassification.useful)
skeleton_rattle = create_item(47, UniqueItem.skeleton_rattle, ItemClassification.useful)
shrimp = create_item(48, RareDrops.shrimp, ItemClassification.filler)
angel_feather = create_item(49, RareDrops.angel_feather, ItemClassification.filler)
tent = create_item(50, UnusedItems.tent, ItemClassification.useful)
fire_opal = create_item(51, Alchemy.fire_opal, ItemClassification.filler)
lotus_seed_pod = create_item(52, Alchemy.lotus_seed_pod, ItemClassification.filler)
onyx = create_item(53, Alchemy.onyx, ItemClassification.filler)
destroying_angel_mushroom = create_item(54, Alchemy.destroying_angel_mushroom, ItemClassification.filler)
ocean_bone_shard = create_item(55, Alchemy.ocean_bone_shard, ItemClassification.filler)
ocean_bone_shell = create_item(56, Alchemy.ocean_bone_shell, ItemClassification.filler)
yellow_morel = create_item(57, Alchemy.yellow_morel, ItemClassification.filler)
bloodweed = create_item(58, Alchemy.bloodweed, ItemClassification.filler)
opal = create_item(59, Alchemy.opal, ItemClassification.filler)
obsidian = create_item(60, Alchemy.obsidian, ItemClassification.filler)
ikurrilb_root = create_item(61, Alchemy.ikurrilb_root, ItemClassification.filler)


item_light_sources = [UniqueItem.crystal_lantern, UniqueItem.oil_lantern]
money = [silver]

all_item_data_by_name = {item.name: item for item in all_items}
all_filler_items = {item for item in all_items if item.classification == ItemClassification.filler}
max_item_count_by_item = {
    black_book: 3,
    earth_talisman: 1,
    water_talisman: 1,
    fractured_death: 1,
    fractured_life: 1,
    white_tape: 1,
    vhs_tape: 1,
    skull_of_josiah: 1,
    crystal_lantern: 1,
    broken_sword: 1,
    strange_coin: 3,
    terminus_prison_key: 1,
    enchanted_key: 2,
    corrupted_key: 1,
    vampiric_symbol: 3,
}
