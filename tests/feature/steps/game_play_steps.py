from unittest.mock import MagicMock

from behave import given, when, then, step
from expects import *

import tdl

from tests.util import StubKeyEvent

from rl import game, screen, tile


def get_screen_with_mock_drawing():
    scrn = screen.Screen()
    scrn.draw = MagicMock()
    scrn.draw_a_wall = MagicMock()
    return scrn


@given('a new game')
def step_impl(context):
    context.screen = get_screen_with_mock_drawing()
    gl = game.new_game(context.screen)
    context.game_loop = gl


@given('a game with walls')
def step_impl(context):
    context.screen = get_screen_with_mock_drawing()
    gl = game.new_game(context.screen)
    for x in range(45):
        gl.game.map.tiles[x][0] = tile.Tile(True)
        gl.game.map.tiles[x][44] = tile.Tile(True)
    context.game_loop = gl


@when('the player walks into a wall')
def step_impl(context):
    tdl.event.key_wait = MagicMock(return_value=StubKeyEvent("UP"))
    context.game_loop.tick()


@then('they should not move')
def step_impl(context):
    expect(context.game_loop.game.player.x).to(equal(1))
    expect(context.game_loop.game.player.y).to(equal(1))


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


@then('the map gets drawn')
def step_impl(context):
    tiles_drawn = context.screen.draw_a_wall.call_count
    assert tiles_drawn == (80 * 45)
