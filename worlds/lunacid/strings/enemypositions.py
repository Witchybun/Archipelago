from dataclasses import dataclass
from random import Random
from typing import Dict, List, Tuple

from worlds.lunacid import LunacidRegion
from worlds.lunacid.strings.enemies import Enemy


@dataclass(frozen=True)
class EnemyPlacement:
    scene: str  # Used for the mod to determine which scene this applies to
    group_name: str  # Used for the mod to determine which group is to be targeted
    child_id: int  # Used for the mod to determine which enemy in the group is to be replaced
    enemy: str
    region: str


@dataclass(frozen=True)
class ModData:
    group_name: str  # Used for the mod to determine which group is to be targeted
    child_id: int  # Used for the mod to determine which enemy in the group is to be replaced
    enemy: str



base_enemy_placement = [
    # Hollow Basin
    EnemyPlacement("PITT_A1", "SmallGroupPittA1", 0, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "SmallGroupPittA1", 1, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "SmallGroupPittA1", 2, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "SmallGroupPittA1", 3, Enemy.mummy, LunacidRegion.temple_of_silence_secret),

    EnemyPlacement("PITT_A1", "StartSnailPittA1", 0, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "StartSnailPittA1", 1, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "StartSnailPittA1", 2, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "StartSnailPittA1", 3, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "StartSnailPittA1", 4, Enemy.mummy, LunacidRegion.temple_of_silence_secret),

    EnemyPlacement("PITT_A1", "MainPittA1", 6, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 7, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 8, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 9, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 10, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 11, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 12, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 13, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 14, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 15, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 16, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 17, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "MainPittA1", 18, Enemy.mummy, LunacidRegion.temple_of_silence_secret),

    EnemyPlacement("PITT_A1", "HiddenPittA1", 0, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 1, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 2, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 3, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 4, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 5, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 6, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 7, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 8, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "HiddenPittA1", 9, Enemy.mummy, LunacidRegion.temple_of_silence_secret),

    EnemyPlacement("PITT_A1", "CrawlingPittA1", 0, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 1, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 2, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 3, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 4, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 5, Enemy.mummy, LunacidRegion.temple_of_silence_secret),
    EnemyPlacement("PITT_A1", "CrawlingPittA1", 6, Enemy.mummy, LunacidRegion.temple_of_silence_secret),

    # Yosei Forest
    EnemyPlacement("FOREST_A1", "LowerFrontForestA1", 0, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerFrontForestA1", 1, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerFrontForestA1", 2, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerFrontForestA1", 3, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerFrontForestA1", 4, Enemy.mummy, LunacidRegion.yosei_forest),

    EnemyPlacement("FOREST_A1", "LowerBackYakulForestA1", 0, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackYakulForestA1", 1, Enemy.mummy, LunacidRegion.yosei_forest),

    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 0, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 1, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 2, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 3, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 4, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "LowerBackBunForestA1", 5, Enemy.mummy, LunacidRegion.yosei_forest),

    EnemyPlacement("FOREST_A1", "MainForestA1", 3, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 4, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 5, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 6, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 10, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 11, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 12, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 13, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 14, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 15, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 16, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 17, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 18, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 19, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 20, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 21, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 22, Enemy.mummy, LunacidRegion.yosei_forest),
    EnemyPlacement("FOREST_A1", "MainForestA1", 23, Enemy.mummy, LunacidRegion.yosei_forest),

    # The Fetid Mire
    EnemyPlacement("SEWER_A1", "MainSewerA1", 0, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 1, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 2, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 3, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 4, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 5, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 6, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 7, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 8, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 9, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 10, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 11, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 12, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 13, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 14, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 15, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 16, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 17, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 18, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 19, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 20, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 21, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 22, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 23, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 24, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 25, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 26, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 27, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 28, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 29, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 30, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 31, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 32, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 33, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 34, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 35, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 36, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 37, Enemy.rat, LunacidRegion.fetid_mire),
    EnemyPlacement("SEWER_A1", "MainSewerA1", 38, Enemy.rat, LunacidRegion.fetid_mire),

    # Forest Canopy
    EnemyPlacement("FOREST_B1", "NestForestB1", 0, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "NestForestB1", 1, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "NestForestB1", 2, Enemy.venus, LunacidRegion.forest_canopy),

    EnemyPlacement("FOREST_B1", "MainForestB1", 2, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 3, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 4, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 5, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 6, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 7, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 8, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 9, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 10, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 11, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 12, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 13, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 14, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 15, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 16, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 17, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 18, Enemy.venus, LunacidRegion.forest_canopy),
    EnemyPlacement("FOREST_B1", "MainForestB1", 19, Enemy.venus, LunacidRegion.forest_canopy),

]

