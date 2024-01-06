from typing import Dict, List, Any
from collections import Counter
from BaseClasses import Region, Entrance, Location, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from . import Options
from .data.location_data import shop_items, base_items, switch_items, drop_items
from .data.item_data import money, max_item_count_by_item, all_item_data_by_name
from .strings.items import Creation
from .strings.weapons import Weapon
from .strings.options import Endings, Victory, Settings
from .strings.regions_entrances import LunacidRegion
from .strings.locations import BaseLocation
from .Items import item_table, item_table_by_setting_by_name, complete_items_by_name, group_table, ITEM_CODE_START
from .Locations import (location_table, base_location_table, shop_locations_table, switch_locations_table, mob_drop_locations_table, LocationDict,
                        LOCATION_CODE_START)
from .Regions import link_lunacid_areas, lunacid_entrances, lunacid_regions
from .Rules import set_rules, has_every_spell
from worlds.generic.Rules import set_rule
from .Options import LunacidOptions


class LunacidItem(Item):
    game: str = "Lunacid"


class LunacidWeb(WebWorld):
    theme = "partyTime"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Lunacid randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Albrekka"]
    )]


class LunacidWorld(World):
    """
    Lunacid is a first person dungeon crawler inspired by old FROMSOFT games like Shadow Tower and King’s Field.

    Long ago a great beast arose from the sea and covered the earth in a poison fog. Now those deemed undesirable
    are thrown into a great well, which has become a pit of chaos and disease. You awaken in a moonlit subterranean world,
    having been thrown into the Great Well for crimes unknown. The only way out is to go further down and confront the
    sleeping old one below. On the way there will be many creatures and secrets to discover.
    """

    game = "Lunacid"
    topology_present = False
    item_name_to_id = {item.name: (ITEM_CODE_START + index) for index, item in enumerate(item_table)}
    location_name_to_id = {loc.name: (LOCATION_CODE_START + index) for index, loc in enumerate(location_table)}

    data_version = 0
    required_client_version = (0, 4, 3)

    options_dataclass = LunacidOptions
    options: LunacidOptions
    item_name_groups = group_table

    web = LunacidWeb()

    def __init__(self, multiworld, player):
        super(LunacidWorld, self).__init__(multiworld, player)

    def set_rules(self):
        set_rules(self)

    def create_item(self, name: str) -> "LunacidItem":
        item_id: int = self.item_name_to_id[name]
        original_id = item_id - ITEM_CODE_START

        return LunacidItem(name, item_table[original_id].classification, item_id, player=self.player)

    def create_event(self, event: str):
        return Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(money)

    def create_regions(self):
        world = self.multiworld
        player = self.player

        def lunacid_region(region_name: str, entrances):
            single_region = Region(region_name, player, world)
            for entrance in entrances:
                single_region.exits.append(Entrance(player, entrance, single_region))
            return single_region

        world.regions += [lunacid_region(*r) for r in lunacid_regions]
        link_lunacid_areas(world, player)

        for index, location in enumerate(location_table):
            if location in shop_locations_table and self.options.shopsanity == self.options.shopsanity.option_false:
                continue
            if location in switch_locations_table and self.options.switchsanity == self.options.switchsanity.option_false:
                continue
            if location in mob_drop_locations_table and self.options.dropsanity == self.options.dropsanity.option_false:
                continue
            region: Region = world.get_region(location.region, player)
            region.add_locations({location.name: index})

        ending_region = world.get_region(LunacidRegion.grave_of_the_sleeper, player)
        throne_region = world.get_region(LunacidRegion.throne_chamber, player)
        crilall = Location(player, "Throne of Prince Crilall Fanu", None, throne_region)
        crilall.place_locked_item(self.create_event("Defeat Prince Crilall Fanu"))
        throne_region.locations.append(crilall)

        if self.options.ending == self.options.ending.option_ending_cd:
            victory = Location(player, Endings.look_into_abyss, None, ending_region)
        else:
            victory = Location(player, Endings.wake_dreamer, None, ending_region)
        victory.place_locked_item(self.create_event(Victory.victory))
        ending_region.locations.append(victory)

        if self.options.ending == self.options.ending.option_ending_e:
            set_rule(victory, lambda state: has_every_spell(state, player))

        world.completion_condition[self.player] = lambda state: state.has("Victory", player)

    def create_items(self):
        world = self.multiworld
        player = self.player

        skipped_items = []
        event_items_count = 2  # Due to how items are constructed, this is used to denote how many extra items were added due to events

        for item, count in world.start_inventory[player].value.items():
            item_name = complete_items_by_name[item]
            max_count = 1
            if item_name in all_item_data_by_name:
                max_count = max_item_count_by_item[item_name]
            if count > max_count:
                count = max_item_count_by_item[item_name]
            for _ in range(count):
                skipped_items.append(item)
            skipped_items.append(Weapon.lucid_blade)

        counter = Counter(skipped_items)
        pool = []

        for original_item in base_items:
            item = item_table_by_setting_by_name[Settings.base][original_item]
            count = item.count - counter[item.name]

            if count <= 0:
                continue
            else:
                for i in range(count):
                    pool.append(self.create_item(item.name))

        if self.options.shopsanity == self.options.shopsanity.option_true:
            for original_item in shop_items:
                item = item_table_by_setting_by_name[Settings.shopsanity][original_item]
                count = item.count - counter[item.name]

                if count <= 0:
                    continue
                else:
                    for i in range(count):
                        pool.append(self.create_item(item.name))

        if self.options.switchsanity == self.options.switchsanity.option_true:
            for original_item in switch_items:
                item = item_table_by_setting_by_name[Settings.switch_shuffle][original_item]
                count = item.count - counter[item.name]

                if count <= 0:
                    continue
                else:
                    for i in range(count):
                        pool.append(self.create_item(item.name))

        if self.options.dropsanity == self.options.dropsanity.option_true:
            for original_item in drop_items:
                item = item_table_by_setting_by_name[Settings.mob_drops][original_item]
                count = item.count - counter[item.name]

                if count <= 0:
                    continue
                else:
                    for i in range(count):
                        pool.append(self.create_item(item.name))

        for items in skipped_items:
            item = complete_items_by_name[items]
            pool.remove(item)
            pool.append(self.create_item(self.get_filler_item_name()))

        filler_pool = [item for item in pool if item.classification == ItemClassification.filler]
        void_location_count = len(list(world.get_locations(self.player))) - len(pool)
        if void_location_count - event_items_count > 0:
            for _ in range(void_location_count - event_items_count):
                chosen_item = world.random.choice(filler_pool)
                pool.append(self.create_item(chosen_item.name))
        if void_location_count - event_items_count < 0:
            for _ in range(event_items_count - void_location_count):
                health_vial = next(item for item in pool if item.name == Creation.health_vial)
                pool.remove(health_vial)
        world.itempool += pool

    def fill_slot_data(self) -> Dict[str, Any]:

        excluded_options = []
        excluded_option_names = [option.internal_name for option in excluded_options]
        generic_option_names = [option_name for option_name in LunacidOptions.type_hints]
        excluded_option_names.extend(generic_option_names)
        included_option_names: List[str] = [option_name for option_name in self.options_dataclass.type_hints if option_name not in excluded_option_names]
        slot_data = self.options.as_dict(*included_option_names)
        slot_data.update({
            "seed": self.multiworld.per_slot_randoms[self.player].randrange(1000000000),  # Seed should be max 9 digits
            "client_version": "0.1.0",
        })

        return slot_data
