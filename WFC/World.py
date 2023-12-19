import random
from Tile import Tile
from Stack import Stack
from Config import *
from time import time

class World:

    def __init__(self, sizeX, sizeY):
        self.cols = sizeX
        self.rows = sizeY

        self.numresets = 0
        self.resetcounter = 0

        self.tileRows = []
        for y in range(self.rows):
            tiles = []
            for x in range(self.cols):
                tile = Tile(x, y)
                tiles.append(tile)
            self.tileRows.append(tiles)

        for y in range(self.rows):
            for x in range(self.cols):
                tile = self.tileRows[y][x]
                if y > 0:
                    tile.addNeighbour(NORTH, self.tileRows[y - 1][x])
                if x < self.cols - 1:
                    tile.addNeighbour(EAST, self.tileRows[y][x + 1])
                if y < self.rows - 1:
                    tile.addNeighbour(SOUTH, self.tileRows[y + 1][x])
                if x > 0:
                    tile.addNeighbour(WEST, self.tileRows[y][x - 1])

    def getEntropy(self, x, y):
        return self.tileRows[y][x].entropy


    def getType(self, x, y):
        return self.tileRows[y][x].possibilities[0]


    def getLowestEntropy(self):
        lowestEntropy = len(list(tileRules.keys()))
        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy
                if tileEntropy > 0:
                    if tileEntropy < lowestEntropy:
                        lowestEntropy = tileEntropy
        return lowestEntropy


    def getTilesLowestEntropy(self):
        lowestEntropy = len(list(tileRules.keys()))
        tileList = []

        for y in range(self.rows):
            for x in range(self.cols):
                tileEntropy = self.tileRows[y][x].entropy
                if tileEntropy > 0:
                    if tileEntropy < lowestEntropy:
                        tileList.clear()
                        lowestEntropy = tileEntropy
                    if tileEntropy == lowestEntropy:
                        tileList.append(self.tileRows[y][x])
        return tileList


    def waveFunctionCollapse(self):
        tilesLowestEntropy = self.getTilesLowestEntropy()

        if tilesLowestEntropy == []:
            return 0

        tileToCollapse = random.choice(tilesLowestEntropy)
        tileToCollapse.collapse()

        stack = Stack()
        stack.push(tileToCollapse)

        while(stack.is_empty() == False):
            tile = stack.pop()
            tilePossibilities = tile.getPossibilities()
            directions = tile.getDirections()

            for direction in directions:
                neighbour = tile.getNeighbour(direction)
                if neighbour.entropy != 0:
                    reduced = neighbour.constrain(tilePossibilities, direction)
                    if reduced == True and neighbour not in stack.items:
                        stack.push(neighbour)    # When possibilities were reduced need to propagate further

        self.resetcounter += 1
        return 1
    
    def reset(self):
        start = time()        
        for r in range(len(self.tileRows)):
            for c in range(len(self.tileRows[0])):
                self.tileRows[r][c].reset()

        self.numresets += 1 if self.resetcounter <= 2 else 0
        self.resetcounter = 0
        end = time()
        if DEBUG: print("Done with backtracking in {}s".format(end-start))