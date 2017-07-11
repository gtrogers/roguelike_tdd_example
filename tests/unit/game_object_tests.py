import unittest

from rl.game_object import GameObject


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

        player.move(0, -1)

        self.assertEqual(player.y, 0)
