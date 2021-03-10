import pygame
import time
from PygameClasses import Circle, rect
g = float(0.4)

# colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

win = pygame.display.set_mode((300, 900))

# initialize ball


win = pygame.display.set_mode((800, 600))


def makeBorders(win, w, h):
    top = rect(0, 0, w, 15, win, WHITE)
    bottom = rect(0, h-15, w, 15, win, WHITE)
    left = rect(0, 0, 15, h, win, WHITE)
    right = rect(w-15, 0, 15, h, win, WHITE)
    return [top, bottom, left, right]


B1 = Circle(win, WHITE, (400, 400), 25)
B1.setVelocity([3, -8])
B1.setAcceleration([0, g])
B2 = Circle(win, WHITE, (200, 400), 25)
B2.setVelocity([5, -5])
B2.setAcceleration([0, g])

borders = makeBorders(win, 800, 600)
while True:
    win.fill((0, 0, 0))
    for item in borders:
        item.draw()

    B1.draw()
    B1.move()
    B1.iscollision(borders + [B2])

    B2.draw()
    B2.move()
    B2.iscollision(borders + [B1])
    time.sleep(0.01)
    pygame.display.update()
