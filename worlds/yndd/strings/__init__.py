from .items import GoalItems
from .locations import Streets, Mall, Docks, Wilderness, School, Snow, Sewer

vanilla_egg_placement = {
    Streets.egg: GoalItems.street_egg,
    Mall.egg: GoalItems.mall_egg,
    Docks.egg: GoalItems.docks_egg,
    Wilderness.egg: GoalItems.wilderness_egg,
    School.egg: GoalItems.school_egg,
    Snow.egg: GoalItems.sewers_egg,
}

vanilla_jellyfish_placement = {
    Streets.jellyfish: GoalItems.street_jellyfish,
    Mall.jellyfish: GoalItems.mall_jellyfish,
    Docks.jellyfish: GoalItems.docks_jellyfish,
    Wilderness.jellyfish: GoalItems.wilderness_jellyfish,
    School.jellyfish: GoalItems.school_jellyfish,
    Sewer.jellyfish: GoalItems.sewers_jellyfish,
}
