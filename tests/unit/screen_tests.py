import unittest
from unittest import mock

import tdl

from rl.screen import Screen

# TODO - maybe stub tdl eventually, feels bad to mock over methods we don't control

class ScreenTests(unittest.TestCase):
    def test_flushes_tdl(self):
        tdl.flush = mock.MagicMock()
        screen = Screen()
        screen.init(80, 80, "foo", False)

        screen.flush()

        tdl.flush.assert_called()

    def test_initialises_with_a_console_object(self):
        screen = Screen()

        self.assertIsNone(screen.console)
        self.assertFalse(screen.is_ready())

        screen.init(80, 80, "foo bar", False)

        self.assertIsNotNone(screen.console)
        self.assertTrue(screen.is_ready())

    def test_calls_through_to_tdl_for_drawing(self):
        screen = Screen()

        screen.console = mock.MagicMock()

        white = (255, 255, 255)
        screen.draw(1, 2, 'g', white)

        screen.console.draw_char.assert_called_with(1, 2, 'g', white)

    def test_returns_value_from_tdl_window_event(self):
        screen = Screen()

        self.assertFalse(screen.is_closed())

    def test_clears_screen_via_tdl(self):
        #TODO - test for drawing + clearing out of bounds
        screen = Screen()
        screen.init(80, 80, 'g', False)

        screen.console = mock.MagicMock()

        screen.clear(10, 10)

        screen.console.draw_char.assert_called_with(10, 10, ' ', bg=None)
