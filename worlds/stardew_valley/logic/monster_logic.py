from typing import Iterable, Union

from .combat_logic import CombatLogic
from .region_logic import RegionLogic
from .time_logic import TimeLogic, MAX_MONTHS
from ..data.monster_data import StardewMonster, all_monsters_by_name
from ..stardew_rule import StardewRule, Or, And


class MonsterLogic:
    player: int
    region: RegionLogic
    time: TimeLogic
    combat: CombatLogic

    def __init__(self, player: int, region: RegionLogic, time: TimeLogic, combat: CombatLogic):
        self.player = player
        self.region = region
        self.time = time
        self.combat = combat

    def can_kill(self, monster: Union[str, StardewMonster], amount_tier: int = 0) -> StardewRule:
        if isinstance(monster, str):
            monster = all_monsters_by_name[monster]
        region_rule = self.region.can_reach_any(monster.locations)
        combat_rule = self.combat.can_fight_at_level(monster.difficulty)
        if amount_tier <= 0:
            amount_tier = 0
        time_rule = self.time.has_lived_months(amount_tier * 2)
        return region_rule & combat_rule & time_rule

    def can_kill_max(self, monster: StardewMonster) -> StardewRule:
        return self.can_kill(monster, MAX_MONTHS)

    def can_kill_any(self, monsters: Iterable[StardewMonster], amount_tier: int = 0) -> StardewRule:
        rules = [self.can_kill(monster, amount_tier) for monster in monsters]
        return Or(rules)

    def can_kill_all(self, monsters: Iterable[StardewMonster], amount_tier: int = 0) -> StardewRule:
        rules = [self.can_kill(monster, amount_tier) for monster in monsters]
        return And(rules)
