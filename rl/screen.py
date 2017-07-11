import tdl

class Screen():
    def __init__(self):
        self.console = None

    def init(self, width, height, title, fullscreen):
        tdl.set_font('arial10x10.png',
                     greyscale=True,
                     altLayout=True)

        self.console = tdl.init(width,
                                height,
                                title=title,
                                fullscreen=fullscreen)

    def draw(self):
        pass
