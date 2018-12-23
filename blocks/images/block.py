from ..core import BlockCore

class Block:
    def __init__(self, color, flat=False, depth=0, shading=0.2):
        if flat:
            self.block = BlockCore(32 - depth)
        else:
            self.block = BlockCore(depth)

        self.flat = flat
        self.shading = shading
        self.shade = 1 - shading
        self.base = color.copy()
        self.create_image(color)

    def create_image(self, color):
        self.create_top(color)

        if not self.flat:
            self.create_left(color)
            self.create_right(color)

    def create_top(self, color):
        surface = BlockCore.get_surface()
        surface.fill(color.color)
        self.update_top_image(surface, color)
        self.block.apply_top(surface)

    def create_left(self, color):
        color.darken_ip(self.shade)
        surface = BlockCore.get_surface()
        surface.fill(color.color)
        self.update_left_image(surface, color)
        self.block.apply_left(surface)

    def create_right(self, color):
        color.darken_ip(self.shade)
        surface = BlockCore.get_surface()
        surface.fill(color.color)
        self.update_right_image(surface, color)
        self.block.apply_right(surface)

    def draw(self, surface, pos):
        surface.blit(self.block.surface, pos)

    def update_top_image(self, surface, color):
        pass

    def update_left_image(self, surface, color):
        pass

    def update_right_image(self, surface, color):
        pass
