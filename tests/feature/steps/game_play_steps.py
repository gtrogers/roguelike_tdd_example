from unittest.mock import MagicMock

from behave import given, when, then, step

from rl import game, screen


def _mock_draw_method(screen):
    screen.draw = MagicMock()


@given('a new game')
def step_impl(context):
    context.screen = screen.Screen()
    _mock_draw_method(context.screen)
    context.game_loop = game.new_game(context.screen)


@when('the game updates')
def step_impl(context):
    context.game_loop.tick()


@then('the player gets drawn')
def step_impl(context):
    context.screen.draw.assert_called_with(1,1,'@', (255, 255, 255))
