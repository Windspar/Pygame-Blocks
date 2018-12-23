from .images import *


class Stage:
    def __init__(self, size):
        self.images = []
        self.map = {}
        for i in range(size):
            self.map[i] = {}

    def map_add(self, row, col, args):
        if self.map[row].get(col, False):
            self.map[row][col].extend(args)
            doubles = set(self.map[row][col])
            if len(self.map[row][col]) != len(doubles):
                self.map[row][col] = list(doubles)
        else:
            self.map[row][col] = list(args)

        self.map[row][col].sort()

    def map_range_row(self, range_, row, *args):
        for i in range_:
            self.map_add(row, i, args)

    def map_range_col(self, range_, col, *args):
        for i in range_:
            self.map_add(i, col, args)

    def map_area(self, row_range, col_range, *args):
        c_range = list(col_range)
        for row in row_range:
            for col in c_range:
                self.map_add(row, col, args)

    def map_stack_range(self, range_, row, col, number):
        self.map_add(row, col, [(i, number) for i in range_])

    def setup_draw(self, surface):
        w, h = surface.get_rect().size
        self.avg = (w // 32 + 1 + h // 16 + 1) // 2 + 3

    def draw(self, surface, pos):
        rows = pos[0] - self.avg // 2
        cols = pos[1] - self.avg // 2

        for row in range(rows, rows + self.avg):
            line = self.map.get(row, False)
            for col in range(cols, cols + self.avg):
                c = col - self.avg // 2
                posx = row * 32 - c * 32
                posy = c * 16 + row * 16
                if line:
                    item = line.get(col, False)
                    if item:
                        for n, i in item:
                            pos = posx, posy - n * 32
                            self.images[i].draw(surface, pos)
