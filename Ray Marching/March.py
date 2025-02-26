import pygame
from Shapes import *
from Ray import Ray
from random import randint
from Utils import *

size = (WIDTH, HEIGHT)

#pygame configurations
pygame.init()
pygame.display.set_caption("2D Raymarching")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

collisions = []

object_count = 15
angle = 0
objects = []

for i in range(0, object_count, 5):
    c = Circle(randint(SCREEN_OFFSET, WIDTH - SCREEN_OFFSET), randint(SCREEN_OFFSET, HEIGHT - SCREEN_OFFSET), randint(20, 100))
    s = Square(randint(SCREEN_OFFSET, WIDTH - SCREEN_OFFSET), randint(SCREEN_OFFSET, HEIGHT - SCREEN_OFFSET), randint(20, 100))
    e = Triangle(randint(SCREEN_OFFSET, WIDTH - SCREEN_OFFSET), randint(SCREEN_OFFSET, HEIGHT - SCREEN_OFFSET), randint(20, 100))
    p = Pentagon(randint(SCREEN_OFFSET, WIDTH - SCREEN_OFFSET), randint(SCREEN_OFFSET, HEIGHT - SCREEN_OFFSET), randint(20, 100))
    x = Hexagram(randint(SCREEN_OFFSET, WIDTH - SCREEN_OFFSET), randint(SCREEN_OFFSET, HEIGHT - SCREEN_OFFSET), randint(20, 100))
    objects.append(c)
    objects.append(s)
    objects.append(e)
    objects.append(p)
    objects.append(x)

run = True
ray = Ray(0, 0, 0, screen)
update = False
while run:
    clock.tick(fps)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        angle += ANGLE_INTERVAL
        update = True
    if keys[pygame.K_LEFT]:
        angle -= ANGLE_INTERVAL
        update = True

    x_mouse, y_mouse = pygame.mouse.get_pos()
    if x_mouse != ray.position[0] or y_mouse != ray.position[1] or ray.angle != angle:
        ray.position = [x_mouse, y_mouse]
        ray.angle = angle
        update = True

    if update:
        screen.fill(BLACK)
        for p in collisions:
            pygame.draw.circle(screen, WHITE, p, 2)

        if len(collisions) > MAX_COLLISIONS:
            collisions.pop()
        ray.march(objects, collisions)
        update = False

pygame.quit()
