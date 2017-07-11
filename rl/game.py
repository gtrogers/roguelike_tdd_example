import tdl

import rl.screen


class GameError(Exception):
    def __init__(self, message):
        self.message = message


class Game():
    def __init__(self, screen):
        self.screen = screen

    def start(self):
        if not self.screen.is_ready():
            self.screen.init(80, 50, "Roguelike", False)
        else:
            raise GameError("Cannot initialise multiple times")

    def draw(self):
        if not self.screen.is_ready():
            raise GameError("Cannot draw to unitialised screen")
        else:
            self.screen.draw(1, 1, '@', (255, 255, 255))
            self.screen.flush()


class GameLoop():
    def __init__(self, game):
        self.game = game
        game.start()

    def tick(self):
        if not tdl.event.is_window_closed():
            self.game.draw()
            return True
        else:
            return False

    def loop(self):
        shouldLoop = True

        while shouldLoop:
            shouldLoop = self.tick()

        exit(0)


def new_game(screen):
    game = Game(screen)
    return GameLoop(game)
