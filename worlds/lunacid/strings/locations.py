from typing import Dict, List


class BaseLocation:
    wings_rest_crystal_shard = "WR: Bench"
    wings_rest_ocean_elixir = "WR: Rafters"
    wings_rest_clives_gift = "WR: Clive's Gift"
    wings_rest_demi_gift = "WR: Demi's Introduction Gift"
    wings_rest_demi_orb = "WR: Demi's Victory Gift"

    hollow_basin_starting_sword = "HB: Starting Weapon"
    hollow_basin_right_water_right = "HB: Rightmost Water Room (Right)"
    hollow_basin_right_water_left = "HB: Rightmost Water Room (Left)"
    hollow_basin_left_water = "HB: Leftmost Water Room"
    hollow_basin_demi_chest = "HB: Chest Near Demi"
    hollow_basin_enchanted_door = "HB: Near Enchanted Door"
    hollow_basin_dark_item = "HB: Dark Tunnel After Enchanted Door"

    temple_fountain = "HB: Temple Fountain"
    temple_ritual_table = "HB: Temple Ritual Table"
    temple_altar_chest = "HB: Temple Altar Chest"
    temple_pillar_left = "HB: Temple Hidden Room Behind Pillar (Left)"
    temple_pillar_right = "HB: Temple Hidden Room Behind Pillar (Right)"
    temple_ritual_ring = "HB: Temple Ritual Table After Bridge"
    temple_small_pillar = "HB: Temple Small Pillar Top"
    temple_pillar_room_left = "HB: Temple Pillar Room Left"
    temple_pillar_room_back_left = "HB: Temple Pillar Room Back Left"
    temple_pillar_room_back_right = "HB: Temple Pillar Room Back Right"
    temple_pillar_room_hidden_room = "HB: Temple Pillar Room Hidden Room"
    temple_hidden_room_in_sewer = "HB: Temple Hidden Room In Sewer"
    temple_table_in_sewer = "HB: Temple Table in Sewer"
    temple_sewer_puzzle = "HB: Temple Sewer Puzzle"
    temple_blood_altar = "HB: Temple Blood Altar"
    temple_path_to_forest = "HB: Alcove on Path to Yosei Forest"

    mire_room_left_foyer = "FM: Room Left of Foyer"
    mire_hidden_slime_chest = "FM: Hidden Slimey Chest Near Entrance"
    mire_upper_overlook_left = "FM: Hidden Upper Overlook (Left)"
    mire_upper_overlook_right = "FM: Hidden Upper Overlook (Right)"
    mire_bonenard_trash = "FM: Bonenard's Trash"
    mire_rubble_bridge = "FM: Rubble Near Overlook Bridge"
    mire_skeleton_chest = "FM: Slime Skeleton Chest"
    mire_jellisha_trash = "FM: Jellisha's Trash"
    mire_jellisha_reward = "FM: Jellisha's Quest Reward"
    mire_hidden_chest_near_underworks = "FM: Hidden Chest Near Underworks"
    mire_rubble_near_illusory_wall = "FM: Rubble Near Illusory Wall"
    mire_underwater_pipe = "FM: Underwater Pipe"
    mire_underworks_waterfall = "FM: Underworks Waterfall"
    mire_underworks_skeleton = "FM: Underworks Skeleton"
    mire_path_to_sea_left = "FM: Path to Sanguine Sea (Left)"
    mire_path_to_sea_right = "FM: Path to Sanguine Sea (Right)"

    sea_pillar = "SS: Pillar In Front of Castle Le Fanu"
    sea_underblood = "SS: Underblood Near Castle Le Fanu"
    sea_fairy_circle = "SS: Fairy Circle"
    sea_kill_jotunn = "SS: Killing the Jotunn"

    catacombs_coffin_stairs = "AT: Catacombs Coffins Near Stairs"
    catacombs_coffin_blue_light = "AT: Catacombs Coffins With Blue Light"
    corrupted_room = "AT: Corrupted Room"
    catacombs_coffin_gate = "AT: Gated Tomb Near Corrupted Room"
    catacombs_hidden_room = "AT: Catacombs Hidden Room"
    catacombs_deep_coffin_storage = "AT: Deep Coffin Storage"
    catacombs_restore_vampire = "AT: Red Skeleton"

    mausoleum_hidden_chest = "AT: Mausoleum Hidden Chest"
    mausoleum_upper_table = "AT: Mausoleum Upper Alcove Table"
    mausoleum_maze_intro = "AT: Mausoleum Maze (Early)"
    mausoleum_maze_mid = "AT: Mausoleum Maze (Middle)"
    mausoleum_center_right = "AT: Mausoleum Central Room (Right)"
    mausoleum_center_left = "AT: Mausoleum Central Room (Left)"
    mausoleum_center_back = "AT: Mausoleum Central Room (Back)"
    mausoleum_center_left_path = "AT: Mausoleum Central Room (Left Path)"
    mausoleum_center_right_path = "AT: Mausoleum Central Room (Right Path)"
    mausoleum_kill_death = "AT: Kill Death"

    tomb_tomb_with_switch = "AT: Tomb With Switch"
    tomb_tomb_with_corpse = "AT: Tomb With Sitting Corpse"
    tomb_demi_chest = "AT: Demi Chest"
    tomb_near_light_switch = "AT: Near Light Switch"
    tomb_hidden_room = "AT: Hidden Room in Tomb"
    tomb_hidden_chest = "AT: Hidden Chest in Tomb"

    yosei_barrels = "YF: Barrel Group"
    yosei_blood_pool = "YF: Blood Pool"
    yosei_branch_in_tree = "YF: Branches Within Tree"
    yosei_chest_near_tree = "YF: Chest Near Tree"
    yosei_blood_plant_insides = "YF: Blood Plant's Insides"
    yosei_hanging_in_trees = "YF: Hanging In The Trees"
    yosei_hidden_chest = "YF: Hidden Chest"
    yosei_room_defended_by_blood_plant = "YF: Room Defended by Blood Plant"
    yosei_patchouli_key = "YF: Patchouli's Canopy Offer"
    yosei_patchouli_quest = "YF: Patchouli's Reward"

    canopy_branch_edge = "FC: Branch Lower Edge"
    branch_cave = "FC: Branch Cave"
    canopy_chest = "FC: Chest"
    canopy_wooden_statue = "FC: Wooden Statue (Josiah)"
    canopy_wooden_sitting = "FC: Wooden Statue (Sitting)"

    archives_back_room_past_bridge = "FbA: Back Room Past Bridge"
    archives_strange_corpse = "FbA: Strange Corpse"
    archives_short_wall_near_trees = "FbA: Short Wall Near Trees"
    archives_against_wall_near_trees = "FbA: Against Wall Near Trees"
    archives_snail_lectern_near = "FbA: Snail Lectern (Near)"
    archives_snail_lectern_far = "FbA: Snail Lectern (Far)"
    archives_rug_on_balcony = "FbA: Rug on Balcony"
    archives_rooftop = "FbA: Rooftops"
    archives_hidden_room_upper = "FbA: Hidden Room Upper Floor"
    archives_hidden_room_lower = "FbA: Hidden Room Lower Floor"
    archives_near_twisty_tree = "FbA: Near Twisty Tree"
    archives_uwu = "FbA: uwu"
    archives_daedalus_one = "FbA: Daedalus Knowledge (First)"
    archives_daedalus_two = "FbA: Daedalus Knowledge (Second)"
    archives_daedalus_third = "FbA: Daedalus Knowledge (Third)"
    archives_corner_near_daedalus = "FbA: Corner Near Daedalus"

    castle_outside_corner = "CLF: Outside Corner"
    castle_cell_south = "CLF: Cattle Cell (South)"
    castle_cell_west = "CLF: Cattle Cell (West)"
    castle_cell_center = "CLF: Cattle Cell (Center)"
    castle_cell_north = "CLF: Cattle Cell (North)"
    castle_hidden_cell = "CLF: Hidden Cattle Cell"

    castle_hallway_rubble_room = "CLF: Hallway Rubble Room"
    castle_hallway_dining_room = "CLF: Hallway Dining Room"
    castle_garrat_resting_room_left = "CLF: Garrat Resting Room (Fountain)"
    castle_garrat_resting_room_back = "CLF: Garrat Resting Room (Wall)"
    castle_hallway_deadend_before_door = "CLF: Hallway Dead End Before Blue Doors"
    castle_upper_floor_coffin_small = "CLF: Upper Floor Coffin Room (Small Room)"
    castle_upper_floor_coffin_large = "CLF: Upper Floor Coffin Room (Large Room)"
    castle_upper_floor_coffin_double = "CLF: Upper Floor Coffin Room (Double)"
    castle_upper_floor_coffin_hallway = "CLF:  Upper Floor Coffin Room (Hallway)"

    ballroom_small_room_lounge = "SB: Entry Small Room Lounge"
    ballroom_entry_hidden_couch_top = "SB: Entry Hidden Couch Top"
    ballroom_entry_hidden_couch_bottom = "SB: Entry Hidden Couch Bottom"
    ballroom_entry_hidden_cave_in_lounge = "SB: Entry Hidden Cave in a Lounge"
    ballroom_entry_long_table = "SB: Entry Lounge Long Table"
    ballroom_side_hidden_cave = "SB: Side Hidden Cave"
    ballroom_side_chest_near_switch = "SB: Side Chest Near Switch"
    ballroom_side_painting = "SB: Side Painting Viewing Room"
    ballroom_side_hidden_casket_room = "SB: Side Hidden Casket Room"
    ballroom_side_xp_drain = "SB: Side XP Drain Party Room"

    chasm_hidden_chest = "LC: Hidden Room"
    chasm_invisible_cliffside = "LC: Invisible Path to Cliffside"

    surface_demi_gift = "GWS: Demi's Gift"

    throne_book = "TC: Crilall's Book Repository"

    battlefield_book = "AHB: Sngula Umbra's Remains"

    grotto_slab_of_bridge = "BG: Slab of a Broken Bridge"
    grotto_hidden_chest = "BG: Hidden Chest"
    grotto_corpse_beneath_entrance = "BG: Corpse Beneath Entrance"
    grotto_triple_secret_chest = "BG: Triple Hidden Chest"
    grotto_rocks_near_lava_switch = "BG: Lava Overseeing Dragon Switch"
    grotto_through_switch_tunnel = "BG: Through Dragon Switch Tunnel"

    sand_room_buried_in_sand = "ST: Room Buried in Sand"
    sand_top_right_sarcophagus = "ST: Top Right Sarcophagus"
    sand_second_floor_snake = "ST: Second Floor Snake Room"
    sand_basement_snake_pit = "ST: Basement Snake Pit"
    sand_hidden_sarcophagus = "ST: Hidden Sarcophagus"
    sand_second_floor_dead_end = "ST: Second Floor Dead End"
    sand_lunacid_sandwich = "ST: Lunacid Sandwich"
    sand_chest_near_switch = "ST: Chest Near Switch"
    sand_chest_overlooking_crypt = "ST: Chest Overlooking Crypt"
    sand_switch_maze = "ST: Floor Switch Maze"
    sand_basement_rubble = "ST: Basement Stone Rubble"
    sand_triple_sarcophagus = "ST: Triple Sarcophagus"

    abyss_floor_5 = "TA: Floor 5 Chest"
    abyss_heal_5 = "TA: Floor 5 Item 1"
    abyss_crystal_5 = "TA: Floor 5 Item 2"
    abyss_floor_10 = "TA: Floor 10 Chest"
    abyss_heal_10 = "TA: Floor 10 Item 1"
    abyss_crystal_10 = "TA: Floor 10 Item 2"
    abyss_floor_15 = "TA: Floor 15 Chest"
    abyss_heal_15 = "TA: Floor 15 Item 1"
    abyss_crystal_15 = "TA: Floor 15 Item 2"
    abyss_floor_20 = "TA: Floor 20 Chest"
    abyss_heal_20 = "TA: Floor 20 Item 1"
    abyss_crystal_20 = "TA: Floor 20 Item 2"
    abyss_floor_25 = "TA: Floor 25 Chest"
    abyss_heal_25 = "TA: Floor 25 Item 1"
    abyss_crystal_25 = "TA: Floor 25 Item 2"
    abyss_floor_30 = "TA: Floor 30 Chest"
    abyss_heal_30 = "TA: Floor 30 Item 1"
    abyss_crystal_30 = "TA: Floor 30 Item 2"
    abyss_floor_35 = "TA: Floor 35 Chest"
    abyss_heal_35 = "TA: Floor 35 Item 1"
    abyss_crystal_35 = "TA: Floor 35 Item 2"
    abyss_floor_40 = "TA: Floor 40 Chest"
    abyss_heal_40 = "TA: Floor 40 Item 1"
    abyss_crystal_40 = "TA: Floor 40 Item 2"
    abyss_floor_45 = "TA: Floor 45 Chest"
    abyss_heal_45 = "TA: Floor 45 Item 1"
    abyss_crystal_45 = "TA: Floor 45 Item 2"
    abyss_floor_50 = "TA: Floor 50 Chest"
    abyss_heal_50 = "TA: Floor 50 Item 1"
    abyss_crystal_50 = "TA: Floor 50 Item 2"
    abyss_prize = "TA: Prize Beneath Tree"

    prison_f3_locked_left = "TP: Third Floor Locked Cell Left"
    prison_f3_locked_right = "TP: Third Floor Locked Cell Right"
    prison_f3_locked_south = "TP: Third Floor Locked Cell South"
    prison_f3_bottomless_pit = "TP: Almost Bottomless Pit"
    prison_f2_broken_cell = "TP: Second Floor Broken Cell"
    prison_f2_jailer_table = "TP: Second Floor Jailer's Table"
    prison_f1_hidden_cell = "TP: First Floor Hidden Cell"
    prison_f1_hidden_debris_room = "TP: First Floor Hidden Debris Room"
    prison_f1_remains = "TP: First Floor Remains"
    prison_b2_guarded_corner_one = "TP: Green Asylum Guarded Alcove (Left)"
    prison_b2_guarded_corner_two = "TP: Green Asylum Guarded Alcove (Right)"
    prison_b2_deep_alcove = "TP: Green Asylum Long Alcove"
    prison_b2_bone_pit = "TP: Green Asylum Bone Pit"
    prison_b2_egg_resting_place = "TP: Egg's Resting Place"
    prison_f4_hanging = "TP: Fourth Floor Cell Hanging Remains"
    prison_f4_maledictus_secret = "TP: Fourth Floor Maledictus Secret"
    prison_f4_hidden_beds = "TP: Fourth Floor Hidden Jailer Sleeping Spot"
    prison_f4_jailer_break_room = "TP: Fourth Floor Jailer Break Room"
    prison_f4_monk_room_one = "TP: Etna's Resting Place Item 1"
    prison_f4_monk_room_two = "TP: Etna's Resting Place Item 2"
    prison_f4_monk_room_three = "TP: Etna's Resting Place Item 3"
    prison_f4_collapsed_tunnel = "TP: Fourth Floor Collapsed Tunnel"

    arena_broken_sword = "FlA: Corpse Waiting For A Full Moon"
    arena_rock_parkour = "FlA: Entry Rock Parkour"
    arena_earth_hidden_plant_haven = "FlA: Temple of Earth Hidden Plant Haven"
    arena_earth_hidden_room = "FlA: Temple of Earth Hidden Room"
    arena_earth_earthen_temple = "FlA: Temple of Earth Fractured Chest"
    arena_earth_chest_near_switch = "FlA: Temple of Earth Chest Near Switch"
    arena_water_room_near_water = "FlA: Temple of Water Room Near Water"
    arena_water_dead_end_near_water = "FlA: Temple of Water Corner Near Water"
    arena_water_collapsed_end_near_balcony = "FlA: Temple of Water Collapsed End Near Balcony"
    arena_water_hidden_basement_left = "FlA: Temple of Water Hidden Basement (Left)"
    arena_water_hidden_basement_right = "FlA: Temple of Water Hidden Basement (Right)"
    arena_water_hidden_laser_room = "FlA: Temple of Water Hidden Laser Room"
    arena_water_hidden_alcove_before = "FlA: Temple of Water Hidden Alcove Before Stairs"
    arena_water_hidden_alcove_left = "FlA: Temple of Water Hidden Alcove (Left)"
    arena_water_hidden_alcove_right = "FlA: Temple of Water Hidden Alcove (Right)"
    arena_water_hidden_alcove_before_switch = "FlA: Temple of Water Hidden Alcove Before Switch"
    arena_water_underwater_temple = "FlA: Temple of Water Fractured Chest"
    arena_water_chest_near_switch = "FlA: Temple of Water Chest Near Switch"

    ash_entry_coffin = "LA: Entry Coffin"
    ash_giant_remains = "LA: Giant Remains"
    ash_cetea_statue = "LA: Behind Statue"
    ash_rocks_near_switch = "LA: Rocks Near Switch"
    ash_forbidden_light_chest = "LA: Forbidden Light Chest"
    ash_hidden_chest = "LA: Hidden Light Stash"
    ash_path_maze = "LA: NNSNSSNSNN Lost Maze"

    fate_lucid_blade = "CF: Calamis' Weapon of Choice"

    abyss_locations = [abyss_prize, abyss_floor_50, abyss_floor_45, abyss_floor_40, abyss_floor_35, abyss_floor_30, abyss_floor_25, abyss_floor_20,
                       abyss_floor_15, abyss_floor_10, abyss_floor_5]
    coin_locations = [sea_kill_jotunn, mausoleum_kill_death, temple_blood_altar]
    daedalus_locations = [archives_daedalus_third, archives_daedalus_one, archives_daedalus_two]


