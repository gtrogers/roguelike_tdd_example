import unittest
from unittest import mock

import tdl

from tests.util import StubKeyEvent

from rl.game import Game, GameError, GameLoop
from rl.screen import Screen

mockMap = mock.MagicMock()

class GameTests(unittest.TestCase):
    def test_game_is_created_with_a_player_and_a_npc(self):
        screen = Screen()
        game = Game(screen, mockMap)

        self.assertEqual(len(game.objects), 2)

    def test_screen_is_initialised_to_correct_size(self):
        screen = Screen()
        screen.init = mock.MagicMock()

        game = Game(screen, mockMap)
        game.start()

        screen.init.assert_called_with(80,
                                       50,
                                       "Roguelike",
                                       False)

    def test_cannot_initialise_multiple_times(self):
        screen = Screen()
        screen.is_ready = mock.MagicMock(return_value=True)

        game = Game(screen, mockMap)

        with self.assertRaises(GameError):
            game.start()

    def test_cannot_draw_to_unitialised_screen(self):
        screen = Screen()
        screen.is_ready = mock.MagicMock(return_value=False)

        game = Game(screen, mockMap)

        with self.assertRaises(GameError):
            game.draw()

    def test_draws_to_and_flushes_screen(self):
        screen = Screen()
        theMap = mock.MagicMock()
        screen.draw = mock.MagicMock()
        screen.flush = mock.MagicMock()

        game = Game(screen, theMap)

        game.start()
        game.draw()

        theMap.draw.assert_called()
        screen.draw.assert_called()
        screen.flush.assert_called()

    def test_drawing_clears_old_position(self):
        screen = Screen()
        screen.clear = mock.MagicMock()
        game = Game(screen, mockMap)

        game.start()
        game.player.x = 10
        game.player.y = 10

        game.draw()

        calls = [mock.call(10, 10), mock.call(1, 1)]
        screen.clear.assert_has_calls(calls)

    def test_draws_player_at_player_x_and_y(self):
        screen = Screen()
        screen.draw = mock.MagicMock()
        game = Game(screen, mockMap)

        game.player.x = 10
        game.player.y = 10

        game.start()
        game.draw()

        white = (255, 255, 255)
        calls = [mock.call(10, 10, '@', white), mock.call(1, 1, '?', white)]
        screen.draw.assert_has_calls(calls)

    def test_moves_player_based_on_arrow_keys(self):
        screen = Screen()
        game = Game(screen, mockMap)
        game.player = mock.MagicMock()

        game.key_pressed("DOWN")
        game.player.move.assert_called_with(0, 1, mockMap)

        game.key_pressed("UP")
        game.player.move.assert_called_with(0, -1, mockMap)

        game.key_pressed("LEFT")
        game.player.move.assert_called_with(-1, 0, mockMap)

        game.key_pressed("RIGHT")
        game.player.move.assert_called_with(1, 0, mockMap)


class TestGameLoop(unittest.TestCase):
    def test_tick_returns_true_while_screen_is_open(self):
        screen = Screen()
        screen.is_closed = mock.MagicMock(return_value=False)
        game = Game(screen, mockMap)
        game_loop = GameLoop(game)

        self.assertTrue(game_loop.tick())

    def test_tick_returns_false_when_window_is_closed(self):
        screen = Screen()
        screen.is_closed = mock.MagicMock(return_value=True)
        game = Game(screen, mockMap)
        game_loop = GameLoop(game)

        self.assertFalse(game_loop.tick())

    def test_game_is_drawn_and_input_handled_on_tick(self):
        screen = Screen()
        game = Game(screen, mockMap)
        game.draw = mock.MagicMock()
        game_loop = GameLoop(game)
        game_loop.handle_input = mock.MagicMock()

        tdl.event.key_wait = mock.MagicMock(return_value=StubKeyEvent("DOWN"))

        game_loop.tick()

        game.draw.assert_called()
        game_loop.handle_input.assert_called()

    def test_input_handling(self):
        screen = Screen()
        game = Game(screen, mockMap)
        game.key_pressed = mock.MagicMock()
        game_loop = GameLoop(game)

        game_loop.handle_input("DOWN")

        game.key_pressed.assert_called_with("DOWN")

    def test_waiting_for_input(self):
        screen = Screen()
        game = Game(screen, mockMap)
        gl = GameLoop(game)
        gl.handle_input = mock.MagicMock()
        tdl.event.key_wait = mock.MagicMock(return_value=StubKeyEvent("FOO"))

        gl.wait_for_input()

        gl.handle_input.assert_called_with("FOO")
