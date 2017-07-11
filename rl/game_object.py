class GameObject():
    def __init__(self, symbol):
        self.x = 1
        self.y = 1
        self.symbol = symbol

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
