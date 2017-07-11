import tdl

from rl import screen, player

class GameError(Exception):
    def __init__(self, message):
        self.message = message


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.player = player.Player()

    def start(self):
        if not self.screen.is_ready():
            self.screen.init(80, 50, "Roguelike", False)
        else:
            raise GameError("Cannot initialise multiple times")

    def draw(self):
        if not self.screen.is_ready():
            raise GameError("Cannot draw to unitialised screen")
        else:
            self.screen.draw(self.player.x,
                             self.player.y,
                             '@',
                             (255, 255, 255))
            self.screen.flush()
            self.screen.clear(self.player.x, self.player.y)

    def key_pressed(self, key):
        self.player.move(0, 1)


class GameLoop():
    def __init__(self, game):
        self.game = game
        game.start()

    def tick(self):
        if not self.game.screen.is_closed():
            self.wait_for_input()
            self.game.draw()
            return True
        else:
            return False

    def handle_input(self, key):
        self.game.key_pressed(key)

    def wait_for_input(self):
        key = tdl.event.key_wait()

        self.handle_input(key)

    def loop(self):
        shouldLoop = True

        while shouldLoop:
            shouldLoop = self.tick()

        exit(0)


def new_game(screen):
    game = Game(screen)
    return GameLoop(game)
