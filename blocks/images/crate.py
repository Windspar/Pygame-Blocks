import pygame
from .block import Block

class Crate(Block):
    def update_top_image(self, surface, color):
        shade = color.darken(self.shade)
        line = shade.darken(self.shade)
        pygame.draw.rect(surface, shade.color, (0, 0, 32, 32), 1)
        pygame.draw.rect(surface, shade.color, (4, 4, 23, 23))
        # lines
        for y in range(9, 26, 5):
            pygame.draw.line(surface, line.color, (4, y), (26, y))

        # board
        p = ((4, 22), (4,26), (8, 26), (26, 8), (26, 4), (22, 4))
        pygame.draw.polygon(surface, color.color, p)

        # board lines
        pygame.draw.line(surface, shade.color, (4, 22), (4, 26))
        pygame.draw.line(surface, shade.color, (4, 26), (8, 26))
        pygame.draw.line(surface, shade.color, (26, 4), (26, 8))
        pygame.draw.line(surface, shade.color, (22, 4), (26, 4))

    def update_left_image(self, surface, color):
        self.update_top_image(surface, color)

    def update_right_image(self, surface, color):
        self.update_top_image(surface, color)
