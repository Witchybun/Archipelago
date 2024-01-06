from BaseClasses import ItemClassification, MultiWorld
from . import LunacidTestBase
from .. import Items
from ..Options import Shopsanity, Switchsanity


def get_real_locations(tester: LunacidTestBase, multiworld: MultiWorld):
    return [location for location in multiworld.get_locations(tester.player) if not location.event]


def get_real_location_names(tester: LunacidTestBase, multiworld: MultiWorld):
    return [location.name for location in multiworld.get_locations(tester.player) if not location.event]


class TestBaseItems(LunacidTestBase):

    def test_all_progression_items_are_added_to_the_pool(self):
        all_created_items = [item.name for item in self.multiworld.itempool]
        progression_items = [item for item in Items.base_table if item.classification is ItemClassification.progression]
        for progression_item in progression_items:
            with self.subTest(f"{progression_item.name}"):
                self.assertIn(progression_item.name, all_created_items)


class TestShopItems(LunacidTestBase):
    options = {
        Shopsanity.internal_name: Shopsanity.option_true
    }

    def test_all_progression_items_are_added_to_the_pool(self):
        all_created_items = [item.name for item in self.multiworld.itempool]
        shop_setting_table = [item for item in Items.base_table or Items.shop_table]
        progression_items = [item for item in shop_setting_table if item.classification is ItemClassification.progression]
        for progression_item in progression_items:
            with self.subTest(f"{progression_item.name}"):
                self.assertIn(progression_item.name, all_created_items)


class TestSwitchItems(LunacidTestBase):
    options = {
        Switchsanity.internal_name: Switchsanity.option_true
    }

    def test_all_progression_items_are_added_to_the_pool(self):
        all_created_items = [item.name for item in self.multiworld.itempool]
        switch_setting_table = [item for item in Items.base_table or Items.switch_table]
        progression_items = [item for item in switch_setting_table if item.classification is ItemClassification.progression]
        for progression_item in progression_items:
            with self.subTest(f"{progression_item.name}"):
                self.assertIn(progression_item.name, all_created_items)
