from ..strings.items import UniqueItem, GenericItem, Creation, Alchemy, Coins, Switch, Progressives, Traps, Door, RareDrops, UnusedItems
from ..strings.weapons import Weapon
from ..strings.spells import Spell, MobSpell

base_weapons = [Weapon.replica_sword,
                Weapon.torch,
                Weapon.ritual_dagger,
                Weapon.wooden_shield,
                Weapon.stone_club,
                Weapon.steel_spear,
                Weapon.battle_axe,
                Weapon.broken_hilt,
                Weapon.corrupted_dagger,
                Weapon.dark_rapier,
                Weapon.halberd,
                Weapon.blade_of_jusztina,
                Weapon.twisted_staff,
                Weapon.vampire_hunter_sword,
                Weapon.elfen_bow,
                Weapon.elfen_sword,
                Weapon.wolfram_greatsword,
                Weapon.axe_of_harming,
                Weapon.wand_of_power,
                Weapon.blade_of_ophelia,
                Weapon.marauder_black_flail,
                Weapon.blessed_wind,
                Weapon.iron_claw,
                Weapon.moonlight,
                Weapon.broken_lance,
                Weapon.fishing_spear,
                Weapon.hammer_of_cruelty,
                Weapon.obsidian_seal,
                Weapon.shadow_blade,
                Weapon.serpent_fang,
                Weapon.lucid_blade,
                ]

base_spells = [Spell.ghost_light,
               Spell.flame_spear,
               Spell.lithomancy,
               Spell.flame_flare,
               Spell.blood_strike,
               Spell.ice_spear,
               Spell.barrier,
               Spell.slime_orb,
               Spell.wind_dash,
               Spell.summon_fairy,
               Spell.coffin,
               Spell.lightning,
               Spell.blood_drain,
               Spell.holy_warmth,
               Spell.light_reveal,
               Spell.earth_strike,
               Spell.poison_mist,
               Spell.wind_slicer,
               Spell.corpse_transformation,
               Spell.fire_worm,
               Spell.bestial_communion,
               Spell.moon_beam,
               Spell.summon_ice_sword,
               Spell.earth_thorn,
               Spell.ice_tear,
               Spell.rock_bridge,
               Spell.ignis_calor,
               Spell.icarian_flight,
               Spell.blue_flame_arc,
               Spell.lava_chasm,
               Spell.spirit_warp,
               Spell.jingle_bells
               ]

base_unique_items = [
    UniqueItem.vhs_tape,
    UniqueItem.corrupted_key,
    UniqueItem.white_tape,
    UniqueItem.skull_of_josiah,
    Alchemy.fractured_life,
    UniqueItem.earth_talisman,
    UniqueItem.enchanted_key,
    UniqueItem.terminus_prison_key,
    Alchemy.broken_sword,
    Alchemy.fractured_death,
    UniqueItem.water_talisman,
    UniqueItem.skeleton_egg,
    UniqueItem.dried_rat,
    UniqueItem.dusty_crystal_orb,
    UniqueItem.skeleton_rattle
]

base_special_item_counts = {
    UniqueItem.black_book: 3,
    Progressives.vampiric_symbol: 3,
    UniqueItem.ocean_elixir: 6,
    UniqueItem.earth_elixir: 9,
}

filler_items = [
    Creation.crystal_shard,
    Creation.health_vial,
    Creation.mana_vial,
    Creation.antidote,
    GenericItem.blood_wine,
    UniqueItem.survey_banner,
    Coins.silver,
    GenericItem.dark_urn,
    GenericItem.light_urn,
    Alchemy.ashes,
    GenericItem.cloth_bandage,
    Alchemy.ectoplasm,
    Alchemy.snowflake_obsidian,
    Alchemy.moon_petal,
    Alchemy.opal,
    Alchemy.fire_opal,
    Alchemy.ikurrilb_root,
    Alchemy.onyx,
    Alchemy.obsidian,
    Alchemy.ocean_bone_shell,
    Alchemy.ocean_bone_shard,
    Alchemy.destroying_angel_mushroom,
    Alchemy.yellow_morel,
    Alchemy.bloodweed,
    Alchemy.lotus_seed_pod,
]

crafted_items = [
    Creation.poison_throwing_knife,
    Creation.holy_water,
    Creation.spectral_candle,
    Creation.staff_of_osiris,
    Creation.moonlight_vial,
    Creation.wisp_heart,
    Creation.fairy_moss,
    Creation.bomb,
    Creation.poison_urn,]

drop_items = [
    RareDrops.shrimp,
    RareDrops.angel_feather
]

unused_items = [
    UnusedItems.tent,
    UnusedItems.curry
]

shop_weapons = [Weapon.rapier,
                Weapon.crossbow,
                Weapon.jotunn_slayer,
                Weapon.privateer_musket,
                Weapon.steel_needle
                ]

shop_unique_items = [UniqueItem.oil_lantern,
                     UniqueItem.enchanted_key
                     ]

shop_item_count = {UniqueItem.ocean_elixir: 2}

drop_weapons = [Weapon.rusted_sword,
                Weapon.ice_sickle,
                Weapon.skeleton_axe,
                Weapon.cursed_blade,
                Weapon.obsidian_cursebrand,
                Weapon.obsidian_poisonguard,
                Weapon.golden_kopesh,
                Weapon.golden_sickle,
                Weapon.brittle_arming_sword,
                Weapon.jailor_candle,
                Weapon.lyrian_longsword,
                Weapon.sucsarian_spear,
                Weapon.sucsarian_dagger,
                ]

drop_spells = [MobSpell.summon_snail,
               MobSpell.summon_kodama,
               MobSpell.quick_stride,
               MobSpell.dark_skull,
               MobSpell.tornado,
               ]

drop_filler_count = [UniqueItem.ocean_elixir
                     ]

switches = [Switch.hollow_basin_switch_near_demi,
            Switch.temple_switch,
            Switch.fetid_mire_switch,
            Switch.archives_switch,
            Switch.archives_elevator_switches,
            Switch.tomb_switches,
            Switch.tomb_light_switches,
            Switch.ballroom_switch,
            Switch.grotto_valves_switches,
            Switch.grotto_switches,
            Switch.prison_shortcut_switch,
            Switch.prison_arena_switch,
            Switch.arena_water_switch,
            Switch.arena_earth_switch,
            Switch.ash_switch,
            ]

doors_no_tower = [Door.basin_temple_sewers,
                  Door.basin_broken_steps,
                  Door.basin_rickety_bridge,
                  Door.chasm_surface_door,
                  Door.ballroom_rooms_key,
                  Door.sleeper_key,
                  Door.sucs_key,
                  Door.ash_key,
                  Door.burning_key,
                  Door.forlorn_key,
                  Door.prison_key,
                  Door.ballroom_key,
                  Door.throne_key,
                  Door.archives_sealed_door,
                  Door.sea_double_doors,
                  Door.sea_eastward,
                  Door.sea_westward,
                  Door.forest_patchouli,
                  Door.forest_door_in_trees]

traps = [Traps.health_viai,
         Traps.slowness_trap,
         Traps.bleed_trap,
         Traps.curse_trap,
         Traps.blindness_trap,
         Traps.mana_drain_trap,
         Traps.xp_drain_trap,
         Traps.poison_trap,
         Traps.eggnog,
         Traps.coal]

