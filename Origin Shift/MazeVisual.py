import pygame
from MazeObj import Maze

canvasWidth, canvasHeight = 1000, 800
sidepadding = 50
gridWidth, gridHeight = 100, 80
size = (canvasWidth, canvasHeight)
black = (20, 20, 20)
white = (247, 247, 247)
green = (20, 247, 20)
red = (247, 20, 20)

displayPaths = False
displayWalls = True
displaySolution = False

#pygame configurations
pygame.init()
pygame.display.set_caption("Origin Shift Maze Generation")
screen = pygame.display.set_mode(size)

gridxScale = (canvasWidth - sidepadding*2) / gridWidth
gridyScale = (canvasHeight - sidepadding*2) / gridHeight
numIters = gridWidth*gridHeight*35
maze = Maze(gridWidth, gridHeight)

for i in range(numIters):
    maze.originShift() 

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_r:
                maze = Maze(gridWidth, gridHeight)
                for i in range(numIters):
                    maze.originShift()
                maze.generateSolution()
            if event.key == pygame.K_o:
                maze.originShift()
                maze.generateSolution()
            if event.key == pygame.K_p:
                displayPaths = not displayPaths
            if event.key == pygame.K_w:
                displayWalls = not displayWalls
            if event.key == pygame.K_s:
                displaySolution = not displaySolution

    screen.fill(black)
    if displayPaths: 
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[i])):
                if len(maze.grid[i][j]) == 0:
                    pygame.draw.circle(screen, white, (j*gridxScale+sidepadding+gridxScale//2, i*gridyScale+sidepadding+gridyScale//2), 3)
                elif maze.grid[i][j][0] == i-1:
                    pygame.draw.line(screen, green, (j*gridxScale+sidepadding+gridxScale//2, i*gridyScale+sidepadding+gridyScale//2), ((j)*gridxScale+sidepadding+gridxScale//2, (i-1)*gridyScale+sidepadding+gridyScale//2))
                elif maze.grid[i][j][0] == i+1:
                    pygame.draw.line(screen, green, (j*gridxScale+sidepadding+gridxScale//2, i*gridyScale+sidepadding+gridyScale//2), ((j)*gridxScale+sidepadding+gridxScale//2, (i+1)*gridyScale+sidepadding+gridyScale//2))
                elif maze.grid[i][j][1] == j-1:
                    pygame.draw.line(screen, green, (j*gridxScale+sidepadding+gridxScale//2, i*gridyScale+sidepadding+gridyScale//2), ((j-1)*gridxScale+sidepadding+gridxScale//2, (i)*gridyScale+sidepadding+gridyScale//2))
                elif maze.grid[i][j][1] == j+1:
                    pygame.draw.line(screen, green, (j*gridxScale+sidepadding+gridxScale//2, i*gridyScale+sidepadding+gridyScale//2), ((j+1)*gridxScale+sidepadding+gridxScale//2, (i)*gridyScale+sidepadding+gridyScale//2))
    
    if displayWalls:
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[i])):
                if maze.grid[i][j] != [i-1, j] and (i == 0 or maze.grid[i-1][j] != [i, j]): # Not pointing up and either on top edge or box above isnt pointing down
                    pygame.draw.line(screen, white, (j*gridxScale+sidepadding, i*gridyScale+sidepadding), ((j+1)*gridxScale+sidepadding, i*gridyScale+sidepadding))
                if maze.grid[i][j] != [i+1, j] and (i == gridHeight - 1 or maze.grid[i+1][j] != [i, j]): # Not pointing down and either on bottom edge or box below isnt pointing up
                    pygame.draw.line(screen, white, (j*gridxScale+sidepadding, (i+1)*gridyScale+sidepadding), ((j+1)*gridxScale+sidepadding, (i+1)*gridyScale+sidepadding))
                if maze.grid[i][j] != [i, j-1] and (j == 0 or maze.grid[i][j-1] != [i, j]): # Not pointing left and either on left edge or box left isnt pointing rght
                    pygame.draw.line(screen, white, (j*gridxScale+sidepadding, i*gridyScale+sidepadding), (j*gridxScale+sidepadding, (i+1)*gridyScale+sidepadding))
                if maze.grid[i][j] != [i, j+1] and (j == gridWidth - 1 or maze.grid[i][j+1] != [i, j]): # Not pointing right and either on right edge or box right isnt pointing left
                    pygame.draw.line(screen, white, ((j+1)*gridxScale+sidepadding, i*gridyScale+sidepadding), ((j+1)*gridxScale+sidepadding, (i+1)*gridyScale+sidepadding))

        pygame.draw.line(screen, black, (maze.start[1]*gridxScale+sidepadding, sidepadding), ((maze.start[1]+1)*gridxScale+sidepadding, sidepadding))
        pygame.draw.line(screen, black, (maze.end[1]*gridxScale+sidepadding, canvasHeight-sidepadding), ((maze.end[1]+1)*gridxScale+sidepadding, canvasHeight-sidepadding))
    
    if displaySolution:
        for i in range(len(maze.solutionpath) - 1):
            y1, x1 = maze.solutionpath[i][0], maze.solutionpath[i][1]
            y2, x2 = maze.solutionpath[i+1][0], maze.solutionpath[i+1][1]
            pygame.draw.line(screen, red, (x1*gridxScale+sidepadding+gridxScale//2, y1*gridyScale+sidepadding+gridyScale//2), (x2*gridxScale+sidepadding+gridxScale//2, y2*gridyScale+sidepadding+gridyScale//2))

    pygame.display.flip()

pygame.quit()