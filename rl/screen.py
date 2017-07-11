import tdl

class Screen():
    def __init__(self):
        self.console = None

    def is_ready(self):
        return (self.console != None)

    def is_closed(self):
        return bool(tdl.event.is_window_closed())

    def init(self, width, height, title, fullscreen):
        tdl.set_font('arial10x10.png',
                     greyscale=True,
                     altLayout=True)

        self.width = width
        self.height = height

        self._root_console = tdl.init(width,
                                height,
                                title=title,
                                fullscreen=fullscreen)

        self.console = tdl.Console(width, height)

    def clear(self, x, y):
        self.console.draw_char(x, y, ' ', bg=None)

    def draw(self, x, y, char, color):
        self.console.draw_char(x, y, char, color)
        self._root_console.blit(self.console,
                                0, 0,
                                self.width, self.height,
                                0, 0)

    def flush(self):
        tdl.flush()
