from dataclasses import dataclass
from typing import List

from BaseClasses import ItemClassification
from worlds.uktena64.strings.items import JebItem, BaseItem, JebCampaignItem, JeebItem, JeebCampaignItem, PhotoItem, MeatItem


@dataclass(frozen=True)
class UktenaItemData:
    code: int
    name: str
    classification: ItemClassification

    def __repr__(self):
        return f"{self.code} {self.name} (Classification: {self.classification})"

all_items: List[UktenaItemData] = []

def create_item(code: int, name: str, classification: ItemClassification) -> UktenaItemData:
    item = UktenaItemData(code, name, classification)
    all_items.append(item)

    return item

base_items = [
    create_item(1, BaseItem.instant_coffee, ItemClassification.useful),
    create_item(2, BaseItem.stim, ItemClassification.filler),
    create_item(3, BaseItem.nothing, ItemClassification.filler),
    create_item(4, BaseItem.jeb_campaign, ItemClassification.progression),
    create_item(5, BaseItem.jeeb_campaign, ItemClassification.progression),
]

jeb_base_item_code = 10
jeb_base_items = [
    create_item(jeb_base_item_code + 1, JebItem.knife, ItemClassification.progression),
    create_item(jeb_base_item_code + 2, JebItem.rifle, ItemClassification.progression),
    create_item(jeb_base_item_code + 3, JebItem.camera, ItemClassification.progression),
    create_item(jeb_base_item_code + 4, JebItem.turkey_call, ItemClassification.progression),
    create_item(jeb_base_item_code + 5, JebItem.revolver, ItemClassification.progression),
    create_item(jeb_base_item_code + 6, JebItem.bren_lmg, ItemClassification.progression),
    create_item(jeb_base_item_code + 7, JebItem.starting_rifle_ammo, ItemClassification.useful),
    create_item(jeb_base_item_code + 8, JebItem.starting_revolver_ammo, ItemClassification.useful),
    create_item(jeb_base_item_code + 9, JebCampaignItem.creek, ItemClassification.progression),
    create_item(jeb_base_item_code + 10, JebCampaignItem.frigid_valley, ItemClassification.progression),
    create_item(jeb_base_item_code + 11, JebCampaignItem.howling_marsh, ItemClassification.progression),
    create_item(jeb_base_item_code + 12, JebItem.church_key, ItemClassification.progression)
]

jeeb_base_item_code = 30
jeeb_base_items = [
    create_item(jeeb_base_item_code + 1, JeebItem.butcher_knives, ItemClassification.progression),
    # create_item(jeeb_base_item_code + 2, JeebItem.binoculars, ItemClassification.progression),
    create_item(jeeb_base_item_code + 3, JeebItem.ruger, ItemClassification.progression),
    create_item(jeeb_base_item_code + 4, JeebItem.bear_trap, ItemClassification.progression),
    create_item(jeeb_base_item_code + 5, JeebItem.crossbow, ItemClassification.progression),
    create_item(jeeb_base_item_code + 6, JeebItem.banjo, ItemClassification.progression),
    create_item(jeeb_base_item_code + 7, JeebItem.starting_ruger_ammo, ItemClassification.useful),
    create_item(jeeb_base_item_code + 8, JeebItem.starting_crossbow_bolts, ItemClassification.useful),
    create_item(jeeb_base_item_code + 9, JeebItem.starting_bear_traps, ItemClassification.useful),
    create_item(jeeb_base_item_code + 10, JeebCampaignItem.ritual_road, ItemClassification.progression),
    create_item(jeeb_base_item_code + 11, JeebCampaignItem.lake_linger, ItemClassification.progression),
    create_item(jeeb_base_item_code + 12, JeebCampaignItem.pallid_park, ItemClassification.progression),
]

jeb_photo_item_code = 50
jeb_photo_items = [
    create_item(jeb_photo_item_code + 1, PhotoItem.cabin, ItemClassification.progression_deprioritized),
    create_item(jeb_photo_item_code + 2, PhotoItem.turkey, ItemClassification.progression_deprioritized),
    create_item(jeb_photo_item_code + 3, PhotoItem.frigid_valley, ItemClassification.progression_deprioritized),
    create_item(jeb_photo_item_code + 4, PhotoItem.howling_marsh, ItemClassification.progression_deprioritized),
    create_item(jeb_photo_item_code + 5, PhotoItem.bleeding_grove, ItemClassification.progression_deprioritized),
]

jeeb_meat_item_code = 70
jeeb_meat_items = [
    create_item(jeeb_meat_item_code + 1, MeatItem.bbq, ItemClassification.progression_deprioritized),
    create_item(jeeb_meat_item_code + 2, MeatItem.ritual, ItemClassification.progression_deprioritized),
    create_item(jeeb_meat_item_code + 3, MeatItem.lake, ItemClassification.progression_deprioritized),
    create_item(jeeb_meat_item_code + 4, MeatItem.pallid, ItemClassification.progression_deprioritized),
    create_item(jeeb_meat_item_code + 5, MeatItem.burning, ItemClassification.progression_deprioritized),
]

hyena_doll_item_code = 80
hyena_doll_items = [
    create_item(hyena_doll_item_code + 1, BaseItem.hyena, ItemClassification.progression_deprioritized),
]