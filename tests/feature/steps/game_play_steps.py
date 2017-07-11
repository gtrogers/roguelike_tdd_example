from unittest.mock import MagicMock

from behave import given, when, then, step

from rl import game, screen


def _mockDrawMethod(screen):
    screen.draw = MagicMock()


@given('a new game')
def step_impl(context):
    context.screen = screen.Screen()
    _mockDrawMethod(context.screen)
    context.game = game.new_game(context.screen)


@when('the game starts')
def step_impl(context):
    context.game.start()


@then('a window is created')
def step_impl(context):
    assert context.screen.console is not None


@then('the player gets drawn')
def step_impl(context):
    context.game.draw()
    context.screen.draw.assert_called_with(1,1,'@', (255, 255, 255))
