from typing import Tuple, List, Dict

from worlds.uktena64.data.locations import UktenaLocation, jeb_base_locations, jeeb_base_locations, jeb_lore_locations, jeeb_lore_locations, \
    jeb_photo_locations, jeeb_meat_locations, hyena_locations, all_locations
from worlds.uktena64.options import UktenaOptions
from worlds.uktena64.strings.locations import Hyena, JebCabin, TheBBQBasket
from worlds.uktena64.strings.regions import JebRegion, JeebRegion

location_table = all_locations
locations_by_name: Dict[str, UktenaLocation] = {location.name: location for location in location_table}

def create_locations(options: UktenaOptions) -> Tuple[List[UktenaLocation], Dict[str, List[UktenaLocation]]]:
    locations = []
    event_locations = {}
    create_jeb_locations(options, locations, event_locations)
    create_jeeb_locations(options, locations, event_locations)
    create_lore_locations(options, locations)
    create_photo_locations(options, locations, event_locations)
    create_meat_locations(options, locations, event_locations)
    create_hyena_locations(options, locations)
    return locations, event_locations

def create_jeb_locations(options: UktenaOptions, locations: List[UktenaLocation], events: Dict[str, List[UktenaLocation]]):
    if options.campaign == options.campaign.option_jeeb:
        return locations
    for location in jeb_base_locations:
        locations.append(location)
    return locations, events

def create_jeeb_locations(options: UktenaOptions, locations: List[UktenaLocation], events: Dict[str, List[UktenaLocation]]):
    if options.campaign == options.campaign.option_jebidiah:
        return locations
    for location in jeeb_base_locations:
        locations.append(location)
    return locations, events

def create_lore_locations(options: UktenaOptions, locations: List[UktenaLocation]):
    if options.rogue_scholar and options.campaign != options.campaign.option_jeeb:
        for location in jeb_lore_locations:
            locations.append(location)
    if options.rogue_scholar and options.campaign != options.campaign.option_jebidiah:
        for location in jeeb_lore_locations:
            locations.append(location)
    return locations

def create_photo_locations(options: UktenaOptions, locations: List[UktenaLocation], events: Dict[str, List[UktenaLocation]]):
    if options.campaign == options.campaign.option_jeeb:
        return locations, events
    photo_state = options.photographer
    for location in jeb_photo_locations:
        if photo_state:
            locations.append(location)
        else:
            if location.region not in events:
                events[location.region] = []
            events[location.region].append(location)
    return locations, events

def create_meat_locations(options: UktenaOptions, locations: List[UktenaLocation], events: Dict[str, List[UktenaLocation]]):
    if options.campaign == options.campaign.option_jebidiah:
        return locations, events
    meat_state = options.bbq_chef
    for location in jeeb_meat_locations:
        if meat_state:
            locations.append(location)
        else:
            if location.region not in events:
                events[location.region] = []
            events[location.region].append(location)
    return locations, events

def create_hyena_locations(options: UktenaOptions, locations: List[UktenaLocation]) -> List[UktenaLocation]:
    if not options.hyenas:
        return locations
    jeb_state = options.campaign != options.campaign.option_jeeb
    jeeb_state = options.campaign != options.campaign.option_jebidiah
    for location in hyena_locations:
        if location.name in Hyena.jeb_hyena and jeb_state:
            locations.append(location)
            continue
        if location.name in Hyena.jeeb_hyena and jeeb_state:
            locations.append(location)
    return locations

