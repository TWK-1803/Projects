from math import sqrt

MAX_STEPS = 100
MAX_COLLISIONS = 4000
WIDTH = 1200
HEIGHT = 800
BLACK = (20, 20, 20)
WHITE = (247, 247, 247)
ANGLE_INTERVAL = 0.008
SCREEN_OFFSET = 200
RED = (255, 41, 120)
GREEN = (180, 244, 187)
COLLISION_THESHOLD = 1

def clamp(x, min, max):
    if x < min: x = min
    if x > max: x = max
    return x

def dot(p1, p2):
    return p1[0]*p2[0] + p1[1]*p2[1]

def length(vector):
    return sqrt(vector[0]**2 + vector[1]**2)