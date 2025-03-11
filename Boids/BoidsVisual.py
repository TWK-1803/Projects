from Vector2 import Vector2
from constants import *
from Boid import Boid
from random import randint
import pygame

pygame.init()
pygame.display.set_caption("Boid Simulation")
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

flocks = []
if SETUP_SCENE == 0:
    flocks.append([WHITE, [Boid(Vector2(randint(SCREEN_OFFSET_X, WIDTH - SCREEN_OFFSET_X), randint(SCREEN_OFFSET_Y, HEIGHT - SCREEN_OFFSET_Y))) for i in range(NUM_BOIDS)]])
if SETUP_SCENE == 1:
    flocks.append([RED, [Boid(Vector2(randint(SCREEN_OFFSET_X, WIDTH - SCREEN_OFFSET_X), randint(SCREEN_OFFSET_Y, HEIGHT - SCREEN_OFFSET_Y))) for i in range(int(NUM_BOIDS // 3))]])
    flocks.append([BLUE, [Boid(Vector2(randint(SCREEN_OFFSET_X, WIDTH - SCREEN_OFFSET_X), randint(SCREEN_OFFSET_Y, HEIGHT - SCREEN_OFFSET_Y))) for i in range(int(NUM_BOIDS // 3))]])
    flocks.append([GREEN, [Boid(Vector2(randint(SCREEN_OFFSET_X, WIDTH - SCREEN_OFFSET_X), randint(SCREEN_OFFSET_Y, HEIGHT - SCREEN_OFFSET_Y))) for i in range(int(NUM_BOIDS // 3))]])

run = True
mouseAvoid = False
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    left, middle, right = pygame.mouse.get_pressed()
    if left:
        mouseAvoid = True

    mousex, mousey = pygame.mouse.get_pos()
    mousePos = Vector2(mousex, mousey)
    # print(mouseAvoid)
    screen.fill(BLACK)
    for flock in flocks:
        for boid in flock[1]:
            boid.guide(flock[1], mousePos, mouseAvoid)
            boid.update()
            boid.display(screen, flock[0])
    mouseAvoid = False

    pygame.display.flip()

pygame.quit()