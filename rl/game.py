import tdl

from rl import screen, game_object
from rl.map import Map


class GameError(Exception):
    def __init__(self, message):
        self.message = message


class Game():
    def __init__(self, screen, theMap):
        self.screen = screen
        self.map = theMap
        self.player = game_object.GameObject('@')
        self.objects = [
            self.player,
            game_object.GameObject('?')
        ]
        self._vectors = {
            "DOWN": (0, 1),
            "UP": (0, -1),
            "LEFT": (-1, 0),
            "RIGHT": (1, 0)
        }

    def start(self):
        if not self.screen.is_ready():
            self.screen.init(80, 50, "Roguelike", False)
        else:
            raise GameError("Cannot initialise multiple times")

    def draw(self):
        if not self.screen.is_ready():
            raise GameError("Cannot draw to unitialised screen")
        else:
            self.map.draw()
            self._draw_objects_on_screen()
            self.screen.flush()
            self._clear_objects_on_screen()

    def key_pressed(self, key):
        vec = self._vectors.get(key, None)
        if vec:
            self.player.move(*vec)

    def _draw_objects_on_screen(self):
        for o in self.objects:
            self.screen.draw(o.x,
                             o.y,
                             o.symbol,
                             (255, 255, 255))

    def _clear_objects_on_screen(self):
        for o in self.objects:
            self.screen.clear(o.x, o.y)


class GameLoop():
    def __init__(self, game):
        self.game = game
        game.start()

    def tick(self):
        if not self.game.screen.is_closed():
            self.game.draw()
            self.wait_for_input()
            return True
        else:
            return False

    def handle_input(self, key):
        self.game.key_pressed(key)

    def wait_for_input(self):
        key = tdl.event.key_wait()

        self.handle_input(key.key)

    def loop(self):
        shouldLoop = True

        while shouldLoop:
            shouldLoop = self.tick()

        exit(0)


def new_game(screen):
    theMap = Map(screen)
    game = Game(screen, theMap)
    return GameLoop(game)
