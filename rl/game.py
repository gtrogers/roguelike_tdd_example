class Game():
    def __init__(self, screen):
        self.screen = screen

    def start(self):
        self.screen.init(80, 50, "Roguelike", False)

    def draw(self):
        self.screen.draw(1, 1, '@', (255, 255, 255))


def new_game(screen):
    return Game(screen)
