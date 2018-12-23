import pygame
from .block import Block
from ..core import pattern


class Brick(Block):
    def __init__(self, mortar, color, flat=False, shading=0.15):
        self.color = color
        self.flip = True
        Block.__init__(self, mortar, flat, 0, shading)

    def update_flip(self, surface, color, color1):
        color2 = color1.darken(0.8)
        pygame.draw.rect(surface, color.color, (0, 0, 8, 32))
        rect = pygame.Rect(1, 1, 6, 6)
        for x in range(0, 32, 8):
            color = (color1, color2)[int(x * (1 / 8)) % 2]
            pygame.draw.rect(surface, color.color, rect.move(0, x))

    def update_top_image(self, surface, color):
        pattern.brick_top(surface, self.color, flip=self.flip)

    def update_left_image(self, surface, color):
        self.color.darken_ip(1 - self.shading)
        pattern.brick_top(surface, self.color, flip=self.flip)
        if self.flip:
            self.update_flip(surface, color, self.color)

    def update_right_image(self, surface, color):
        self.color.darken_ip(1 - self.shading)
        pattern.brick_top(surface, self.color, flip=self.flip)
