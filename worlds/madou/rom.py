import hashlib
import os
import typing
from typing import Collection, SupportsIndex
from .data.static_data import endings

import Utils
from worlds.Files import APProcedurePatch, APTokenMixin, APTokenTypes, APPatchExtension

base_save_offset = 0x12724
HASH = 'fe6af670466c1e64538a4d14ad033440'

if typing.TYPE_CHECKING:
    from . import MadouWorld


class RomData:
    def __init__(self, file: bytes, name: typing.Optional[str] = None):
        self.file = bytearray(file)
        self.name = name

    def read_byte(self, offset: int) -> int:
        return self.file[offset]

    def read_bytes(self, offset: int, length: int) -> bytearray:
        return self.file[offset:offset + length]

    def write_byte(self, offset: int, value: int) -> None:
        self.file[offset] = value

    def write_bytes(self, offset: int, values: typing.Sequence[int]) -> None:
        self.file[offset:offset + len(values)] = values

    def get_bytes(self) -> bytes:
        return bytes(self.file)


class MadouProcedurePatch(APProcedurePatch, APTokenMixin):
    hash = [HASH]
    game = "Madou Monogatari Hanamaru Daiyouchienji"
    patch_file_ending = ".apmmhd"
    procedure = [
        ("apply_tokens", ["token_patch.bin"]),
        ("calc_snes_crc", [])
    ]
    name: bytes  # used to pass to __init__

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


def initial_patch(world: "MadouWorld", patch: MadouProcedurePatch):
    #  Sets the flag for reading all the books in the library.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0xa5, bytes([0xf0, 0xff]))
    #  Skips the kindergarten intro, since its tedious.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x79, bytes([0x0f]))
    #  Skips most of the frog stuff and skips the puzzle.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x7c, bytes([0x05]))
    # Skips when Suketoudora runs away from Ancient Ruins.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x9F, bytes([0x20])),
    # Skips part where Suketoudora moves to his house.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x8a, bytes([0x02])),
    # Puts Scorpion Guy in the boat.  However, this also triggers the cutscene where Zoh slams the door on you.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x37, bytes([0x10])),
    # Patches for the school incident.  Makes the school frozen, and moves the victory read for entering the headmaster room elsewhere.
    patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x7f, bytes([0x08])),
    patch.write_token(APTokenTypes.WRITE, 0x150735, bytes([0xF8, 0x00]))
    # All items that can be allowed.  The method calling system stores the line call at X, and we could back-read this.
    # Checking X+9 with 16 bit enabled returns 4880 if it's a chest, 0000 if its from a store.
    # We can use this to figure out what items are acceptable.  0000 is the only acceptable one.  Any other item
    # is just blocked.  Look around 0x02925e for a jump splice.
    patch.write_token(APTokenTypes.WRITE, 0x007090, bytes(
        [
            0x23, 0x24, 0x25, 0x26, 0x28,  # Food items.
            0x32, 0x33, 0x34, 0x35,  # Shop Staffs.
            0x43, 0x44, 0x45, 0x46,  # Shop Rings.
            0xFF  # Some way to denote the end of the list.
        ]
    )),
    # Patch Carbuncle interaction to refer to another flag.
    patch.write_token(APTokenTypes.WRITE, 0x16fa92, bytes([0xF9, 0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x16fb2f, bytes([0xF9, 0x00]))
    # Patch the explosion event to put its value somewhere needless.  This is actually the book checks which doesn't matter.
    patch.write_token(APTokenTypes.WRITE, 0x179dc5, bytes([0x80, 0x01]))

    # Patch the shop item locations so the flags aren't tied.
    patch.write_token(APTokenTypes.WRITE, 0x1650f3, bytes([0xF4, 0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x165155, bytes([0xF4, 0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x16507c, bytes([0xF3, 0x00]))
    patch.write_token(APTokenTypes.WRITE, 0x165185, bytes([0xF3, 0x00]))

    # Patch chest items which give important items that are flag relevant.

    from Utils import __version__
    patch_name = bytearray(
        f'KDL3{__version__.replace(".", "")[0:3]}_{world.player}_{world.multiworld.seed:11}\0', 'utf8')[:21]
    patch_name.extend([0] * (21 - len(patch_name)))
    patch.name = bytes(patch_name)
    patch.write_token(APTokenTypes.WRITE, 0x3C000, patch.name)

    patch.write_token(APTokenTypes.COPY, 0x7FC0, (21, 0x3C000))

    patch.write_file("token_patch.bin", patch.get_token_binary())


def patch_rom(world: "MadouWorld", patch: MadouProcedurePatch) -> None:
    initial_patch(world, patch)
    # Written slot data.
    ending = world.options.goal.value
    goal_flag = endings[ending][1]
    required_stones = world.options.required_secret_stones.value
    experience_rates = world.options.experience_multiplier // 50

    patch.write_token(APTokenTypes.WRITE, 0x007080, bytes(
        [
            ending, goal_flag, required_stones, experience_rates
        ]
    ))
    starting_spells = world.options.starting_magic.value
    if "Healing" not in starting_spells:
        patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x37, bytes([0x00]))
    if "Fire" not in starting_spells:
        patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x39, bytes([0x00]))
    if "Ice Storm" not in starting_spells:
        patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x3A, bytes([0x00]))
    if "Thunder" not in starting_spells:
        patch.write_token(APTokenTypes.WRITE, base_save_offset + 0x3B, bytes([0x00]))
    if world.options.squirrel_stations:  # Move the station flags to write to a free spot in save memory.
        patch.write_token(APTokenTypes.WRITE, 0x150330, bytes([0xEE, 0x00]))
        patch.write_token(APTokenTypes.WRITE, 0x152815, bytes([0xE8, 0x00]))
        patch.write_token(APTokenTypes.WRITE, 0x1515a7, bytes([0xEF, 0x00]))
        patch.write_token(APTokenTypes.WRITE, 0x150b80, bytes([0xE9, 0x00]))
        patch.write_token(APTokenTypes.WRITE, 0x171446, bytes([0xEA, 0x00]))


def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if HASH != basemd5.hexdigest():
            raise Exception('Supplied Base Rom is not the patched english version.')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_settings().general_options
    if not file_name:
        file_name = options["madou_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name
