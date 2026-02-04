from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Toggle, DeathLink


class Campaign(Choice):
    """Which campaign is played and is required for goal.
    If the option is both, both endings must be reached and completed."""
    internal_name = "campaign"
    display_name = "Campaign"
    option_jebidiah = 0
    option_jeeb = 1
    option_both = 2
    default = 0

class RandomizeCameraKnife(Toggle):
    """The Camera for Jebidiah and the Butcher's Knife for Jeeb are required to complete levels.
    If this is on, goaling most levels is not possible until you get them."""
    internal_name = "randomize_camera_knife"
    display_name = "Randomize Camera and Knife"

class Photographer(Toggle):
    """Each picture taken is a check, and the photos are items.
    Only relevant if Jebidiah's campaign is playable."""
    internal_name = "photographer"
    display_name = "Photographer"


class BBQChef(Toggle):
    """Collecting meat is a check, and meat per level is an item.
    Only relevant if Jeeb's campaign is playable."""
    internal_name = "bbq_chef"
    display_name = "BBQ Chef"

class Hyenas(Toggle):
    """Destroying every Hyena is a location, and each one is an item, for the given campaigns."""
    internal_name = "hyenas"
    display_name = "Hyenas"

class RogueScholar(Toggle):
    """Reading books, notes, and the like with some lore benefit are checks."""
    internal_name = "rogue_scholar"
    display_name = "Rogue Scholar"


@dataclass
class UktenaOptions(PerGameCommonOptions):
    campaign: Campaign
    randomize_camera_knife: RandomizeCameraKnife
    photographer: Photographer
    bbq_chef: BBQChef
    hyenas: Hyenas
    rogue_scholar: RogueScholar
    death_link: DeathLink
