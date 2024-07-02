from random import *
class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.origin = [height - 1, width - 1]
        self.start = [0, randint(0, width - 1)]
        self.end  = [height - 1, randint(0, width - 1)]
        self.grid = [[[j, i+1] if i < width - 1 else [j+1, i] for i in range(width)] for j in range(height)]
        self.grid[self.origin[0]][self.origin[1]] = []
        self.validDirections = [[-1, 0], [0, -1]]
        self.generateSolution()

    def originShift(self):
        previousOrigin = self.origin.copy()
        self.validDirections = []
        if previousOrigin[0] < self.height - 1:
            self.validDirections.append([1, 0])
        if previousOrigin[0] > 0:
            self.validDirections.append([-1, 0])
        if previousOrigin[1] < self.width - 1:
            self.validDirections.append([0, 1])
        if previousOrigin[1] > 0:
            self.validDirections.append([0, -1])

        direction = choice(self.validDirections)
        self.origin[0] += direction[0]
        self.origin[1] += direction[1]
        self.grid[previousOrigin[0]][previousOrigin[1]] = [self.origin[0], self.origin[1]]
        self.grid[self.origin[0]][self.origin[1]] = []
        
    def generateSolution(self):
        startsolutionpath = []
        y, x = self.start[0], self.start[1]
        while [y, x] != self.origin:
            startsolutionpath.append([y, x])
            y, x = self.grid[y][x][0], self.grid[y][x][1]
        startsolutionpath.append(self.origin)
        endsolutionpath = []
        y, x = self.end[0], self.end[1]
        while [y, x] != self.origin:
            endsolutionpath.append([y, x])
            y, x = self.grid[y][x][0], self.grid[y][x][1]
            if [y, x] != self.origin and [y, x] in startsolutionpath:
                ind = startsolutionpath.index([y, x])
                endsolutionpath.append([y, x])
                self.solutionpath = startsolutionpath[0:ind]+list(reversed(endsolutionpath))
                return
        self.solutionpath = startsolutionpath+list(reversed(endsolutionpath))

    def __str__(self):
        result = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == []:
                    result+="."
                else:
                    if self.grid[i][j] == [i, j-1]:
                        result+="\u2190"
                    elif self.grid[i][j] == [i-1, j]:
                        result+="\u2191"
                    elif self.grid[i][j] == [i, j+1]:
                        result+="\u2192"
                    elif self.grid[i][j] == [i+1, j]:
                        result+="\u2193"
            result+="\n"
        return result