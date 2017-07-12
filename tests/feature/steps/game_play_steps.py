from unittest.mock import MagicMock

from behave import given, when, then, step

import tdl

from tests.util import StubKeyEvent

from rl import game, screen


@given('a new game')
def step_impl(context):
    context.screen = screen.Screen()
    context.screen.draw = MagicMock()
    gl = game.new_game(context.screen)
    context.game_loop = gl


@when('the game starts')
def step_impl(context):
    tdl.event.key_wait = MagicMock(return_value=StubKeyEvent("NOTHING"))
    context.game_loop.tick()


@then('the player and npc are drawn')
def step_impl(context):
    context.screen.draw.assert_any_call(1, 1, '@', (255, 255, 255))
    context.screen.draw.assert_any_call(1, 1, '?', (255, 255, 255))


@when('the down key is pressed')
def step_impl(context):
    tdl.event.key_wait = MagicMock(return_value=StubKeyEvent("DOWN"))
    context.game_loop.tick()


@then('the player moves down')
def step_impl(context):
    tdl.event.key_wait = MagicMock(return_value=StubKeyEvent("NOTHING"))
    context.game_loop.tick()
    context.screen.draw.assert_any_call(1, 2, '@', (255, 255, 255))


@then('the NPC gets drawn')
def step_impl(context):
    context.screen.draw.assert_any_call(1, 1, '?', (255, 255, 255))
