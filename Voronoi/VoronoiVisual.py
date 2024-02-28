from itertools import combinations
from utils import *
from Config import *
import pygame

#pygame configurations
pygame.init()
pygame.display.set_caption("Voronoi Diagram")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

t = triangulate(POINTS)

run = True
selected = None
while run:
    clock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.MOUSEBUTTONUP:
            selected = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            for point in POINTS:
                if -3 <= point.x - mousex <= 3 and -3 <= point.y - mousey <= 3:
                    selected = point
                    break
        

    screen.fill(BLACK)
    for point in POINTS:
        pygame.draw.circle(screen, RED, (point.x, point.y), 3)

    if DELAUNEYVISIBLE:
        for triangle in t:
            if not triangle.sharesVertexWithSuper:
                pygame.draw.line(screen, GREEN, (triangle.v0.x, triangle.v0.y), (triangle.v1.x, triangle.v1.y))
                pygame.draw.line(screen, GREEN, (triangle.v0.x, triangle.v0.y), (triangle.v2.x, triangle.v2.y))
                pygame.draw.line(screen, GREEN, (triangle.v1.x, triangle.v1.y), (triangle.v2.x, triangle.v2.y))

    if VORONOIVISIBLE:
        for pair in combinations(t, r=2):
            if sharesEdge(pair[0], pair[1]):
                pygame.draw.line(screen, WHITE, (pair[0].circumCirc.x, pair[0].circumCirc.y), (pair[1].circumCirc.x, pair[1].circumCirc.y))
    
    if CIRCUMCIRCLEVISIBLE:
        for triangle in t:
            if not triangle.sharesVertexWithSuper:
                pygame.draw.circle(screen, BLUE, (triangle.circumCirc.x, triangle.circumCirc.y), triangle.circumCirc.r, width=1)
            
    pygame.display.flip()

    if AUTOMOVINGPOINTS:
        for i in range(NUMPOINTS):
            POINTS[i].x += VELOCITIES[i][0]
            POINTS[i].y += VELOCITIES[i][1]
            if POINTS[i].x < 0:
                POINTS[i].x = 0
                VELOCITIES[i][0] = -VELOCITIES[i][0]
            elif POINTS[i].x > WIDTH:
                POINTS[i].x = WIDTH
                VELOCITIES[i][0] = -VELOCITIES[i][0]
            if POINTS[i].y < 0:
                POINTS[i].y = 0
                VELOCITIES[i][1] = -VELOCITIES[i][1]
            elif POINTS[i].y > HEIGHT:
                POINTS[i].y = HEIGHT
                VELOCITIES[i][1] = -VELOCITIES[i][1]
        t = triangulate(POINTS)  

    else:
        if selected is not None:
            selected.x = clamp(0, mousex, WIDTH)
            selected.y = clamp(0, mousey, HEIGHT)
            t = triangulate(POINTS)      
                                                              
pygame.quit()