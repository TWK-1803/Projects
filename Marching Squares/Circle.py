import random
from Config import *

class Circle:

    def __init__(self):
        self.r = random.randint(25, 75)
        self.x = random.randint(self.r+1, canvasWidth-self.r-1)
        self.y = random.randint(self.r+1, canvasWidth-self.r-1)
        self.dx = random.randint(-50, 50)/tickrate
        self.dy = random.randint(-50, 50)/tickrate
    
    def update(self):
        if self.x + self.dx + self.r > canvasWidth or self.x + self.dx - self.r < 0:
            self.dx = -self.dx
        if self.y + self.dy + self.r > canvasHeight or self.y + self.dy - self.r < 0:
            self.dy = -self.dy
        self.x += self.dx
        self.y += self.dy

    def calculateImplicitFunction(self, x, y):
        diff = (x - self.x)**2 + (y - self.y)**2
        if diff == 0:
            return (self.r**2)/0.000001
        else:
            return (self.r**2)/diff
    