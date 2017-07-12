class Map():
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        self.screen.draw_a_wall(2, 2, (155, 155, 155))
