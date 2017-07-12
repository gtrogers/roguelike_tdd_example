class GameObject():
    def __init__(self, symbol):
        self.x = 1
        self.y = 1
        self.symbol = symbol

    def move(self, dx, dy, theMap):
        new_x = self.x + dx
        new_y = self.y + dy
        tile = theMap.getTile(new_x, new_y)

        if not tile.blocked:
            self.x = new_x
            self.y = new_y
