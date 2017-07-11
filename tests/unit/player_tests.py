import unittest

from rl.player import Player


class PlayerTests(unittest.TestCase):
    def test_player_starts_at_1_1(self):
        player = Player()

        self.assertEqual(player.x, 1)
        self.assertEqual(player.y, 1)

    def test_moving_player(self):
        player = Player()

        player.move(0, -1)

        self.assertEqual(player.y, 0)
