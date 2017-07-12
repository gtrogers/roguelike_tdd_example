from rl.tile import Tile

class Map():
    def __init__(self):
        self.tiles = [[Tile(False) for y in range(45)] for x in range(80)]

        self.tiles[10][10] = Tile(True)
        self.tiles[10][9] = Tile(True)
        self.tiles[10][8] = Tile(True)
        self.tiles[10][7] = Tile(True)

    def getTile(self, x, y):
        return self.tiles[x][y]

    def draw(self, screen):
        for y in range(45):
            for x in range(80):
                if self.tiles[x][y].blocked_sight:
                    screen.draw_a_wall(x, y, (100, 100, 100))
                else:
                    screen.draw_a_wall(x, y, (155, 155, 155))
