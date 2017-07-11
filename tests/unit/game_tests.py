import unittest
from unittest import mock

from rl.game import Game, GameError, GameLoop
from rl.screen import Screen


class GameTests(unittest.TestCase):
    def test_screen_is_initialised_to_correct_size(self):
        screen = Screen()
        screen.init = mock.MagicMock()

        game = Game(screen)
        game.start()

        screen.init.assert_called_with(80,
                                       50,
                                       "Roguelike",
                                       False)

    def test_cannot_initialise_multiple_times(self):
        screen = Screen()
        screen.is_ready = mock.MagicMock(return_value=True)

        game = Game(screen)

        with self.assertRaises(GameError):
            game.start()

    def test_cannot_draw_to_unitialised_screen(self):
        screen = Screen()
        screen.is_ready = mock.MagicMock(return_value=False)

        game = Game(screen)

        with self.assertRaises(GameError):
            game.draw()

    def test_draws_to_and_flushes_screen(self):
        screen = Screen()
        screen.draw = mock.MagicMock()
        screen.flush = mock.MagicMock()

        game = Game(screen)

        game.start()
        game.draw()

        screen.draw.assert_called()
        screen.flush.assert_called()


class TestGameLoop(unittest.TestCase):
    def test_tick_returns_true_while_screen_is_open(self):
        screen = Screen()
        screen.is_closed = mock.MagicMock(return_value=False)
        game = Game(screen)
        game_loop = GameLoop(game)

        self.assertTrue(game_loop.tick())

    def test_tick_returns_false_when_window_is_closed(self):
        screen = Screen()
        screen.is_closed = mock.MagicMock(return_value=True)
        game = Game(screen)
        game_loop = GameLoop(game)

        self.assertFalse(game_loop.tick())
