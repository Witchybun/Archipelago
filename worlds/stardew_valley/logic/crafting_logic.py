from .has_logic import HasLogic
from .money_logic import MoneyLogic
from .received_logic import ReceivedLogic
from .region_logic import RegionLogic
from .relationship_logic import RelationshipLogic
from .skill_logic import SkillLogic
from .special_order_logic import SpecialOrderLogic
from .time_logic import TimeLogic
from .. import options
from ..data.craftable_data import CraftingRecipe
from ..data.recipe_data import RecipeSource, StarterSource, ShopSource, SkillSource, FriendshipSource
from ..data.recipe_source import CutsceneSource, ShopTradeSource, ArchipelagoSource, LogicSource, SpecialOrderSource, FestivalShopSource
from ..options import Craftsanity, FestivalLocations, SpecialOrderLocations
from ..stardew_rule import StardewRule, True_, False_, And
from ..strings.region_names import Region


class CraftingLogic:
    player: int
    craftsanity_option: Craftsanity
    festivals_option: FestivalLocations
    special_orders_option: SpecialOrderLocations
    received: ReceivedLogic
    has: HasLogic
    region: RegionLogic
    time: TimeLogic
    money: MoneyLogic
    relationship: RelationshipLogic
    skill: SkillLogic
    special_orders: SpecialOrderLogic

    def __init__(self, player: int, craftsanity_option: Craftsanity, festivals_option: FestivalLocations, special_orders_option: SpecialOrderLocations, received: ReceivedLogic, has: HasLogic, region: RegionLogic,
                 time: TimeLogic, money: MoneyLogic, relationship: RelationshipLogic, skill: SkillLogic, special_orders: SpecialOrderLogic):
        self.player = player
        self.craftsanity_option = craftsanity_option
        self.festivals_option = festivals_option
        self.special_orders_option = special_orders_option
        self.received = received
        self.has = has
        self.region = region
        self.time = time
        self.money = money
        self.relationship = relationship
        self.skill = skill
        self.special_orders = special_orders

    def can_craft(self, recipe: CraftingRecipe = None) -> StardewRule:
        craft_rule = True_()
        if recipe is None:
            return craft_rule

        learn_rule = self.knows_recipe(recipe)
        ingredients_rule = And([self.has(ingredient) for ingredient in recipe.ingredients])
        number_ingredients = sum(recipe.ingredients[ingredient] for ingredient in recipe.ingredients) // 10
        time_rule = self.time.has_lived_months(number_ingredients)
        return craft_rule & learn_rule & ingredients_rule & time_rule

    def knows_recipe(self, recipe: CraftingRecipe) -> StardewRule:
        if isinstance(recipe.source, ArchipelagoSource):
            return self.received(recipe.source.ap_item, len(recipe.source.ap_item))
        if isinstance(recipe.source, FestivalShopSource):
            if self.festivals_option == options.FestivalLocations.option_disabled:
                return self.can_learn_recipe(recipe)
            else:
                return self.received_recipe(recipe.item)
        if self.craftsanity_option == Craftsanity.option_none:
            return self.can_learn_recipe(recipe)
        if isinstance(recipe.source, StarterSource) or isinstance(recipe.source, ShopTradeSource) or isinstance(recipe.source, ShopSource):
            return self.received_recipe(recipe.item)
        if isinstance(recipe.source, SpecialOrderSource) and self.special_orders_option != SpecialOrderLocations.option_disabled:
            return self.received_recipe(recipe.item)
        return self.can_learn_recipe(recipe)

    def can_learn_recipe(self, recipe: CraftingRecipe) -> StardewRule:
        if isinstance(recipe.source, StarterSource):
            return True_()
        if isinstance(recipe.source, ArchipelagoSource):
            return self.received(recipe.source.ap_item, len(recipe.source.ap_item))
        if isinstance(recipe.source, ShopTradeSource):
            return self.money.can_trade_at(recipe.source.region, recipe.source.currency, recipe.source.price)
        if isinstance(recipe.source, ShopSource):
            return self.money.can_spend_at(recipe.source.region, recipe.source.price)
        if isinstance(recipe.source, SkillSource):
            return self.skill.has_level(recipe.source.skill, recipe.source.level)
        if isinstance(recipe.source, CutsceneSource):
            return self.region.can_reach(recipe.source.region) & self.relationship.has_hearts(recipe.source.friend, recipe.source.hearts)
        if isinstance(recipe.source, FriendshipSource):
            return self.relationship.has_hearts(recipe.source.friend, recipe.source.hearts)
        if isinstance(recipe.source, SpecialOrderSource):
            if self.special_orders_option == SpecialOrderLocations.option_disabled:
                return self.special_orders.can_complete_special_order(recipe.source.special_order)
            return self.received_recipe(recipe.item)
        if isinstance(recipe.source, LogicSource):
            if recipe.source.logic_rule == "Cellar":
                return self.region.can_reach(Region.cellar)

        return False_()

    def received_recipe(self, item_name: str):
        return self.received(f"{item_name} Recipe")