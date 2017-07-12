class Tile:
    def __init__(self, blocked, blocked_sight=None):
        self.blocked = blocked
        if blocked_sight is None:
            self.blocked_sight = blocked
        else:
            self.blocked_sight = blocked_sight