enemy_to_enemy_placement: Dict[str, List[EnemyPlacement]] = {}


def randomize_enemies(random: Random) -> Tuple[Dict[str, List[ModData]], Dict[str, List[str]]]:
    chosen_enemies = []
    enemy_counts = {}
    randomized_enemy_placement = []
    for enemy_data in base_enemy_placement:
        picked_enemy = random.choice(Enemy.randomizable_enemies)
        new_data = EnemyPlacement(enemy_data.scene, enemy_data.group_name, enemy_data.child_id, picked_enemy, enemy_data.region)
        if picked_enemy not in chosen_enemies:
            chosen_enemies.append(picked_enemy)
        if picked_enemy not in enemy_counts:
            enemy_counts[picked_enemy] = 1
        else:
            enemy_counts[picked_enemy] += 1
        if picked_enemy in enemy_to_enemy_placement:
            enemy_to_enemy_placement[picked_enemy].append(new_data)
        else:
            enemy_to_enemy_placement[picked_enemy] = [new_data]
        randomized_enemy_placement.append(new_data)
    while chosen_enemies.sort() != Enemy.randomizable_enemies.sort():
        acceptable_enemies = [enemy for enemy in enemy_counts if enemy_counts[enemy] > 1]
        for checked_enemy in Enemy.randomizable_enemies:
            if checked_enemy not in chosen_enemies:
                random_enemy = random.choice(acceptable_enemies)
                random_data = random.choice(enemy_to_enemy_placement[random_enemy])
                enemy_to_enemy_placement[random_enemy].remove(random_data)
                randomized_enemy_placement.remove(random_data)
                enemy_counts[random_enemy] -= 1
                new_data = EnemyPlacement(random_data.scene, random_data.group_name, random_data.child_id, checked_enemy, random_data.region)
                enemy_to_enemy_placement[checked_enemy] = [new_data]
                enemy_counts[checked_enemy] = 1
                randomized_enemy_placement.append(new_data)
                chosen_enemies.append(checked_enemy)
    mod_data = construct_flag_data_for_mod(randomized_enemy_placement)
    enemy_dictionary = construct_enemy_dictionary(randomized_enemy_placement)
    return mod_data, enemy_dictionary


def construct_flag_data_for_mod(enemy_data: List[EnemyPlacement]) -> Dict[str, List[ModData]]:
    mod_package = {}
    for enemy in enemy_data:
        if enemy.scene not in mod_package:
            mod_package[enemy.scene] = [ModData(enemy.group_name, enemy.child_id, enemy.enemy)]
        else:
            mod_package[enemy.scene].append(ModData(enemy.group_name, enemy.child_id, enemy.enemy))
    return mod_package


def construct_enemy_dictionary(enemy_data: List[EnemyPlacement]) -> Dict[str, List[str]]:
    enemy_to_regions: Dict[str, List[str]] = {}
    for data in enemy_data:
        if data.enemy in enemy_to_regions:
            if data.region not in enemy_to_regions[data.enemy]:
                enemy_to_regions[data.enemy].append(data.region)
        else:
            enemy_to_regions[data.enemy] = [data.region]
    return enemy_to_regions
