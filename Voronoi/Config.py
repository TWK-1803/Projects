from utils import *
from random import randint

WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)
BLACK = (20, 20, 20)
WHITE = (247, 247, 247)
GREEN = (20, 247, 20)
RED = (247, 20, 20)
BLUE = (20, 20, 247)
FPS = 60
NUMPOINTS = 100
AUTOMOVINGPOINTS = True
DELAUNEYVISIBLE = False
VORONOIVISIBLE = True
CIRCUMCIRCLEVISIBLE= False
POINTS = [Vertex(randint(100,WIDTH-100), randint(100, HEIGHT-100)) for i in range(NUMPOINTS)]
VELOCITIES = [[randint(-1, 1), randint(-1, 1)] for i in range(NUMPOINTS)]