class ShopLocation:
    buy_enchanted_key = "Buy Enchanted Key"
    buy_rapier = "Buy Rapier"
    buy_steel_needle = "Buy Steel Needle"
    buy_crossbow = "Buy Crossbow"
    buy_oil_lantern = "Buy Oil Lantern"
    buy_ocean_elixir_patchouli = "Buy Ocean Elixir (Patchouli)"
    buy_privateer_musket = "Buy Privateer Musket"
    buy_jotunn_slayer = "Buy Jotunn Slayer"

    shop_locations = [buy_rapier, buy_crossbow, buy_jotunn_slayer, buy_ocean_elixir_patchouli,
                      buy_oil_lantern, buy_enchanted_key, buy_steel_needle, buy_privateer_musket]


unique_drop_locations = []
other_drop_locations = []


def unique_drop(name: str) -> str:
    if name not in unique_drop_locations:
        unique_drop_locations.append(name)
    return name


def other_drop(name: str) -> str:
    if name not in other_drop_locations:
        other_drop_locations.append(name)
    return name


class DropLocation:
    #  Hollow Basin
    snail = unique_drop("Snail: Summon Snail Drop")
    snail_2c = other_drop("Snail: Small Silver Drop")
    snail_10c = other_drop("Snail: Large Silver Drop")
    snail_ocean = other_drop("Snail: Ocean Bone Shard Drop")
    milk_snail = unique_drop("Milk Snail: Ice Sickle Drop")
    milk_5c = other_drop("Milk Snail: Small Silver Drop")
    milk_10c = other_drop("Milk Snail: Large Silver Drop")
    milk_ocean = other_drop("Milk Snail: Ocean Bone Shard Drop")
    shulker_obsidian = other_drop("Shulker: Obsidian Drop")
    shulker_onyx = other_drop("Shulker: Onyx Drop")
    mummy_mana_vial = other_drop("Mummy: Mana Vial Drop")
    mummy_onyx = other_drop("Mummy: Onyx Drop")
    mummy_2c = other_drop("Mummy: Small Silver Drop")
    mummy_10c = other_drop("Mummy: Large Silver Drop")
    mummy_knight = unique_drop("Mummy Knight: Rusted Sword Drop")
    mummy_knight_onyx = other_drop("Mummy Knight: Onyx Drop")
    mummy_knight_10c = other_drop("Mummy Knight: Large Silver Drop")
    mummy_knight_5c = other_drop("Mummy Knight: Small Silver Drop")
    #  Forbidden Archives
    necronomicon_fire_opal = other_drop("Necronomicon: Fire Opal Drop")
    necronomicon_5c = other_drop("Necronomicon: Medium Silver Drop")
    necronomicon_10c = other_drop("Necronomicon: Large Silver Drop")
    necronomicon_mana_vial = other_drop("Necronomicon: Mana Vial Drop")
    chimera_drop = unique_drop("Chimera: Quick Stride Drop")
    chimera_light_urn = other_drop("Chimera: Light Urn Drop")
    chimera_holy_water = other_drop("Chimera: Holy Water Drop")
    enlightened_mana_vial = other_drop("Enlightened One: Mana Vial Drop")
    enlightened_ocean_bone_shell = other_drop("Enlightened One: Ocean Bone Shell Drop")
    #  Fetid Mire
    slime_skeleton = other_drop("Slime Skeleton: Ashes Drop")
    skeleton_weapon = unique_drop("Skeleton: Skeleton Axe Drop")
    skeleton_spell = unique_drop("Skeleton: Dark Skull Drop")
    skeleton_10c = other_drop("Skeleton: Medium Silver Drop")
    skeleton_mana_vial = other_drop("Skeleton: Mana Vial")
    skeleton_onyx = other_drop("Skeleton: Onyx Drop")
    skeleton_bones = other_drop("Skeleton: Bones Drop")
    rat_king_10c = other_drop("Rat King: Large Silver Drop")
    rat_king_lotus_seed = other_drop("Rat King: Lotus Seed Pod Drop")
    rat = other_drop("Rat: Small Silver Drop")
    #  Yosei Forest + Forest Canopy
    kodama_drop = unique_drop("Kodama: Summon Kodama Drop")
    kodama_2c = other_drop("Kodama: Small Silver Drop")
    kodama_10c = other_drop("Kodama: Medium Silver Drop")
    kodama_opal = other_drop("Kodama: Opal Drop")
    yakul_10c = other_drop("Yakul: Medium Silver Drop")
    yakul_fire_opal = other_drop("Yakul: Fire Opal Drop")
    yakul_opal = other_drop("Yakul: Opal Drop")
    yakul_health_vial = other_drop("Yakul: Health Vial Drop")
    venus_10c = other_drop("Venus: Medium Silver Drop")
    venus_yellow_morel = other_drop("Venus: Yellow Morel Drop")
    venus_dest_angel = other_drop("Venus: Destroying Angel Mushroom Drop")
    neptune_10c = other_drop("Neptune: Medium Silver Drop")
    neptune_yellow_morel = other_drop("Neptune: Yellow Morel Drop")
    neptune_dest_angel = other_drop("Neptune: Destroying Angel Mushroom Drop")
    unilateralis_10c = other_drop("Unilateralis: Medium Silver Drop")
    unilateralis_yellow_morel = other_drop("Unilateralis: Yellow Morel Drop")
    unilateralis_dest_angel = other_drop("Unilateralis: Destroying Angel Mushroom Drop")
    #  Sanguine Sea
    hemalith_health_vial = other_drop("Hemalith: Health Vial Drop")
    hemalith_shrimp = other_drop("Hemalith: Pink Shrimp Drop")
    hemallith_bloodweed = other_drop("Hemalith: Bloodweed Drop")
    sea_demon = unique_drop("Abyssal Demon: Ocean Elixir Drop")
    #  Accursed Tomb
    mi_go_ocean_bone_shell = other_drop("Mi-Go: Ocean Bone Shell Drop")
    mi_go_10c = other_drop("Mi-Go: Medium Silver Drop")
    mi_go_snowflake_obsidian = other_drop("Mi-Go: Snowflake Obsidian Drop")
    mare_10c = other_drop("Mare: Medium Silver Drop")
    mare_obsidian = other_drop("Mare: Obsidian Drop")
    mare_onyx = other_drop("Mare: Onyx Drop")
    painting_fire_opal = other_drop("Cursed Painting: Fire Opal Drop")
    painting_10c = other_drop("Cursed Painting: Medium Silver Drop")
    painting_mana_vial = other_drop("Cursed Painting: Mana Vial Drop")
    painting_20c = other_drop("Cursed Painting: Large Silver Drop")
    #  Castle Le Fanu
    phantom = unique_drop("Phantom: Cursed Blade Drop")
    phantom_10c = other_drop("Phantom: Medium Silver Drop")
    phantom_holy_water = other_drop("Phantom: Holy Water Drop")
    phantom_moon_vial = other_drop("Phantom: Moonlight Vial Drop")
    phantom_ectoplasm = other_drop("Phantom: Ectoplasm Drop")
    vampire_drop = unique_drop("Vampire Page: Lyrian Longsword Drop")
    vampire_5c = other_drop("Vampire: Large Silver Drop")
    vampire_vampiric_ashes = other_drop("Vampire: Vampiric Ashes Drop")
    vampire_bandage = other_drop("Vampire: Cloth Bandage Drop")
    vampire_page_ashes = other_drop("Vampire Page: Vampiric Ashes Drop")
    vampire_page_20c = other_drop("Vampire Page: Large Silver Drop")
    malformed_vampiric_ashes = other_drop("Malformed: Vampiric Ashes Drop")
    great_bat_health_vial = other_drop("Great Bat: Health Vial Drop")
    great_bat_obsidian = other_drop("Great Bat: Obsidian Drop")
    great_bat_10c = other_drop("Great Bat: Large Silver Drop")
    poltergeist_10c = other_drop("Poltergeist: Large Silver Drop")
    poltergeist_ectoplasm = other_drop("Poltergeist: Ectoplasm Drop")
    #  Sealed Ballroom
    horse_drop = unique_drop("Malformed Horse: Brittle Arming Sword Drop")
    horse_10c = other_drop("Malformed Horse: Large Silver Drop")
    horse_mana_vial = other_drop("Malformed Horse: Mana Vial Drop")
    hallowed_husk_10c = other_drop("Hallowed Husk: Large Silver Drop")
    hallowed_husk_bones = other_drop("Hallowed Husk: Bones Drop")
    hallowed_husk_bandage = other_drop("Hallowed Husk: Cloth Bandage Drop")
    hallowed_husk_light_urn = other_drop("Hallowed Husk: Light Urn Drop")
    hallowed_husk_goldeness = other_drop("Hallowed Husk: Fool's Gold Drop")
    hallowed_husk_holy_water = other_drop("Hallowed Husk: Holy Water Drop")
    #  Boiling Grotto
    ikkurilb_root = other_drop("Ikurr'ilb: Ikurr'ilb Root Drop")
    ikkurilb_10c = other_drop("Ikurr'ilb: Medium Silver Drop")
    ikkurilb_snowflake_obsidian = other_drop("Ikurr'ilb: Snowflake Obsidian Drop")
    mimic_moon_vial = other_drop("Mimic: Moonlight Vial Drop")
    mimic_obsidian = other_drop("Mimic: Obsidian Drop")
    mimic_fools_gold = other_drop("Mimic: Fool's Gold Drop")
    obsidian_skeleton_drop_1 = unique_drop("Obsidian Skeleton: Obsidian Cursebrand Drop")
    obsidian_skeleton_drop_2 = unique_drop("Obsidian Skeleton: Obsidian Poisonguard Drop")
    obsidian_skeleton_10c = other_drop("Obsidian Skeleton: Large Silver Drop")
    obsidian_skeleton_bones = other_drop("Obsidian Skeleton: Bones Drop")
    obsidian_skeleton_mana_vial = other_drop("Obsidian Skeleton: Mana Vial Drop")
    obsidian_skeleton_obsidian = other_drop("Obsidian Skeleton: Obsidian Drop")
    anpu_drop_1 = unique_drop("Anpu: Golden Khopesh Drop")
    anpu_drop_2 = unique_drop("Anpu: Golden Sickle Drop")
    anpu_10c = other_drop("Anpu: Large Silver Drop")
    anpu_fire_opal = other_drop("Anpu: Fire Opal Drop")
    serpent_antidote = other_drop("Serpent: Antidote Drop")
    serpent_5c = other_drop("Serpent: Small Silver Drop")
    embalmed_bandage = other_drop("Embalmed: Cloth Bandage Drop")
    embalmed_ashes = other_drop("Embalmed: Ashes Drop")
    embalmed_bones = other_drop("Embalmed: Bones Drop")
    #  Terminus Prison
    jailor_drop = unique_drop("Jailor: Jailor's Candle Drop")
    jailor_10c = other_drop("Jailor: Large Silver Drop")
    jailor_candle = other_drop("Jailor: Spectral Candle Drop")
    jailor_bandage = other_drop("Jailor: Cloth Bandage Drop")
    jailor_health_vial = other_drop("Jailor: Health Vial Drop")
    jailor_angel = other_drop("Jailor: Angel's Feather Drop")
    lunam_ectoplasm = other_drop("Cerritulus Lunam: Ectoplasm Drop")
    lunam_10c = other_drop("Cerritulus Lunam: Medium Silver Drop")
    lunam_snowflake_obsidian = other_drop("Cerritulus Lunam: Snowflake Obsidian Drop")
    giant_dark_urn = other_drop("Giant Skeleton: Dark Urn Drop")
    giant_bones = other_drop("Giant Skeleton: Bones Drop")
    giant_mana_vial = other_drop("Giant Skeleton: Mana Vial Drop")
    giant_onyx = other_drop("Giant Skeleton: Onyx Drop")
    giant_spell = unique_drop("Giant Skeleton: Dark Skull Drop")
    lupine_spell = unique_drop("Lupine Skeleton: Dark Skull Drop")
    lupine_10c = other_drop("Lupine Skeleton: Medium Silver Drop")
    lupine_bones = other_drop("Lupine Skeleton: Bones Drop")
    lupine_onyx = other_drop("Lupine Skeleton: Onyx Drop")
    infested_antidote = other_drop("Infested Corpse: Antidote Drop")
    infested_bones = other_drop("Infested Corpse: Bones")
    #  Forlorn Arena
    sucsarian_drop_1 = unique_drop("Sucsarian: Sucsarian Dagger Drop")
    sucsarian_drop_2 = unique_drop("Sucsarian: Sucsarian Spear Drop")
    sucsarian_10c = other_drop("Sucsarian: Large Silver Drop")
    sucsarian_obsidian = other_drop("Sucsarian: Obsidian Drop")
    sucsarian_snowflake_obsidian = other_drop("Sucsarian: Snowflake Obsidian Drop")
    sucsarian_throwing_knife = other_drop("Sucsarian: Throwing Knife Drop")
    vesta_fairy_moss = other_drop("Vesta: Fairy Moss Drop")
    vesta_yellow_morel = other_drop("Vesta: Yellow Morel Drop")
    vesta_dest_angel = other_drop("Vesta: Destroying Angel Mushroom Drop")
    ceres_fairy_moss = other_drop("Ceres: Fairy Moss Drop")
    ceres_yellow_morel = other_drop("Ceres: Yellow Morel Drop")
    ceres_dest_angel = other_drop("Ceres: Destroying Angel Mushroom Drop")
    gloom_fairy_moss = other_drop("Gloom Wood: Fairy Moss Drop")
    gloom_health_vial = other_drop("Gloom Wood: Health Vial Drop")
    gloom_dest_angel = other_drop("Gloom Wood: Mana Vial Drop")
    #  Labyrinth of Ash
    cetea_drop = unique_drop("Cetea: Tornado Drop")
    cetea_10c = other_drop("Cetea: Medium Silver Drop")
    cetea_ocean_bone_shell = other_drop("Cetea: Ocean Bone Shell Drop")
    sanguis_book = unique_drop("Sanguis Umbra: Black Book Drop")

    starter_drops = [snail, snail_2c, snail_10c, snail_ocean, milk_snail, milk_5c, milk_10c,
    milk_ocean, shulker_obsidian, shulker_onyx, mummy_mana_vial, mummy_onyx, mummy_2c, mummy_10c, mummy_knight,
    mummy_knight_onyx, mummy_knight_10c, mummy_knight_5c]


