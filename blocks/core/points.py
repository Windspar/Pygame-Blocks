from .point import Point


class Points:
    @classmethod
    def topnside(cls):
        top = cls()
        top.top()
        return (top, *top.get_side())

    def __init__(self, topleft=Point(0,0),
                       topright=Point(0,0),
                       bottomleft=Point(0,0),
                       bottomright=Point(0,0)):

        self.topleft = topleft
        self.topright = topright
        self.bottomright = bottomright
        self.bottomleft = bottomleft

    def __repr__(self):
        return str(vars(self))

    def get_side(self, height=32):
        h = Point(0, height)
        return (Points(self.topleft,
                       self.bottomleft,
                       self.topleft + h,
                       self.bottomleft + h),

                Points(self.bottomleft,
                       self.bottomright,
                       self.bottomleft + h,
                       self.bottomright + h))

    def move_across(self, x):
        if -2 > x < 2:
            return

        if x % 2 != 0:
            x -= 1

        across = Point(x, -x * 0.5)
        return Points(self.topleft + across,
                      self.topright + across,
                      self.bottomleft + across,
                      self.bottomright + across)

    def move_down(self, y):
        if -1 > y < 1:
            return

        down = Point(y * 2, y)
        return Points(self.topleft + down,
                      self.topright + down,
                      self.bottomleft + down,
                      self.bottomright + down)

    def move(self, x, y):
        xmove = self.move_across(x)
        return xmove.move_down(y)

    def shift(self, shift_points):
        return Points(self.topleft + shift_points,
                      self.topright + shift_points,
                      self.bottomleft + shift_points,
                      self.bottomright + shift_points)

    def shift_ip(self, shift_points):
        self.topleft += shift_points
        self.topright += shift_points
        self.bottomright += shift_points
        self.bottomleft += shift_points

    def top(self, left=0, top=0, right=64, bottom=32, depth=0):
        if right < 0:
            right = 64 + right

        if bottom < 0:
            bottom = 32 + bottom

        centerx = (left + right) * 0.5
        centery = (top + bottom) * 0.5
        center = (right - bottom * 2) * 0.25

        self.topleft = Point(left, centery)
        self.bottomleft = Point(centerx - center * 2, bottom)
        self.topright = Point(centerx, top - center)
        self.bottomright = Point(right - center * 2, centery - center)

    def top_scaled(self, x=0, y=0):
        w = 64 - x * 2
        h = 32 - y * 2

        self.topleft     = Point(x,            y + h * 0.5)
        self.topright    = Point(x + w * 0.5,  y + x * 0.5)
        self.bottomleft  = Point(x + w * 0.5,  y + h - x * 0.5)
        self.bottomright = Point(x + w,        y + h * 0.5)

    def as_tuple(self):
        return (tuple(self.topleft), tuple(self.topright),
                tuple(self.bottomright), tuple(self.bottomleft))
