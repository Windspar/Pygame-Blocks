import pygame

class Color:
    def __init__(self, r=0, g=0, b=0, a=255):
        if isinstance(r, str):
            self.color = pygame.Color(r)
        else:
            self.color = pygame.Color(r, g, b, a)

    def copy(self):
        return Color(*self.color)

    def _darken(self, value):
        if value < 0.0 or value > 1.0:
            raise ValueError('Value out of range')

        return self.color.hsla

    def darken(self, value):
        h, s, l, a = self._darken(value)
        c = Color()
        c.color.hsla = h, s, l * value, a
        return c

    def darken_ip(self, value):
        h, s, l, a = self._darken(value)
        self.color.hsla = h, s, l * value, a
