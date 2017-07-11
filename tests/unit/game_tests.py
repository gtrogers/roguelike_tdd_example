import unittest
from unittest import mock

import tdl

from rl.game import Game, GameError, GameLoop
from rl.screen import Screen


class GameTests(unittest.TestCase):
    def test_game_is_created_with_a_player(self):
        screen = Screen()
        game = Game(screen)

        self.assertIsNotNone(game.player)

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

    def test_drawing_clears_old_position(self):
        screen = Screen()
        screen.clear = mock.MagicMock()
        game = Game(screen)

        game.start()
        game.player.x = 10
        game.player.y = 10

        game.draw()

        screen.clear.assert_called_with(10, 10)

    def test_draws_player_at_player_x_and_y(self):
        screen = Screen()
        screen.draw = mock.MagicMock()
        game = Game(screen)

        game.player.x = 10
        game.player.y = 10

        game.start()
        game.draw()

        white = (255, 255, 255)
        screen.draw.assert_called_with(10, 10, '@', white)

    def test_moves_player_when_down_is_pressed(self):
        screen = Screen()
        game = Game(screen)
        game.player = mock.MagicMock()

        game.key_pressed("DOWN")

        game.player.move.assert_called_with(0, 1)

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

    def test_game_is_drawn_and_input_handled_on_tick(self):
        screen = Screen()
        game = Game(screen)
        game.draw = mock.MagicMock()
        game_loop = GameLoop(game)
        game_loop.handle_input = mock.MagicMock()

        tdl.event.key_wait = mock.MagicMock(return_value="DOWN")

        game_loop.tick()

        game.draw.assert_called()
        game_loop.handle_input.assert_called()

    def test_input_handling(self):
        screen = Screen()
        game = Game(screen)
        game.key_pressed = mock.MagicMock()
        game_loop = GameLoop(game)

        game_loop.handle_input("DOWN")

        game.key_pressed.assert_called_with("DOWN")

    def test_waiting_for_input(self):
        screen = Screen()
        game = Game(screen)
        gl = GameLoop(game)
        gl.handle_input = mock.MagicMock()
        tdl.event.key_wait = mock.MagicMock(return_value="FOO")

        gl.wait_for_input()

        gl.handle_input.assert_called_with("FOO")