all_drops = unique_drop_locations + other_drop_locations
all_drops_by_enemy: Dict[str, List[str]] = {}

for location in all_drops:
    location_split = location.split(": ")
    enemy = str(location_split[0])
    drop = str(location_split[1]).replace(" Drop", "")
    if enemy not in all_drops_by_enemy:
        all_drops_by_enemy[enemy] = [drop]
        continue
    all_drops_by_enemy[enemy].append(drop)


class Quench:
    brittle_arming_sword = "Quench Brittle Arming Sword"
    broken_hilt = "Quench Broken Hilt"
    broken_lance = "Quench Broken Lance"
    crossbow = "Quench Crossbow"
    elfen_sword = "Quench Elfen Sword"
    iron_claw = "Quench Iron Claw"
    iron_club = "Quench Iron Club"
    lyrian_longsword = "Quench Lyrian Longsword"
    obsidian_cursebrand = "Quench Obsidian Cursebrand"
    obsidian_poisonguard = "Quench Obsidian Poisonguard"
    obsidian_seal = "Quench Obsidian Seal"
    rapier = "Quench Rapier"
    replica_sword = "Quench Replica Sword"
    rusted_sword = "Quench Rusted Sword"
    shadow_blade = "Quench Shadow Blade"
    shining_blade = "Quench Shining Blade"
    steel_claw = "Quench Steel Claw"
    stone_club = "Quench Stone Club"
    torch = "Quench Torch"
    scythe = "Quench Death Scythe"

    all_quenches = [brittle_arming_sword, broken_hilt, broken_lance, crossbow, elfen_sword, iron_club, iron_claw, lyrian_longsword, obsidian_seal, obsidian_cursebrand,
                    obsidian_poisonguard, rapier, replica_sword, rusted_sword, shadow_blade, shining_blade, steel_claw, stone_club, torch, scythe]


