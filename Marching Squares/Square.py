import random
from Config import *

class Square:

    def __init__(self):
        self.sidelength = random.randint(25, 75)
        self.x = random.randint(self.sidelength//2+1, canvasWidth-self.sidelength//2-1)
        self.y = random.randint(self.sidelength//2+1, canvasHeight-self.sidelength//2-1)
        self.dx = random.randint(-50, 50)/tickrate
        self.dy = random.randint(-50, 50)/tickrate

    def update(self):
        if self.x + self.dx + self.sidelength/2 > canvasWidth or self.x + self.dx - self.sidelength/2 < 0:
            self.dx = -self.dx
        if self.y + self.dy + self.sidelength/2 > canvasHeight or self.y + self.dy - self.sidelength/2 < 0:
            self.dy = -self.dy
        self.x += self.dx
        self.y += self.dy

    def calculateImplicitFunction(self, x, y):
        diff = abs((x-self.x)+(y-self.y))+abs((x-self.x)-(y-self.y))
        if diff == 0:
            return self.sidelength/0.000001
        else:
            return self.sidelength/diff