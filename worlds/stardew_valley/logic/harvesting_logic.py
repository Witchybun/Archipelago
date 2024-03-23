from functools import cached_property
from typing import Union

from Utils import cache_self1
from .base_logic import BaseLogicMixin, BaseLogic
from .has_logic import HasLogicMixin
from .received_logic import ReceivedLogicMixin
from .region_logic import RegionLogicMixin
from .season_logic import SeasonLogicMixin
from .tool_logic import ToolLogicMixin
from ..data.harvest import ForagingSource
from ..stardew_rule import StardewRule
from ..strings.ap_names.community_upgrade_names import CommunityUpgrade
from ..strings.region_names import Region
from ..strings.tool_names import Tool


class HarvestingLogicMixin(BaseLogicMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.harvesting = HarvestingLogic(*args, **kwargs)


class HarvestingLogic(BaseLogic[Union[HarvestingLogicMixin, HasLogicMixin, ReceivedLogicMixin, RegionLogicMixin, SeasonLogicMixin, ToolLogicMixin]]):

    @cached_property
    def can_harvest_from_fruit_bats(self) -> StardewRule:
        return self.logic.region.can_reach(Region.farm_cave) & self.logic.received(CommunityUpgrade.fruit_bats)

    @cached_property
    def can_harvest_from_mushroom_cave(self) -> StardewRule:
        return self.logic.region.can_reach(Region.farm_cave) & self.logic.received(CommunityUpgrade.mushroom_boxes)

    @cache_self1
    def can_forage_from(self, source: ForagingSource):
        seasons_rule = self.logic.season.has_any(source.seasons)
        regions_rule = self.logic.region.can_reach_any(source.regions)
        hoe_rule = self.logic.tool.has_tool(Tool.hoe)
        return self.logic.and_(seasons_rule, regions_rule, hoe_rule)