class AlchemyLocation:
    explosives = "Alchemize Explosives"
    health = "Alchemize Healing Remedy"
    mana = "Alchemize Mana Remedy"
    warp = "Alchemize Unstable Stone"
    antidote = "Alchemize Antivenom"
    knife = "Alchemize Sharp Object"
    poison_knife = "Alchemize Venomous Object"
    moonlight = "Alchemize Concentrated Lunacy"
    fairy_moss = "Alchemize Nature"
    spectral = "Alchemize Hostility Barrier"
    wisp = "Alchemize Simple Life"
    limbo = "Alchemize Golden Sin of Abdul"
    banner = "Alchemize Cleromancy Tool"
    holy = "Alchemize Water of Life"
    poison_urn = "Alchemize Concentrated Poison"
    staff_of_osiris = "Alchemize Defense Construct"

    all_alchemy_locations = [explosives, health, mana, warp, antidote, knife, poison_knife, moonlight, fairy_moss, spectral, wisp,
                             limbo, banner, holy, poison_urn, staff_of_osiris]


class SpookyLocation:
    rest = "Demi's Spooky Treats"
    jellisha = "Jellisha's Jelly Treats"
    patchouli = "Patchouli's Poisoned Treats"
    le_fanu = "Crilall's Bloody Treats"
    daedalus = "Daedalus' Blackened Treats"
    lobos = "Lobos' Late Treats"
    lava = "Shery's Delectable Treats"
    spooky_spell = "Demi's Reward for All Soul Candies"
    headless_horseman = "Headless Horseman: Cavalry Saber Drop"

    candy_locations = [rest, jellisha, patchouli, le_fanu, daedalus, lobos, lava, spooky_spell]


