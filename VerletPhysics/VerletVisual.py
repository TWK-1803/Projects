from utils import *
from Config import *
import pygame

#pygame configurations
pygame.init()
pygame.display.set_caption("Verlet Physics")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

POINTS = [[Mass(c*GRIDSCALE, r*GRIDSCALE, mass=0.05, elasticity=0.3, pinned = r==1) for c in range(1, GRIDWIDTH)] for r in range(1, GRIDHEIGHT)]

SPRINGS = []
for r in range(1, GRIDHEIGHT - 1):
    for c in range(GRIDWIDTH - 1):
        SPRINGS.append(Spring(POINTS[r][c], POINTS[r-1][c], distance(POINTS[r][c], POINTS[r-1][c]), maxstrainmult=99))

for c in range(1, GRIDWIDTH - 1):
    for r in range(GRIDHEIGHT - 1):
        SPRINGS.append(Spring(POINTS[r][c], POINTS[r][c-1], distance(POINTS[r][c], POINTS[r][c-1]), maxstrainmult=99))

selected = None
run = True
gravityEnabled = False
while run:
    clock.tick(FPS)
    mousex, mousey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_g:
                if gravityEnabled:
                    FORCES.remove((0,1))
                    gravityEnabled = not gravityEnabled
                else:
                    FORCES.append((0,1))
                    gravityEnabled = not gravityEnabled

        if event.type == pygame.MOUSEBUTTONUP:
            selected = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for row in POINTS:
                    for point in row:
                        if -GRABRADIUS <= point.x - mousex <= GRABRADIUS and -GRABRADIUS <= point.y - mousey <= GRABRADIUS:
                            selected = point
                            break
            elif event.button == 3:
                for spring in SPRINGS:
                    if -GRABRADIUS <= point.x - mousex <= GRABRADIUS and -GRABRADIUS <= point.y - mousey <= GRABRADIUS:
                        row.remove(point)
                        break

    screen.fill(BLACK)
    for row in POINTS:
        for point in row:
            if DRAWPOINTS:
                pygame.draw.circle(screen, WHITE, (point.x, point.y), 2)
            point.update()
    
    for spring in SPRINGS:
        if DRAWLINES:
            pygame.draw.line(screen, WHITE, (spring.mass1.x, spring.mass1.y), (spring.mass2.x, spring.mass2.y), 1)
        spring.update()
        if spring.strained:
            SPRINGS.remove(spring)
    
    for row in POINTS:
        for point in row:
            point.constrain()

    if selected is not None:
        selected.x = clamp(0, mousex, WIDTH)
        selected.y = clamp(0, mousey, HEIGHT)

    pygame.display.flip()

pygame.quit()