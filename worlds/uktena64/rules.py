from typing import TYPE_CHECKING, Dict

from BaseClasses import CollectionState
from worlds.generic.Rules import CollectionRule
from .strings.items import JebCampaignItem, BaseItem, JeebCampaignItem, JebItem, JeebItem, PhotoItem, MeatItem
from .strings.locations import TurkeyCreek, JebCabin, CabinCamera, TurkeyCamera, Hyena, FrigidValley, FrigidCamera, HowlingMarsh, HowlingCamera, \
    BleedingGrove, TheBBQBasket, BBQMeat, RitualRoad, RitualMeat, LakeLinger, LakeMeat, PallidPark, PallidMeat, BurningGrove, BurningMeat, \
    BleedingCamera
from .strings.regions import JebEntrance, JeebEntrance

if TYPE_CHECKING:
    from . import UktenaWorld

class UktenaRules:
    player: int
    world: "UktenaWorld"
    region_rules: Dict[str, CollectionRule]
    entrance_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]

    def __init__(self, world: "UktenaWorld") -> None:
        self.player = world.player
        self.world = world
        self.world.options = world.options
        only_jeeb = self.world.options.campaign == self.world.options.campaign.option_jeeb
        only_jeb = self.world.options.campaign == self.world.options.campaign.option_jebidiah

        self.region_rules = {}

        self.entrance_rules = {
            JebEntrance.campaign_to_turkey: lambda state: state.has(JebCampaignItem.creek, self.player) or only_jeeb,
            JebEntrance.campaign_to_frozen: lambda state: state.has(JebCampaignItem.frigid_valley, self.player) or only_jeeb,
            JebEntrance.campaign_to_howling: lambda state: state.has(JebCampaignItem.howling_marsh, self.player) or only_jeeb,
            JebEntrance.campaign_to_bleeding: lambda state: state.has(BaseItem.jeb_campaign, self.player, 4) or only_jeeb,
            JeebEntrance.campaign_to_ritual: lambda state: state.has(JeebCampaignItem.ritual_road, self.player) or only_jeb,
            JeebEntrance.campaign_to_lake: lambda state: state.has(JeebCampaignItem.lake_linger, self.player) or only_jeb,
            JeebEntrance.campaign_to_pallid: lambda state: state.has(JeebCampaignItem.pallid_park, self.player) or only_jeb,
            JeebEntrance.campaign_to_burning: lambda state: state.has(BaseItem.jeeb_campaign, self.player, 4) or only_jeb,
        }

        self.location_rules = {
            "Complete Both Campaigns": lambda state: state.has("Complete Jeb Campaign", self.player) and state.has("Complete Jeeb Campaign", self.player),
            "Uktena Defeated": lambda state: state.has(JebItem.bren_lmg, self.player) and state.has(PhotoItem.bleeding_grove, self.player),
            "Failed Rhythm Game": lambda state: state.has(MeatItem.burning, self.player, 7) and state.has(JeebItem.banjo, self.player),
            # Jeb

            # Cabin
            JebCabin.camera: lambda state: state.has(JebItem.knife, self.player),
            JebCabin.clear: lambda state: state.has(PhotoItem.cabin, self.player),

            CabinCamera.squirrel: lambda state: state.has(JebItem.camera, self.player),

            # Turkey Creek
            TurkeyCreek.hen_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            TurkeyCreek.dark_spot_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            TurkeyCreek.house_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            TurkeyCreek.house_coffee: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            TurkeyCreek.clear: lambda state: state.has(PhotoItem.turkey, self.player, 10),

            TurkeyCamera.turkey_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            TurkeyCamera.dark_linked_turkey_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.dark_linked_turkey_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.dark_linked_turkey_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.turkey_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                 and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.rock_linked_turkey_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.rock_linked_turkey_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.rock_linked_turkey_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                             and state.has(JebItem.turkey_call, self.player),
            TurkeyCamera.creek_dead_body: lambda state: state.has(JebItem.camera, self.player),
            TurkeyCamera.house_linked_turkey_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            TurkeyCamera.house_linked_turkey_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.knife, self.player)
                                                              and state.has(JebItem.camera, self.player),
            TurkeyCamera.house_linked_turkey_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            TurkeyCamera.turkey_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player) and
                                                 self.can_break_barrel_in_campaign(state, "Jeb"),
            TurkeyCamera.headless_turkey: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),

            Hyena.turkey_creek: lambda state: self.has_ranged_options_in_campaign(state, "Jeb"),

            # Frigid Valley
            FrigidValley.shack_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.truck: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.path_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.second_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.trailer_barrel_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.final_shack_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.final_shack_coffee: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.late_path_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            FrigidValley.clear: lambda state: state.has(PhotoItem.frigid_valley, self.player, 13),

            FrigidCamera.early_wolf_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.early_wolf_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.early_wolf_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.second_wolf_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.second_wolf_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.second_wolf_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.second_wolf_4: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.open_wolf_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.open_wolf_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.circle_meat: lambda state: state.has(JebItem.camera, self.player),
            FrigidCamera.trailer_dog: lambda state: state.has(JebItem.camera, self.player),
            FrigidCamera.tree_dog_1: lambda state: state.has(JebItem.camera, self.player),
            FrigidCamera.tree_dog_2: lambda state: state.has(JebItem.camera, self.player),
            FrigidCamera.elk: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            FrigidCamera.skinned_return_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_4: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_5: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_6: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.skinned_return_7: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player)
                                                         and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.snowman_skull: lambda state: self.can_break_barrel_in_campaign(state, "Jeb") and
                                                      state.has(JebItem.camera, self.player) and state.has(PhotoItem.frigid_valley, self.player, 13),
            FrigidCamera.mountain_wolf: lambda state: state.has(JebItem.camera, self.player) and self.has_ranged_options_in_campaign(state, "Jeb"),

            Hyena.frigid_valley: lambda state: self.has_ranged_options_in_campaign(state, "Jeb"),

            # Howling Marsh
            HowlingMarsh.fence_house_ammo_1: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            HowlingMarsh.fence_house_ammo_2: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            HowlingMarsh.graveyard_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            HowlingMarsh.greenhouse_ammo_1: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            HowlingMarsh.greenhouse_ammo_2: lambda state: self.can_break_barrel_in_campaign(state, "Jeb"),
            HowlingMarsh.clear: lambda state: state.has(PhotoItem.howling_marsh, self.player, 6),
            HowlingCamera.bear_1: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            HowlingCamera.bear_2: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            HowlingCamera.bear_3: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            HowlingCamera.bear_4: lambda state: state.has(JebItem.knife, self.player) and state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_1: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                        state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_2: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                          state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_3: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                          state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_4: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                          state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_5: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                          state.has(JebItem.camera, self.player),
            HowlingCamera.burned_corpses_6: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                          state.has(JebItem.camera, self.player),
            HowlingCamera.huge_bear: lambda state: state.has(JebItem.church_key, self.player) and state.has(JebItem.knife, self.player) and
                                                   state.has(JebItem.camera, self.player),

            # Bleeding Grove
            BleedingGrove.bren: lambda state: state.has(JebItem.camera, self.player) and self.has_ranged_options_in_campaign(state, "Jeb"),
            BleedingGrove.clear: lambda state: state.has(JebItem.bren_lmg, self.player) and state.has(PhotoItem.bleeding_grove, self.player),

            BleedingCamera.starved: lambda state: state.has(JebItem.camera, self.player) and self.has_ranged_options_in_campaign(state, "Jeb"),

            # Jeeb

            # The BBQ Basket
            TheBBQBasket.binoculars: lambda state: state.has(JeebItem.butcher_knives, self.player),
            TheBBQBasket.ruger: lambda state: state.has(JeebItem.butcher_knives, self.player),
            TheBBQBasket.clear: lambda state: state.has(MeatItem.bbq, self.player),

            BBQMeat.squirrel: lambda state: state.has(JeebItem.butcher_knives, self.player),

            # Ritual Road
            RitualRoad.truck_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            RitualRoad.outside_venereal_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            RitualRoad.bridge_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            RitualRoad.clear: lambda state: state.has(MeatItem.ritual, self.player, 10),

            RitualMeat.bird_bridge_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.bird_bridge_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.bird_bridge_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.roadkill_bridge_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.roadkill_bridge_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.dollar_bird_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.dollar_bird_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.dollar_bird_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.tree_roadkill: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.intersection_bird_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.intersection_bird_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.intersection_roadkill: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.car_crash: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.legless_deer: lambda state: state.has(JeebItem.butcher_knives, self.player),
            RitualMeat.your_truck: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.ritual, self.player, 10),

            # Lake Linger
            LakeLinger.starting_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.island_coffee: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.island_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.dead_end_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.two_story_coffee: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.main_office_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.north_house_trap: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.coffee_trap_trap_1: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.coffee_trap_trap_2: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.coffee_trap_trap_3: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.dam_ammo_1: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.dam_ammo_2: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            LakeLinger.trapped_start_trap_1: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_2: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_3: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_4: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_5: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_6: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.trapped_start_trap_7: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb") and state.has(MeatItem.lake, self.player, 16),
            LakeLinger.clear: lambda state: state.has(MeatItem.lake, self.player, 16),

            LakeMeat.dead_body: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.hiding_otter_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.hiding_otter_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.hiding_otter_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.covered_body: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_4: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_5: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_6: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.north_house_otter_7: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.coffee_trap_otter_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.coffee_trap_otter_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.coffee_trap_otter_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.dam_otter_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.dam_otter_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.warning_otter_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.warning_otter_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.warning_otter_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.warning_otter_4: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.warning_otter_5: lambda state: state.has(JeebItem.butcher_knives, self.player),
            LakeMeat.trapped_start_1: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.lake, self.player, 16),
            LakeMeat.trapped_start_2: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.lake, self.player, 16),
            LakeMeat.trapped_start_3: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.lake, self.player, 16),
            LakeMeat.trapped_start_4: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.lake, self.player, 16),

            Hyena.lake_linger: lambda state: self.has_ranged_options_in_campaign(state, "Jeeb"),

            # Pallid Park
            PallidPark.chamber_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            PallidPark.owner_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            PallidPark.swamp_bridge_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            PallidPark.north_coffee: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            PallidPark.swamp_shack_ammo: lambda state: self.can_break_barrel_in_campaign(state, "Jeeb"),
            PallidPark.clear: lambda state: state.has(MeatItem.pallid, self.player, 9),

            PallidMeat.dougie: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.dead_owner: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.north_leech_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.north_leech_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.north_leech_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.north_leech_4: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.south_leech_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.south_leech_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.south_leech_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.south_leech_4: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.ghost_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            PallidMeat.ghost_2: lambda state: state.has(JeebItem.butcher_knives, self.player) and state.has(MeatItem.pallid, self.player, 9),

            # Burning Grove
            BurningGrove.banjo: lambda state: state.has(MeatItem.burning, self.player, 7),
            BurningGrove.clear: lambda state: state.has(MeatItem.burning, self.player, 7) and state.has(JeebItem.banjo, self.player),

            BurningMeat.burning_dog_1: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.burning_dog_2: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.burning_dog_3: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.burning_dog_4: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.burning_dog_5: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.burning_dog_6: lambda state: state.has(JeebItem.butcher_knives, self.player),
            BurningMeat.rotting_corpse: lambda state: state.has(JeebItem.butcher_knives, self.player),
        }

    def can_break_barrel_in_campaign(self, state: CollectionState, campaign: str) -> bool:
        if campaign == "Jeb":
            return state.has_any(JebItem.weapons, self.player)
        return state.has_any(JeebItem.weapons, self.player)

    def has_ranged_options_in_campaign(self, state: CollectionState, campaign: str) -> bool:
        if campaign == "Jeb":
            return state.has_any(JebItem.guns, self.player)
        return state.has_any(JeebItem.guns, self.player)


    def set_uktena_rules(self) -> None:
        multiworld = self.world.multiworld
        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
                for location in region.locations:
                    location.access_rule = self.region_rules[region.name]
            for entrance in region.entrances:
                multiworld.register_indirect_condition(region, entrance)
                if entrance.name in self.entrance_rules:
                    entrance.access_rule = entrance.access_rule and self.entrance_rules[entrance.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = loc.access_rule and self.location_rules[loc.name]