class CrimpusLocation:
    wings_rest_present = "Christmas Present"
    yosei_patchouli_eggnog = "Patchouli's Yuletide Offering"

    christmas_locations = [yosei_patchouli_eggnog, wings_rest_present]


class StatLocation:
    stat_1 = "Stat Investment [1]"
    stat_2 = "Stat Investment [2]"
    stat_3 = "Stat Investment [3]"
    stat_4 = "Stat Investment [4]"
    stat_5 = "Stat Investment [5]"
    stat_6 = "Stat Investment [6]"
    stat_7 = "Stat Investment [7]"
    stat_8 = "Stat Investment [8]"
    stat_9 = "Stat Investment [9]"
    stat_10 = "Stat Investment [10]"
    stat_11 = "Stat Investment [11]"
    stat_12 = "Stat Investment [12]"
    stat_13 = "Stat Investment [13]"
    stat_14 = "Stat Investment [14]"
    stat_15 = "Stat Investment [15]"
    stat_16 = "Stat Investment [16]"
    stat_17 = "Stat Investment [17]"
    stat_18 = "Stat Investment [18]"
    stat_19 = "Stat Investment [19]"
    stat_20 = "Stat Investment [20]"
    stat_21 = "Stat Investment [21]"
    stat_22 = "Stat Investment [22]"
    stat_23 = "Stat Investment [23]"
    stat_24 = "Stat Investment [24]"
    stat_25 = "Stat Investment [25]"
    stat_26 = "Stat Investment [26]"
    stat_27 = "Stat Investment [27]"
    stat_28 = "Stat Investment [28]"
    stat_29 = "Stat Investment [29]"
    stat_30 = "Stat Investment [30]"
    stat_31 = "Stat Investment [31]"
    stat_32 = "Stat Investment [32]"
    stat_33 = "Stat Investment [33]"
    stat_34 = "Stat Investment [34]"
    stat_35 = "Stat Investment [35]"
    stat_36 = "Stat Investment [36]"
    stat_37 = "Stat Investment [37]"
    stat_38 = "Stat Investment [38]"
    stat_39 = "Stat Investment [39]"
    stat_40 = "Stat Investment [40]"
    stat_41 = "Stat Investment [41]"
    stat_42 = "Stat Investment [42]"
    stat_43 = "Stat Investment [43]"
    stat_44 = "Stat Investment [44]"
    stat_45 = "Stat Investment [45]"
    stat_46 = "Stat Investment [46]"
    stat_47 = "Stat Investment [47]"
    stat_48 = "Stat Investment [48]"
    stat_49 = "Stat Investment [49]"
    stat_50 = "Stat Investment [50]"
    stat_51 = "Stat Investment [51]"
    stat_52 = "Stat Investment [52]"
    stat_53 = "Stat Investment [53]"
    stat_54 = "Stat Investment [54]"
    stat_55 = "Stat Investment [55]"
    stat_56 = "Stat Investment [56]"
    stat_57 = "Stat Investment [57]"
    stat_58 = "Stat Investment [58]"
    stat_59 = "Stat Investment [59]"
    stat_60 = "Stat Investment [60]"
    stat_61 = "Stat Investment [61]"
    stat_62 = "Stat Investment [62]"
    stat_63 = "Stat Investment [63]"
    stat_64 = "Stat Investment [64]"
    stat_65 = "Stat Investment [65]"
    stat_66 = "Stat Investment [66]"
    stat_67 = "Stat Investment [67]"
    stat_68 = "Stat Investment [68]"
    stat_69 = "Stat Investment [69]"
    stat_70 = "Stat Investment [70]"
    stat_71 = "Stat Investment [71]"
    stat_72 = "Stat Investment [72]"
    stat_73 = "Stat Investment [73]"
    stat_74 = "Stat Investment [74]"
    stat_75 = "Stat Investment [75]"
    stat_76 = "Stat Investment [76]"
    stat_77 = "Stat Investment [77]"
    stat_78 = "Stat Investment [78]"
    stat_79 = "Stat Investment [79]"
    stat_80 = "Stat Investment [80]"
    stat_81 = "Stat Investment [81]"
    stat_82 = "Stat Investment [82]"
    stat_83 = "Stat Investment [83]"
    stat_84 = "Stat Investment [84]"
    stat_85 = "Stat Investment [85]"
    stat_86 = "Stat Investment [86]"
    stat_87 = "Stat Investment [87]"
    stat_88 = "Stat Investment [88]"
    stat_89 = "Stat Investment [89]"
    stat_90 = "Stat Investment [90]"
    stat_91 = "Stat Investment [91]"
    stat_92 = "Stat Investment [92]"
    stat_93 = "Stat Investment [93]"
    stat_94 = "Stat Investment [94]"
    stat_95 = "Stat Investment [95]"
    stat_96 = "Stat Investment [96]"
    stat_97 = "Stat Investment [97]"
    stat_98 = "Stat Investment [98]"
    stat_99 = "Stat Investment [99]"
    stat_100 = "Stat Investment [100]"
    stat_101 = "Stat Investment [101]"
    stat_102 = "Stat Investment [102]"
    stat_103 = "Stat Investment [103]"
    stat_104 = "Stat Investment [104]"
    stat_105 = "Stat Investment [105]"
    stat_106 = "Stat Investment [106]"
    stat_107 = "Stat Investment [107]"
    stat_108 = "Stat Investment [108]"
    stat_109 = "Stat Investment [109]"
    stat_110 = "Stat Investment [110]"
    stat_111 = "Stat Investment [111]"
    stat_112 = "Stat Investment [112]"
    stat_113 = "Stat Investment [113]"
    stat_114 = "Stat Investment [114]"
    stat_115 = "Stat Investment [115]"
    stat_116 = "Stat Investment [116]"
    stat_117 = "Stat Investment [117]"
    stat_118 = "Stat Investment [118]"
    stat_119 = "Stat Investment [119]"
    stat_120 = "Stat Investment [120]"
    stat_121 = "Stat Investment [121]"
    stat_122 = "Stat Investment [122]"
    stat_123 = "Stat Investment [123]"
    stat_124 = "Stat Investment [124]"
    stat_125 = "Stat Investment [125]"
    stat_126 = "Stat Investment [126]"
    stat_127 = "Stat Investment [127]"
    stat_128 = "Stat Investment [128]"
    stat_129 = "Stat Investment [129]"
    stat_130 = "Stat Investment [130]"
    stat_131 = "Stat Investment [131]"
    stat_132 = "Stat Investment [132]"
    stat_133 = "Stat Investment [133]"
    stat_134 = "Stat Investment [134]"
    stat_135 = "Stat Investment [135]"
    stat_136 = "Stat Investment [136]"
    stat_137 = "Stat Investment [137]"
    stat_138 = "Stat Investment [138]"
    stat_139 = "Stat Investment [139]"
    stat_140 = "Stat Investment [140]"
    stat_141 = "Stat Investment [141]"
    stat_142 = "Stat Investment [142]"
    stat_143 = "Stat Investment [143]"
    stat_144 = "Stat Investment [144]"
    stat_145 = "Stat Investment [145]"
    stat_146 = "Stat Investment [146]"
    stat_147 = "Stat Investment [147]"
    stat_148 = "Stat Investment [148]"
    stat_149 = "Stat Investment [149]"
    stat_150 = "Stat Investment [150]"
    stat_151 = "Stat Investment [151]"
    stat_152 = "Stat Investment [152]"
    stat_153 = "Stat Investment [153]"
    stat_154 = "Stat Investment [154]"
    stat_155 = "Stat Investment [155]"
    stat_156 = "Stat Investment [156]"
    stat_157 = "Stat Investment [157]"
    stat_158 = "Stat Investment [158]"
    stat_159 = "Stat Investment [159]"
    stat_160 = "Stat Investment [160]"
    stat_161 = "Stat Investment [161]"
    stat_162 = "Stat Investment [162]"
    stat_163 = "Stat Investment [163]"
    stat_164 = "Stat Investment [164]"
    stat_165 = "Stat Investment [165]"
    stat_166 = "Stat Investment [166]"
    stat_167 = "Stat Investment [167]"
    stat_168 = "Stat Investment [168]"
    stat_169 = "Stat Investment [169]"
    stat_170 = "Stat Investment [170]"
    stat_171 = "Stat Investment [171]"
    stat_172 = "Stat Investment [172]"
    stat_173 = "Stat Investment [173]"
    stat_174 = "Stat Investment [174]"
    stat_175 = "Stat Investment [175]"
    stat_176 = "Stat Investment [176]"
    stat_177 = "Stat Investment [177]"
    stat_178 = "Stat Investment [178]"
    stat_179 = "Stat Investment [179]"
    stat_180 = "Stat Investment [180]"
    stat_181 = "Stat Investment [181]"
    stat_182 = "Stat Investment [182]"
    stat_183 = "Stat Investment [183]"
    stat_184 = "Stat Investment [184]"
    stat_185 = "Stat Investment [185]"
    stat_186 = "Stat Investment [186]"
    stat_187 = "Stat Investment [187]"
    stat_188 = "Stat Investment [188]"
    stat_189 = "Stat Investment [189]"
    stat_190 = "Stat Investment [190]"
    stat_191 = "Stat Investment [191]"
    stat_192 = "Stat Investment [192]"
    stat_193 = "Stat Investment [193]"
    stat_194 = "Stat Investment [194]"
    stat_195 = "Stat Investment [195]"
    stat_196 = "Stat Investment [196]"
    stat_197 = "Stat Investment [197]"
    stat_198 = "Stat Investment [198]"
    stat_199 = "Stat Investment [199]"
    stat_200 = "Stat Investment [200]"
    stat_201 = "Stat Investment [201]"
    stat_202 = "Stat Investment [202]"
    stat_203 = "Stat Investment [203]"
    stat_204 = "Stat Investment [204]"
    stat_205 = "Stat Investment [205]"
    stat_206 = "Stat Investment [206]"
    stat_207 = "Stat Investment [207]"
    stat_208 = "Stat Investment [208]"
    stat_209 = "Stat Investment [209]"
    stat_210 = "Stat Investment [210]"
    stat_211 = "Stat Investment [211]"
    stat_212 = "Stat Investment [212]"
    stat_213 = "Stat Investment [213]"
    stat_214 = "Stat Investment [214]"
    stat_215 = "Stat Investment [215]"
    stat_216 = "Stat Investment [216]"
    stat_217 = "Stat Investment [217]"
    stat_218 = "Stat Investment [218]"
    stat_219 = "Stat Investment [219]"
    stat_220 = "Stat Investment [220]"
    stat_221 = "Stat Investment [221]"
    stat_222 = "Stat Investment [222]"
    stat_223 = "Stat Investment [223]"
    stat_224 = "Stat Investment [224]"
    stat_225 = "Stat Investment [225]"
    stat_226 = "Stat Investment [226]"
    stat_227 = "Stat Investment [227]"
    stat_228 = "Stat Investment [228]"
    stat_229 = "Stat Investment [229]"
    stat_230 = "Stat Investment [230]"
    stat_231 = "Stat Investment [231]"
    stat_232 = "Stat Investment [232]"
    stat_233 = "Stat Investment [233]"
    stat_234 = "Stat Investment [234]"
    stat_235 = "Stat Investment [235]"
    stat_236 = "Stat Investment [236]"
    stat_237 = "Stat Investment [237]"
    stat_238 = "Stat Investment [238]"
    stat_239 = "Stat Investment [239]"
    stat_240 = "Stat Investment [240]"
    stat_241 = "Stat Investment [241]"
    stat_242 = "Stat Investment [242]"
    stat_243 = "Stat Investment [243]"
    stat_244 = "Stat Investment [244]"
    stat_245 = "Stat Investment [245]"
    stat_246 = "Stat Investment [246]"
    stat_247 = "Stat Investment [247]"
    stat_248 = "Stat Investment [248]"
    stat_249 = "Stat Investment [249]"
    stat_250 = "Stat Investment [250]"
    stat_251 = "Stat Investment [251]"
    stat_252 = "Stat Investment [252]"
    stat_253 = "Stat Investment [253]"
    stat_254 = "Stat Investment [254]"
    stat_255 = "Stat Investment [255]"
    stat_256 = "Stat Investment [256]"
    stat_257 = "Stat Investment [257]"
    stat_258 = "Stat Investment [258]"
    stat_259 = "Stat Investment [259]"
    stat_260 = "Stat Investment [260]"
    stat_261 = "Stat Investment [261]"
    stat_262 = "Stat Investment [262]"
    stat_263 = "Stat Investment [263]"
    stat_264 = "Stat Investment [264]"
    stat_265 = "Stat Investment [265]"
    stat_266 = "Stat Investment [266]"
    stat_267 = "Stat Investment [267]"
    stat_268 = "Stat Investment [268]"
    stat_269 = "Stat Investment [269]"
    stat_270 = "Stat Investment [270]"
    stat_271 = "Stat Investment [271]"
    stat_272 = "Stat Investment [272]"
    stat_273 = "Stat Investment [273]"
    stat_274 = "Stat Investment [274]"
    stat_275 = "Stat Investment [275]"
    stat_276 = "Stat Investment [276]"
    stat_277 = "Stat Investment [277]"
    stat_278 = "Stat Investment [278]"
    stat_279 = "Stat Investment [279]"
    stat_280 = "Stat Investment [280]"
    stat_281 = "Stat Investment [281]"
    stat_282 = "Stat Investment [282]"
    stat_283 = "Stat Investment [283]"
    stat_284 = "Stat Investment [284]"
    stat_285 = "Stat Investment [285]"
    stat_286 = "Stat Investment [286]"
    stat_287 = "Stat Investment [287]"
    stat_288 = "Stat Investment [288]"
    stat_289 = "Stat Investment [289]"
    stat_290 = "Stat Investment [290]"
    stat_291 = "Stat Investment [291]"
    stat_292 = "Stat Investment [292]"
    stat_293 = "Stat Investment [293]"
    stat_294 = "Stat Investment [294]"
    stat_295 = "Stat Investment [295]"
    stat_296 = "Stat Investment [296]"
    stat_297 = "Stat Investment [297]"
    stat_298 = "Stat Investment [298]"
    stat_299 = "Stat Investment [299]"
    stat_300 = "Stat Investment [300]"
    stat_301 = "Stat Investment [301]"
    stat_302 = "Stat Investment [302]"
    stat_303 = "Stat Investment [303]"
    stat_304 = "Stat Investment [304]"
