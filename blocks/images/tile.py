from .block import Block
from ..core import pattern, Point


class Tile(Block):
    def __init__(self, color, color2=None, size=8, flat=False, shading=0.2):
        self.size = size
        if color2 is None:
            self.color2 = color.darken(0.6)
        else:
            self.color2 = color2

        Block.__init__(self, color, flat, 0, shading)

    def update_top_image(self, surface, color):
        pattern.tile(surface, self.color2, Point(self.size, self.size))

    def update_left_image(self, surface, color):
        self.color2.darken_ip(1 - self.shading)
        pattern.tile(surface, self.color2, Point(self.size, self.size))

    def update_right_image(self, surface, color):
        self.color2.darken_ip(1 - self.shading)
        surface.fill(self.color2.color)
        pattern.tile(surface, color, Point(self.size, self.size))
