class Player():
    def __init__(self):
        self.x = 1
        self.y = 1

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
