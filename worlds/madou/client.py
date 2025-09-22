import logging
import struct
import typing
import random
from typing import TYPE_CHECKING

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient

from .data.item_data import hex_data_by_item
from .data.location_data import hex_by_location

if TYPE_CHECKING:
    from SNIClient import SNIContext

snes_logger = logging.getLogger("SNES")

ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

MADOU_ROMHASH_START = 0x7FC0
ROMHASH_SIZE = 0x15

MADOU_INVENTORY = 0x001309
MADOU_INVENTORY_LENGTH = 0x2A
MADOU_INVENTORY_COUNT = 0x001333
MADOU_SAVE = 0x001334
MADOU_SAVE_LENGTH = 0x7F
MADOU_BESTIARY = 0x0013A8
MADOU_BESTIARY_LENGTH = 0x22
MADOU_HEALTH = 0x001346
MADOU_TOOLS = 0x0013C8
MADOU_LENGTH = 0x06
MADOU_TOOL_COUNT = 0x0013DB
MADOU_AP_SAVEINFO = 0x001390
MADOU_AP_SAVEINFO_LENGTH = 0x0A

MADOU_FREEZE = 0x001401
MADOU_MENU = 0x00172B

MADOU_RANDO_INFO = 0x007080


class MadouSNIClient(SNIClient):
    game = "Madou Monogatari Hanamaru Daiyouchienji"
    patch_suffix = ".apmmhd"
    item_queue: typing.List[int] = []
    client_random: random.Random = random.Random()

    async def add_item_to_inventory(self, ctx: "SNIContext", in_stage: bool, has_full_inventory: bool) -> None:
        from SNIClient import snes_buffered_write, snes_read
        if len(self.item_queue) > 0:
            item = self.item_queue.pop()
            if not in_stage or has_full_inventory:
                # can't handle this item right now, send it to the back and return to handle the rest
                self.item_queue.append(item)
                return
            inventory_list = list(struct.unpack("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", await snes_read(ctx, MADOU_INVENTORY, MADOU_INVENTORY_LENGTH)))
            for i in range(len(inventory_list)):
                if inventory_list[i] == 0x00:
                    inventory_list[i] = hex_data_by_item[item][1][0].value
                    snes_buffered_write(ctx, SRAM_START + MADOU_INVENTORY, struct.pack("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH", *inventory_list))
                    # Some items actually are flag oriented, not inventory oriented, so the flag needs to exist anyway.
                    if len(hex_data_by_item[item][1]) > 1:
                        additional_info = hex_data_by_item[item][1][1]
                        current_state = await snes_read(ctx, SRAM_START + MADOU_SAVE + additional_info.hex_address, 0x01)
                        new_state = int.to_bytes(current_state[0] | additional_info.value)
                        snes_buffered_write(ctx, SRAM_START + MADOU_SAVE + additional_info.hex_address, new_state)
                    break
            else:
                self.item_queue.append(item)  # no more slots, get it next go around

    async def validate_rom(self, ctx: "SNIContext") -> bool:
        from SNIClient import snes_read
        rom_name = await snes_read(ctx, MADOU_ROMHASH_START, 0x15)
        if rom_name is None or rom_name == bytes([0] * 0x15) or rom_name[:5] != b"Madou":
            return False

        ctx.game = self.game
        ctx.rom = rom_name
        ctx.items_handling = 0b101  # default local items with remote start inventory
        ctx.allow_collect = True
        return True

    async def game_watcher(self, ctx: "SNIContext") -> None:
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        if not ctx.slot:
            return
        # We need a read to check whether the game is "in-game", and if the game is paused or in a cutscene or a fight.
        pause_state = await snes_read(ctx, MADOU_FREEZE, 0x01)
        menu_state = await snes_read(ctx, MADOU_MENU, 0x01)
        # For now, check for whether the player is in-game if the player's health is 0.
        main_menu_state = await snes_read(ctx, MADOU_HEALTH, 0x01)
        # We need to find a place in the ROM to store the goal of the game, then do a read on it.
        goal_type = await snes_read(ctx, MADOU_RANDO_INFO, 0x01)
        goal_flag = await snes_read(ctx, MADOU_RANDO_INFO + 0x01, 0x01)

        is_paused = pause_state[0] == 0x01
        is_menued = menu_state[0] == 0x01
        is_in_game = main_menu_state[0] != 0x00
        is_not_in_playable_state = is_paused or is_menued or is_in_game

        if is_not_in_playable_state:
            return

        rom = await snes_read(ctx, MADOU_ROMHASH_START, 0x15)
        if rom != ctx.rom:
            ctx.rom = None
            return
        if goal_type[0] == 0x00:
            goal_condition = await snes_read(ctx, SRAM_START + MADOU_SAVE + 0x88, 0x01)
        elif goal_type[0] == 0x01:
            goal_condition = await snes_read(ctx, SRAM_START + MADOU_SAVE + 0xA1, 0x01)
        elif goal_type[0] == 0x02:
            goal_condition = await snes_read(ctx, SRAM_START + MADOU_SAVE + 0x88, 0x01)
        else:
            goal_condition = await snes_read(ctx, SRAM_START + MADOU_SAVE + 0xFF, 0x01)  # Fake memory read.  We need this flag.
        is_goaled = goal_condition[0] & goal_flag[0] == goal_condition[0]
        if is_goaled:
            await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
            ctx.finished_game = True

        new_checks = []

        location_ram_data = await snes_read(ctx, SRAM_START + MADOU_SAVE, MADOU_SAVE_LENGTH)
        bestiary_location_ram_data = await snes_read(ctx, SRAM_START + MADOU_BESTIARY, MADOU_BESTIARY_LENGTH)
        for loc_id, loc_data in hex_by_location.items():
            if loc_id not in ctx.locations_checked:
                if loc_data[0] > 0x1400:  # If it's a bestiary location we just check if the value > 0, as the value is simply the page its on in the bestiary.
                    save_data = bestiary_location_ram_data[loc_data[0] - MADOU_BESTIARY]
                    if save_data > 0:
                        new_checks.append(loc_id)
                    continue
                # Otherwise, we use the flag method.
                save_data = location_ram_data[loc_data[0] - MADOU_SAVE]  # Grab the save data's value
                masked_data = save_data & loc_data[1]  # The save data uses a flag system, so we need to do an and here to check it
                if masked_data != 0:  # If the result is non-zero, it was checked.
                    new_checks.append(loc_id)

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names.lookup_in_game(new_check_id)
            total_locations = len(ctx.missing_locations) + len(ctx.checked_locations)
            snes_logger.info(f"New Check: {location} ({len(ctx.locations_checked)}/{total_locations})")
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": [new_check_id]}])

        recv_count = await snes_read(ctx, SRAM_START + MADOU_AP_SAVEINFO, 2)
        recv_amount = struct.unpack("H", recv_count)[0]
        if recv_amount < len(ctx.items_received):
            item = ctx.items_received[recv_amount]
            recv_amount += 1
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names.lookup_in_game(item.item), 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names.lookup_in_slot(item.location, item.player), recv_amount, len(ctx.items_received)))

            snes_buffered_write(ctx, SRAM_START + MADOU_AP_SAVEINFO, struct.pack("H", recv_amount))
            group = hex_data_by_item[item.item][0]
            if group == "Equipment" or group == "Consumable" or group == "Gem" or group == "Souvenir":
                self.item_queue.append(item.item)
            elif group != "Nothing":
                hex_commands_list = hex_data_by_item[item.item][1]
                for command in hex_commands_list:
                    if group == "Event Item" or group == "Flight Access":
                        value = await snes_read(ctx, SRAM_START + MADOU_SAVE + command.hex_address, 0x01)
                        new_value = struct.unpack("H", value)[0] | command.value
                        snes_buffered_write(ctx, MADOU_SAVE + command.hex_address, struct.pack("H", new_value))
                    elif group == "Cookies":
                        value = await snes_read(ctx, SRAM_START + MADOU_SAVE + command.hex_address, 0x02)
                        int_value = int.from_bytes(value, "little")
                        new_value = int.to_bytes(2, min(0x270F, int_value + 0x01F4), "little")
                        snes_buffered_write(ctx, SRAM_START + MADOU_SAVE + command.hex_address, new_value)
                    elif group == "Tool":
                        if command.hex_address == 0xFF:
                            tool_inventory = list(struct.unpack("HHHHHH", await snes_read(ctx, SRAM_START + MADOU_TOOLS, MADOU_TOOL_COUNT)))
                            for i in range(len(tool_inventory)):
                                if tool_inventory[i] == 0x00:
                                    tool_inventory[i] = command.value
                                    snes_buffered_write(ctx, SRAM_START + MADOU_TOOLS, struct.pack("HHHHHH", *tool_inventory))
                                if tool_inventory[i] == command.value:
                                    break  # Was already given.
                    elif group == "Secret Stone":
                        stone_count = await snes_read(ctx, SRAM_START + MADOU_SAVE + 0xe3, 0x01)
                        new_count = min(struct.pack("H", 0x08), struct.unpack("H", stone_count)[0] + 1)
                        snes_buffered_write(ctx, SRAM_START + MADOU_SAVE + 0xe3, new_count)
                        stone_icons = list(struct.unpack("HHHHHHHH", await snes_read(ctx, SRAM_START + MADOU_SAVE + 0xe4, 0x08)))
                        for i in range(len(stone_icons)):
                            if stone_icons[i] == 0x00:
                                stone_icons[i] = 0x01
                        snes_buffered_write(ctx,  SRAM_START + MADOU_SAVE + 0xe4, *stone_icons)
                    else:
                        value = await snes_read(ctx, SRAM_START + MADOU_SAVE + command.hex_address, 0x01)
                        new_value = struct.unpack("H", value)[0] + command.value
                        snes_buffered_write(ctx, MADOU_SAVE + command.hex_address, struct.pack("H", new_value))
        inventory_count = await snes_read(ctx, MADOU_INVENTORY_COUNT, 0x01)
        is_inventory_full = inventory_count[0] != 0x2A
        await self.add_item_to_inventory(ctx, is_not_in_playable_state, is_inventory_full)
        await snes_flush_writes(ctx)
