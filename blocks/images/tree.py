import pygame
from .block import Block
from ..core import BlockCore

class Tree:
    def __init__(self, leaves_color, trunk_color, ground_block, shading=0.2):
        shade = 1 - shading
        self.leaves = BlockCore()
        self.trunk = BlockCore()
        self.ground_block = ground_block

        mid_leaves = leaves_color.darken(shade)
        dark_leaves = mid_leaves.darken(shade)

        image = BlockCore.get_surface(leaves_color.color)
        m_image = BlockCore.get_surface(mid_leaves.color)
        d_image = BlockCore.get_surface(dark_leaves.color)

        for i in (0, 8, 16, 24):
            self.leaves.apply_top(image, 32 - i, 32 - i, i, 24 - i)
            self.leaves.apply_left(m_image, 8, 32 - i, i, 24 - i)
            self.leaves.apply_right(d_image, 8, 32 - i, i, 24 - i)

        image.fill(trunk_color.color)
        self.trunk.apply_top(image, 8, 8, 24, 0)
        trunk_color.darken_ip(shade)
        image.fill(trunk_color.color)
        self.trunk.apply_left(image, 32, 8, 24, 0)
        trunk_color.darken_ip(shade)
        image.fill(trunk_color.color)
        self.trunk.apply_right(image, 32, 8, 24, 0)

    def draw(self, surface, pos):
        self.ground_block.draw(surface, pos)
        surface.blit(self.trunk.surface, pos)
        surface.blit(self.leaves.surface, (pos[0], pos[1] - 32))
