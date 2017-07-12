import unittest
from rl.tile import Tile


class TileTests(unittest.TestCase):
    def test_blocking_tiles_blocked_sight_by_default(self):
        blocking = True
        tile = Tile(blocking)

        self.assertTrue(tile.blocked_sight)

        unblocked = False
        tile = Tile(unblocked)
        self.assertFalse(tile.blocked_sight)

    def test_can_override_default_blocked_sight(self):
        blocked = True
        blocked_sight = False
        tile = Tile(blocked, blocked_sight)

        self.assertFalse(tile.blocked_sight)

        blocked_b = False
        blocked_sight_b = True
        tile_b = Tile(blocked_b, blocked_sight_b)

        self.assertTrue(tile_b.blocked_sight)
