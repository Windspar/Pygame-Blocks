import pygame
from .block import Block


class IceBlock(Block):
    def update_top_image(self, surface, color):
        color1 = color.darken(0.8)
        color1.darken_ip(0.8)
        pygame.draw.polygon(surface, color1.color, [(1, 1), (5, 1), (1, 7)])
        pygame.draw.polygon(surface, color1.color, [(19, 1), (21, 1), (1,23), (1, 18)])
        pygame.draw.polygon(surface, color1.color, [(30, 30), (30, 17), (19,30)])

    def update_left_image(self, surface, color):
        surface.set_at((5, 4), self.base.color)
        surface.set_at((21, 7), self.base.color)
        surface.set_at((12, 11), self.base.color)
        surface.set_at((19, 16), self.base.color)
        surface.set_at((7, 26), self.base.color)

    def update_right_image(self, surface, color):
        surface.set_at((9, 6), self.base.color)
        surface.set_at((15, 9), self.base.color)
        surface.set_at((22, 14), self.base.color)
        surface.set_at((7, 18), self.base.color)
        surface.set_at((24, 28), self.base.color)
        surface.set_at((16, 30), self.base.color)
