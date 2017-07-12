import unittest
from  unittest import mock
from expects import *

from rl.tile import Tile
from rl.map import Map


class MapTests(unittest.TestCase):
    def test_map_draws_all_tiles(self):
        screen = mock.MagicMock()
        theMap = Map()
        theMap.draw(screen)

        for y in range(45):
            for x in range(80):
                screen.draw_a_wall.assert_any_call(x, y, mock.ANY)

    def test_blocked_tiles_are_dark_grey(self):
        screen = mock.MagicMock()
        theMap = Map()

        theMap.tiles[10][10] = Tile(True)

        theMap.draw(screen)

        screen.draw_a_wall.assert_any_call(10, 10, (100, 100, 100))

    def test_unblocked_tiles_are_light_grey(self):
        screen = mock.MagicMock()
        theMap = Map()

        theMap.tiles[10][10] = Tile(False)

        theMap.draw(screen)

        screen.draw_a_wall.assert_any_call(10, 10, (155, 155, 155))

    def test_getting_a_tile(self):
        theMap = Map()

        tile = theMap.getTile(1, 1)

        expect(tile).to(be_a(Tile))
