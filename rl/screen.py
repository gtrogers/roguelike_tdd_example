import tdl

class Screen():
    def __init__(self):
        self.console = None

    def is_ready(self):
        return (self.console != None)

    def is_closed(self):
        return tdl.event.is_window_closed()

    def init(self, width, height, title, fullscreen):
        tdl.set_font('arial10x10.png',
                     greyscale=True,
                     altLayout=True)

        self.console = tdl.init(width,
                                height,
                                title=title,
                                fullscreen=fullscreen)

    def draw(self, x, y, char, color):
        self.console.draw_char(x, y, char, color)

    def flush(self):
        tdl.flush()
