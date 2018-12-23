import pygame


class BlockCore:
    def __init__(self, depth=0):
        self.surface = pygame.Surface((64, 64)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        self.depth = depth

    def apply_left(self, image, width=32, height=32, xoffset=0, yoffset=0):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(width - self.depth):
            xs = xoffset
            ys = x + 17 + self.depth + yoffset
            for y in range(height):
                spix[xs, int(ys)] = ipix[x, y]
                ys += 0.5
                xs += 1

    def apply_right(self, image, width=32, height=32, xoffset=0, yoffset=0):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(width - self.depth):
            xs = 32 #- xoffset
            ys = x + 32 + yoffset - int(xoffset * 0.5)
            for y in range(height):
                spix[xs, int(ys)] = ipix[x, y]
                ys -= 0.5
                xs += 1

        """
        xs = 32 + xoffset
        ys = 16 + yoffset
        for y in range(0, height, 2):
            spix[xs, int(ys)] = ipix[31, y]
            ys += 1
            xs += 2
        """

    def apply_top(self, image, width=32, height=32, xoffset=0, yoffset=0):
        ipix = pygame.surfarray.pixels2d(image)
        spix = pygame.surfarray.pixels2d(self.surface)

        for x in range(width):
            xs = x + xoffset
            ys = 0.5 * x + 16 + self.depth + yoffset
            for y in range(height):
                spix[xs, int(ys)] = ipix[x, y]
                ys -= 0.5
                xs += 1

    @staticmethod
    def get_surface(color=(0,0,0,0)):
        surface = pygame.Surface((32, 32)).convert_alpha()
        surface.fill(color)
        return surface
