from Vector2 import Vector2
from utils import *
import pygame

WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)
BLACK = (20, 20, 20)
WHITE = (247, 247, 247)
GREEN = (20, 247, 20)
FPS = 60
NUMITERATIONS = 50
EPSILONTHRESHOLD = 0.01

points = []
connectors = []
for i in range(1, 25):
    points.append(Vector2(i*25, 300))
for i in range(len(points) - 1):
    connectors.append(Connector(points[i], points[i+1], distance(points[i], points[i+1])))

segment = Segment(points, connectors)

pygame.init()
pygame.display.set_caption("Inverse Kinemetics")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()
    target = Vector2(mousex, mousey)
    origin = segment.points[0]
    mouseDist = target - origin
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(BLACK)

    if mouseDist.length() >= segment.totalLength:
        newRelativeTarget = mouseDist.normalize() * segment.totalLength
        target = segment.points[0] + newRelativeTarget
    
    for iter in range(NUMITERATIONS):
        # Backward adjustment
        for i in range(len(segment.points) - 1, -1, -1):
            if i == len(segment.points) - 1:
                segment.points[i] = target
                previousPoint = segment.points[i]
            else:
                dist = previousPoint - segment.points[i]
                newRelativePos = dist.normalize() * segment.connectors[i].length
                segment.points[i] = previousPoint - newRelativePos
                previousPoint = segment.points[i]
        
        # Forward adjustment
        for i in range(0, len(segment.points)):
            if i == 0:
                segment.points[i] = origin
                previousPoint = segment.points[i]
            else:
                dist = segment.points[i] - previousPoint 
                newRelativePos = dist.normalize() * segment.connectors[i-1].length
                segment.points[i] = previousPoint + newRelativePos
                previousPoint = segment.points[i]

        epsilon = (target - segment.points[-1]).length()
        # Average error
        if epsilon <= EPSILONTHRESHOLD:
            break

    previousDrawnPoint = segment.points[0]
    
    for i in range(len(segment.points)):
        pygame.draw.circle(screen, WHITE, (segment.points[i].x, segment.points[i].y), 5)
        if i > 0:
            pygame.draw.line(screen, WHITE, (segment.points[i].x, segment.points[i].y), (previousDrawnPoint.x, previousDrawnPoint.y))
            previousDrawnPoint = segment.points[i]

    pygame.draw.circle(screen, GREEN, (target.x, target.y), 3)
    pygame.display.flip()

pygame.quit()