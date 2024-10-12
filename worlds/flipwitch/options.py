from dataclasses import dataclass

from Options import Toggle, Choice, DefaultOnToggle, Range, PerGameCommonOptions, StartInventoryPool


class StartingGender(Choice):
    """Decides the starting gender state."""
    internal_name = "starting_gender"
    display_name = "Starting Gender"
    option_female = 0
    option_male = 1
    default = 0


class ShuffleChaosPieces(Toggle):
    """Shuffles the six Chaos Pieces in your game.
    Off: All pieces are placed in their original locations.
    On: All six Chaos Pieces can be found anywhere in the multiworld.
    If you want to plando these, turn this on first.
    """
    internal_name = "shuffle_chaos_pieces"
    display_name = "Shuffle Chaos Pieces"


class ShopPrices(Range):
    """Sets, as a percentage, the price of all goods in the game."""
    internal_name = "shop_prices"
    display_name = "Shop Prices"
    range_start = 0
    range_end = 200
    default = 100


class Gachapon(Toggle):
    """Shuffles the rewards of the gachapon rewards."""
    internal_name = "gachapon"
    display_name = "Gachapon"


class CrystalTeleports(Toggle):
    """Shuffles the crystal teleports.  Item is obtained by interacting with a teleport panel.
    This doesn't do anything right now."""
    internal_name = "crystal_teleports"
    display_name = "Crystal Teleports"


class FuckLink(Toggle):
    """When you get fucked, everyone gets fucked (or dies, I suppose). Of course the reverse is true too."""
    display_name = "FuckLink"


@dataclass
class FlipwitchOptions(PerGameCommonOptions):
    starting_gender: StartingGender
    shuffle_chaos_pieces: ShuffleChaosPieces
    shop_prices: ShopPrices
    gachapon: Gachapon
    crystal_teleports: CrystalTeleports
    death_link: FuckLink
