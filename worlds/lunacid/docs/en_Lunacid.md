# Lunacid

## Where is the settings page?
The [player settings page for this game](../player-settings) contains all the options you need to configure and export a
config file.

## What does randomization do to this game?
The game's randomization changes the base game by
- removing the initial barrier at the start of the game,
- shuffling starting class and weapon,
- allowing shuffling entrances,
- choosing whether or not to lock doors or switches unless an item is obtained, 
- selecting which ending is necessary for victory,
- determining how many Strange Coins are required to complete Ending B,
- giving yourself more experience gain rates,
- giving the Dusty Crystal Orb a purpose by potentially locking hidden walls,

among other settings.

## What items and locations get shuffled?
The base settings shuffle:
- all normal item pickup locations scattered around the world,
- the strange coin locations,
- gifts given to the player by Demi and Clive,
- the spells given to you by Daedalus,

With additional settings:
- shuffle all drops enemies drop,
- removing either Tower of Abyss or Coin locations from your game,

with more planned as time moves on. 

Items shuffled depend on your settings, but can include:
- Weapons.
- Spells.
- Key items (Vampiric Symbols, Terminus Prison Key, etc).
- Voucher items that reduce the cost of items to 0.
- Crafted goods (Health Vials, Bombs, Throwing Knives).
- Rare drops (Angelic Feather, Pink Shrimp).


## When the player receives an item, what happens?
When the player receives an item, it will be displayed on the client.  The item's
name is colored to help determine its progression value.

## How does the Gifting system work in Lunacid?
This is a setting that currently only works with dropsanity, but later will work
for alchemy.  If the following conditions are met, you are allowed to continuously
farm Archipelago items:
- The other game has opted into the gifting system (up to developer to add it).
- If the game is not Stardew Valley, the item must not be progression.
- If the game is Stardew Valley, it has to be a basic "Object" from that game (not
furniture, weapons, hats, and so on).
- The initial drop was already found.

When this occurs, the drop item name will be colored olive green and it will say the
item is gifted.

## Known quirks
- Sometimes when being sent key items to open doors, they might not work if you 
are still in the same area.  A reload should fix this.
- When connecting, the slot name is case sensitive; the font used by the game 
obscures this as it is always in upper case.
- If the game does not get past a connect, its likely that the server has winded down,
or there is a version mismatch.  Check the LogOutut of BepInEx if you aren't sure.
- If the game's port changes, you can edit the save's JSON file to change the port.