import pygame
from .point import Point
#from .block import BlockCore

def tile(surface, color, size):
    rect = pygame.Rect(0, 0, size.x, size.y)

    for y in range(0, 32, size.y):
        for x in range(0, 32, size.x * 2):
            offset = (y % (size.y * 2)) * (1 / 8) * size.x
            pygame.draw.rect(surface, color.color, rect.move(x + offset, y))

def brick_top(surface, color1, color2=None, color3=None, flip=False):
    if color2 is None:
        color2 = color1.darken(0.8)

    if color3 is None:
        color3 = color2.darken(0.8)

    if flip:
        w = 6
        h = 14
    else:
        w = 14
        h = 6

    rect = pygame.Rect(1, 1, w, h)
    for y in range(0, 32, 8):
        offset = y % 16
        layer = int(y * 0.125) % 2
        for x in range(-offset, 32, 16):
            xlayer = int((x + offset) * 0.0625) % 2
            color = [(color1, color2), (color2, color3)][layer][xlayer]
            if flip:
                pygame.draw.rect(surface, color.color, rect.move(y, x))
            else:
                pygame.draw.rect(surface, color.color, rect.move(x, y))
