from dataclasses import dataclass
from typing import List

from .. import LunacidRegion
from ..strings.enemies import Enemy
from ..strings.locations import all_drops_by_enemy


@dataclass(frozen=True)
class EnemyData:
    name: str
    drops: List[str]
    regions: List[str]

    def __repr__(self):
        return f"{self.name} (Drops: {self.drops}) (Regions: {self.regions}"


all_enemies: List[EnemyData] = []


def create_enemy(name: str, positions: List[str]):
    if name not in all_drops_by_enemy:
        drops = []
    else:
        drops = all_drops_by_enemy[name]
    enemy = EnemyData(name, drops, positions)
    all_enemies.append(enemy)
    return enemy


snail = create_enemy(Enemy.snail, [LunacidRegion.hollow_basin])
milk_snail = create_enemy(Enemy.milk_snail, [LunacidRegion.hollow_basin, LunacidRegion.forbidden_archives_3, LunacidRegion.forbidden_archives_1b])
shulker = create_enemy(Enemy.shulker, [LunacidRegion.hollow_basin])
mummy = create_enemy(Enemy.mummy, [LunacidRegion.temple_of_silence_interior])
mummy_knight = create_enemy(Enemy.mummy_knight, [LunacidRegion.temple_of_silence_interior, LunacidRegion.temple_of_silence_secret])
necronomicon = create_enemy(Enemy.necronomicon, [LunacidRegion.forbidden_archives_2, LunacidRegion.forbidden_archives_3, LunacidRegion.forbidden_archives_1b])
enlightened_one = create_enemy(Enemy.enlightened_one, [LunacidRegion.forbidden_archives_3, LunacidRegion.forbidden_archives_1b])
chimera = create_enemy(Enemy.chimera, [LunacidRegion.forbidden_archives_1b, LunacidRegion.forbidden_archives_3])
rat = create_enemy(Enemy.rat, [LunacidRegion.fetid_mire, LunacidRegion.fetid_mire_secret, LunacidRegion.terminus_prison_upstairs])
rat_king = create_enemy(Enemy.rat_king, [LunacidRegion.fetid_mire, LunacidRegion.vampire_tomb, LunacidRegion.terminus_prison_upstairs])
rat_queen = create_enemy(Enemy.rat_queen, [LunacidRegion.fetid_mire, LunacidRegion.terminus_prison_upstairs])
slime_skeleton = create_enemy(Enemy.slime_skeleton, [LunacidRegion.fetid_mire])
slime = create_enemy(Enemy.slime, [LunacidRegion.fetid_mire])
skeleton = create_enemy(Enemy.skeleton, [LunacidRegion.fetid_mire, LunacidRegion.mausoleum, LunacidRegion.boiling_grotto, LunacidRegion.terminus_prison_dark, LunacidRegion.accursed_tomb])
lunaga = create_enemy(Enemy.lunaga, [LunacidRegion.yosei_forest])
kodama = create_enemy(Enemy.kodama, [LunacidRegion.yosei_forest])
yakul = create_enemy(Enemy.yakul, [LunacidRegion.yosei_forest])
venus = create_enemy(Enemy.venus, [LunacidRegion.yosei_lower, LunacidRegion.yosei_forest, LunacidRegion.forest_canopy])
neptune = create_enemy(Enemy.neptune, [LunacidRegion.yosei_lower, LunacidRegion.forest_canopy])
unilateralis = create_enemy(Enemy.unilateralis, [LunacidRegion.forest_canopy])
tillandsia = create_enemy(Enemy.tillandsia, [LunacidRegion.forest_canopy, LunacidRegion.forlorn_arena])
mimic = create_enemy(Enemy.mimic, [LunacidRegion.boiling_grotto_secret])
devil_slime = create_enemy(Enemy.devil_slime, [LunacidRegion.fetid_mire])
hemalith = create_enemy(Enemy.hemalith, [LunacidRegion.sanguine_sea])
mare = create_enemy(Enemy.mare, [LunacidRegion.accursed_tomb])
mi_go = create_enemy(Enemy.mi_go, [LunacidRegion.accursed_tomb])
phantom = create_enemy(Enemy.phantom, [LunacidRegion.mausoleum, LunacidRegion.castle_le_fanu, LunacidRegion.castle_le_fanu_white])
cursed_painting = create_enemy(Enemy.cursed_painting, [LunacidRegion.accursed_tomb, LunacidRegion.castle_le_fanu_blue])
malformed = create_enemy(Enemy.malformed, [LunacidRegion.vampire_tomb, LunacidRegion.castle_le_fanu_blue, LunacidRegion.castle_le_fanu_red])
poltergeist = create_enemy(Enemy.poltergeist, [LunacidRegion.castle_le_fanu_blue])
giant_bat = create_enemy(Enemy.giant_bat, [LunacidRegion.castle_le_fanu_white, LunacidRegion.castle_le_fanu_blue])
vampire = create_enemy(Enemy.vampire, [LunacidRegion.castle_le_fanu_red])
vampire_page = create_enemy(Enemy.vampire, [LunacidRegion.castle_le_fanu_red, LunacidRegion.castle_le_fanu_white])
malformed_horse = create_enemy(Enemy.malformed_horse, [LunacidRegion.sealed_ballroom])
hallowed_husk = create_enemy(Enemy.hallowed_husk, [LunacidRegion.sealed_ballroom, LunacidRegion.sealed_ballroom_secret, LunacidRegion.holy_seat_of_gold])
ikurrilb = create_enemy(Enemy.ikurrilb, [LunacidRegion.boiling_grotto])
obsidian_skeleton = create_enemy(Enemy.obsidian_skeleton, [LunacidRegion.boiling_grotto, LunacidRegion.terminus_prison_dark, LunacidRegion.labyrinth_of_ash])
serpent = create_enemy(Enemy.serpent, [LunacidRegion.sand_temple])
anpu = create_enemy(Enemy.anpu, [LunacidRegion.sand_temple])
embalmed = create_enemy(Enemy.embalmed, [LunacidRegion.sand_temple])
lunam = create_enemy(Enemy.lunam, [LunacidRegion.terminus_prison_dark])
jailor = create_enemy(Enemy.jailor, [LunacidRegion.terminus_prison, LunacidRegion.terminus_prison_upstairs])
lupine_skeleton = create_enemy(Enemy.lupine_skeleton, [LunacidRegion.terminus_prison_upstairs, LunacidRegion.terminus_prison_dark])
giant_skeleton = create_enemy(Enemy.giant_skeleton, [LunacidRegion.terminus_prison_dark])
sucsarian = create_enemy(Enemy.sucsarian, [LunacidRegion.forlorn_arena])
ceres = create_enemy(Enemy.ceres, [LunacidRegion.forlorn_arena])
vesta = create_enemy(Enemy.vesta, [LunacidRegion.forlorn_arena])
gloom_wood = create_enemy(Enemy.gloom_wood, [LunacidRegion.forlorn_arena])
cetea = create_enemy(Enemy.cetea, [LunacidRegion.labyrinth_of_ash])


all_enemies_by_name = {}

for enemy in all_enemies:
    all_enemies_by_name[enemy.name] = enemy
