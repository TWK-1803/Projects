import pygame
from World import World
from DrawWorld import DrawWorld
from Config import *
from time import time

# Inspired by https://github.com/CodingQuest2023/Algorithms/tree/main/WorldGeneration/WaveFunctionCollapse
# Uses the rendering framework from the repo but with customizations to allow for programmatic generation
# of the rules of the algorithm from an input example image

pygame.init()
clock = pygame.time.Clock()

displaySurface = pygame.display.set_mode((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))
pygame.display.set_caption("Wave Function Collapse")


world = World(WORLD_X, WORLD_Y)
drawWorld = DrawWorld(world)

done = False

if INTERACTIVE == False:
    while done == False:
        result = world.waveFunctionCollapse()
        if result == 0:
            done = True


drawWorld.update()
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            if event.key == pygame.K_SPACE:
                if INTERACTIVE == True and INTERACTIVE_KEYPRESS == True:
                    start = time()
                    world.waveFunctionCollapse()
                    end = time()
                    if DEBUG: print("Done with Wave Function in {}s".format(end-start))
                    drawWorld.update()

    if INTERACTIVE == True and INTERACTIVE_KEYPRESS == False:
        if not done:
            start = time()
            result = world.waveFunctionCollapse()
            end = time()
            if DEBUG: print("Done with Wave Function in {}s".format(end-start))
            if result == 0:
                done = True
        drawWorld.update()

    if world.numresets > STOP_THRESHOLD:
        print("\n\nTileset reset too often with little progress. Unlikely to resolve\n")
        isRunning = False

    drawWorld.draw(displaySurface)

    pygame.display.flip()
    clock.tick(60)

    

pygame.quit()