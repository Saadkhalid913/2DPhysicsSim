import pygame
import numpy as np
from math import *


def getMag(arr):
    #returns magnitude of a vector 
    mag = sqrt(arr[0]**2 + arr[1]**2)
    return mag


class PygameObject():

    def __init__(self, window, color):
        self.window = window
        self.color = color


class Circle(PygameObject):

    def __init__(self, window, color, centre, radius):
        super().__init__(window, color)
        self.radius = radius
        self.centre = np.array([centre[0], centre[1]], dtype=float)
        self.velocity = np.array([0, 0], dtype=float)
        self.acceleration = np.array([0, 0], dtype=float)

        # interaction with enviornment
        self.Bounce = 0.75

    def draw(self):
        pygame.draw.circle(self.window, self.color,
                           list(self.centre.astype(int)), self.radius)

    def move(self):
        self.centre += self.velocity
        self.draw()
        self.velocity = self.velocity + self.acceleration



    def setVelocity(self, v: list):
        self.velocity = np.array(v)

    def setAcceleration(self, a: list):
        self.acceleration = np.array(a)

    def setBouncyness(self, b):
        self.Bounce = b

    @property
    def max_X(self):
        return self.centre[0] + self.radius

    @property
    def max_Y(self):
        return self.centre[1] + self.radius

    @property
    def min_Y(self):
        return self.centre[1] - self.radius

    @property
    def min_X(self):
        return self.centre[0] - self.radius

    @property
    def rect(self):
        return rect(self.min_X, self.min_Y, self.max_X - self.min_X, self.max_Y - self.min_Y, self.window, (255, 255, 255))

    def reflect(self, dir):
        X_flipMatrix = np.array([[-1 * self.Bounce, 0],
                                 [0, 1]])

        Y_flipMatrix = np.array([[1, 0],
                                 [0, -1 * self.Bounce]])
        if dir == 1:
            self.velocity = np.dot(Y_flipMatrix, self.velocity)
        elif dir == 0:
            self.velocity = np.dot(X_flipMatrix, self.velocity)
        else:
            raise ValueError

   

    def iscollision(self, objs):
        for obj in objs:

            if not isinstance(obj, rect):
                upper = (getMag(self.velocity) + getMag(obj.velocity)) + 10
                lower = -upper
                obj = obj.rect
            else:
                upper = getMag(self.velocity) + 10
                lower = -upper

            if self.rect.colliderect(obj):

                # vertical collisions
                if lower <= self.max_Y - (obj.y) <= upper:
                    self.reflect(dir=1)

                elif lower <= self.min_Y - ((obj.y + obj.h)) <= upper:
                    self.reflect(dir=1)

                # sideways collisions
                elif lower <= self.min_X - (obj.x + obj.w) <= upper:
                    self.reflect(dir=0)
                    print("left")
                elif lower <= self.max_X - obj.x <= upper:
                    self.reflect(dir=0)
                    print("right")


class rect(pygame.Rect):

    def __init__(self, X, Y, W, L, window, Color):
        super().__init__(X, Y, W, L)
        self.c = Color
        self.window = window

    def draw(self):
        pygame.draw.rect(self.window, self.c, self)
