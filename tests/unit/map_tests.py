import unittest
from  unittest import mock
from rl.map import Map


class MapTests(unittest.TestCase):
    def test_map_draw_a_tile(self):
        screen = mock.MagicMock()
        map = Map()
        map.draw(screen)

        x = 2
        y = 2
        bg_color = (155, 155, 155)

        screen.draw_a_wall.assert_called_with(x, y, bg_color)
