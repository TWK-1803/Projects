from Config import *
from math import sqrt
from random import random, randint
import pygame

FORCES = []
DT = 60/1000

def distance(p1, p2): return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def clamp(s, n, l) : return max(s, min(n, l))

class Mass:

    def __init__(self, x, y, mass = 0.1, elasticity = 1, pinned = False):
        self.x = x
        self.x_0 = x
        self.y = y
        self.y_0 = y
        self.mass = mass
        self.elasticity = elasticity
        self.pinned = pinned
        self.burning = False
    
    def update(self):
        if not self.pinned:
            fx = 0
            fy = 0
            for force in FORCES:
                fx += force[0]
                fy += force[1]

            ax = fx/self.mass
            ay = fy/self.mass
            
            tempx = self.x
            tempy = self.y

            self.x = 2 * self.x - self.x_0 + ax * DT**2
            self.y = 2 * self.y - self.y_0 + ay * DT**2

            self.x_0 = tempx
            self.y_0 = tempy

    def constrain(self):
        vx = self.x - self.x_0
        vy = self.y - self.y_0

        if self.x < 0:
            self.x = 0
            self.x_0 = self.x + vx * self.elasticity
        elif self.x > WIDTH:
            self.x = WIDTH
            self.x_0 = self.x + vx * self.elasticity
        if self.y < 0:
            self.y = 0
            self.y_0 = self.y + vy * self.elasticity
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.y_0 = self.y + vy * self.elasticity
        
class Spring:

    def __init__(self, screen, mass1, mass2, length, compressability = 1, maxstrainmult = 99):
        self.mass1 = mass1
        self.mass2 = mass2
        self.x = (self.mass1.x + self.mass2.x)//2
        self.y = (self.mass1.y + self.mass2.y)//2
        self.length = length
        self.compressability = compressability
        self.strained = False
        self.maxstrainmult = maxstrainmult
        self.burning = False
        self.particlesSpawned = 0

    def update(self):
        dx = self.mass2.x - self.mass1.x
        dy = self.mass2.y - self.mass1.y
        dist = sqrt(dx**2 + dy**2)
        diff = self.length - dist

        if diff == 0:
            percent = 0
        else:
            percent = (diff/dist)/2

        self.strained = dist > self.length * self.maxstrainmult
        
        if self.burning:
            if not self.mass1.burning:
                self.mass1.burning = True if random() <= BURNSPREADCHANCE else False
            if not self.mass2.burning:
                self.mass2.burning = True if random() <= BURNSPREADCHANCE else False

        else:
            if self.mass1.burning or self.mass2.burning:
                self.burning = True

        if not self.strained:    
            offsetx = dx*percent*self.compressability
            offsety = dy*percent*self.compressability

            if not self.mass1.pinned:
                self.mass1.x -= offsetx
                self.mass1.y -= offsety
                
            if not self.mass2.pinned:
                self.mass2.x += offsetx
                self.mass2.y += offsety
        
        self.x = (self.mass1.x + self.mass2.x)//2
        self.y = (self.mass1.y + self.mass2.y)//2