class DrawBlock:
    def __init__(self, block, data):
        self.block = block
        self.data = data

    def draw(self, surface, pos):
        self.block.draw(surface, pos, self.data)
