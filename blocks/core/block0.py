import pygame


class BlockCore:
    def __init__(self, depth=0):
        self.surface = pygame.Surface((64, 64)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        self.depth = depth

    def apply_left(self, image):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(32 - self.depth):
            xs = 0
            ys = x + 17 + self.depth
            for y in range(32):
                spix[xs, int(ys)] = ipix[x, y]
                ys += 0.5
                xs += 1

    def apply_right(self, image):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(32 - self.depth):
            xs = 63
            ys = 48 - x
            for y in range(32):
                spix[xs, int(ys)] = ipix[x, y]
                ys += 0.5
                xs -= 1

        #"""
        xs = 63
        ys = 16
        for y in range(0, 32, 2):
            spix[xs, int(ys)] = ipix[31, y]
            ys += 1
            xs -= 2
        #"""

    def apply_top(self, image):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(32):
            xs = x
            ys = 0.5 * x + 16 + self.depth
            for y in range(32):
                spix[xs, int(ys)] = ipix[x, y]
                ys -= 0.5
                xs += 1

    @staticmethod
    def get_surface(color=(0,0,0,0)):
        surface = pygame.Surface((32, 32)).convert_alpha()
        surface.fill(color)
        return surface
