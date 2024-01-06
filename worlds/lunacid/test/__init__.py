from typing import ClassVar
import unittest
from test.bases import WorldTestBase


class LunacidTestCase(unittest.TestCase):
    game = "Lunacid"
    player: ClassVar[int] = 1


class LunacidTestBase(WorldTestBase, LunacidTestCase):
    seed = None

    def world_setup(self, *args, **kwargs):
        super().world_setup(*args, **kwargs)
