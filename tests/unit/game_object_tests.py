import unittest
from unittest.mock import MagicMock

from rl.game_object import GameObject
from rl.map import Map
from rl.tile import Tile

mockMap = MagicMock()

class GameObjectTests(unittest.TestCase):
    def test_player_starts_at_1_1(self):
        player = GameObject('@')

        self.assertEqual(player.x, 1)
        self.assertEqual(player.y, 1)

    def test_player_is_represented_with_at_symbol(self):
        player = GameObject('@')

        self.assertEqual(player.symbol, '@')

    def test_moving_player(self):
        player = GameObject('@')
        theMap = MagicMock()
        theMap.getTile = MagicMock(return_value=Tile(False))

        player.move(0, -1, theMap)

        self.assertEqual(player.y, 0)

    def test_game_object_cannot_move_through_walls(self):
        player = GameObject('@')
        theMap = MagicMock()
        theMap.getTile = MagicMock(return_value=Tile(True))

        player.move(0, -1, theMap)

        self.assertEqual(player.x, 1)
        self.assertEqual(player.y, 1)
