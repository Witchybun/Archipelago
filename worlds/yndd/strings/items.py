class Glitch:
    glitch = "Glitched Item"

class Abilities:
    knife = "Knife"
    hamsa = "Hamsa"
    flute = "Flute"
    umbrella = "Umbrella"
    lantern = "Lantern"
    hat_scarf = "Hat and Scarf"
    uboa_mask = "Mask of Fear"

class Movement:
    jump = "Lower Body Strength"
    climb = "Upper Body Strength"
    run = "Improved Stamina"

    movement_to_item = {
        "Jump": jump,
        "Climb": climb,
        "Run": run
    }

class GoalItems:
    street_egg = "Street Egg"
    street_jellyfish = "Street Jellyfish"
    wilderness_egg = "Wilderness Egg"
    wilderness_jellyfish = "Wilderness Jellyfish"
    docks_egg = "Docks Egg"
    docks_jellyfish = "Docks Jellyfish"
    mall_egg = "Mall Egg"
    mall_jellyfish = "Mall Jellyfish"
    school_egg = "School Egg"
    school_jellyfish = "School Jellyfish"
    sewers_egg = "Sewers Egg"
    sewers_jellyfish = "Sewers Jellyfish"

    eggs = [street_egg, wilderness_egg, docks_egg, mall_egg, school_egg, sewers_egg]
    jellyfish = [street_jellyfish, wilderness_jellyfish, docks_jellyfish, mall_jellyfish, school_jellyfish, sewers_jellyfish]

class NexusDoors:
    street = "Streets Key"
    wilderness = "Wilderness Key"
    docks = "Docks Key"
    mall = "Mall Key"
    school = "School Key"
    sewer = "Sewers Key"

    door_to_key = {
        "Streets": street,
        "Wilderness": wilderness,
        "Docks": docks,
        "Mall": mall,
        "School": school,
        "Sewers": sewer,
    }

class ConnectorKeys:
    street_to_sewers = "Street Workers' Manhole Key"
    wilderness_to_sewers = "Well Rope"
    wilderness_to_docks = "Special Train Ticket"
    mall_to_sewers = "Mall Security Manhole Key"


class NasuItem:
    nasu_get = "Unlock Nasu Get <3"
    doubler = "Nasu Point Doubler Cheat Code"
    starting_points = "Starting Points + 100"

class AoOniItem:
    key = "Room Key"
    mansion_key = "Mansion Key"
    poniko = "Poniko"
    monoko = "Monoko"
    monoe = "Monoe"
    doll = "Doll"
    handkerchief = "Handkerchief"
    lighter = "Lighter"

class WitchAdventureItem:
    heart_container = "Heart Container"
    heal_unlock = "Witch Heal Unlock"

class Game:
    nasu = "Nasu Game Cartridge"
    ao_oni = "Dirty Game Cartridge"
    witch_adventure = "Mysterious Game Cartridge"


class Songs:
    oman = "Song of O Man"
    bagu = "Song of the Bagu"
    train = "Red Eye's Song"
    finale = "Requiem of The Ending"

class WildernessItem:
    red_eye = "Red Eye"
    death = "Death Glyph"
    moon = "Moon Glyph"
    sun = "Sun Glyph"
    war = "War Glyph"
    kalimba = "Kalimba"
    kite = "Kite"

class DockItem:
    yen = "10 Yen Coin"
    boards = "Wood Plank"
    blood_bag = "Blood Bag"
    sad_fish = "Sad Fish"

class MallItem:
    warehouse_key = "Warehouse Key"
    valve = "Valve"
    rooftop_key = "Rooftop Key"

class SchoolItem:
    photo = "Photo Fragment"
    books = "Stack of Books"
    brush = "Brush"
    triangle = "Triangle"
    key = "Bathroom Key"
    lever = "Lever"

class BlockItem:
    girl = "Progressive Block"

class ApartmentItem:
    key = "Rusty Key"

class Filler:
    nothing = "Nothing"

class Trap:
    pinch = "Pinch Trap"
