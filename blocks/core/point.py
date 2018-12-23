import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def alter(self, point, op):
        if isinstance(point, Point):
            return Point(op(self.x, point.x), op(self.y, point.y))
        elif isinstance(point, (tuple, list)):
            return Point(op(self.x, point[0]), op(self.x, point[1]))
        elif isinstance(point, (int, float)):
            return Point(op(self.x, point), op(self.y, point))

    def astype(self, astype):
        return Point(astype(self.x), astype(self.y))

    def copy(self):
        return Point(self.x, self.y)

    def __add__(self, point):
        return self.alter(point, operator.add)

    def __sub__(self, point):
        return self.alter(point, operator.sub)

    def __mul__(self, point):
        return self.alter(point, operator.mul)

    def __truediv__(self, point):
        return self.alter(point, operator.truediv)

    def __floordiv__(self, point):
        return self.alter(point, operator.floordiv)

    def __mod__(self, point):
        return self.alter(point, operator.mod)

    def __pow__(self, point):
        return self.alter(point, operator.pow)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return str(vars(self))
