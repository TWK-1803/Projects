from PIL import Image
import hashlib
import numpy as np
from time import time

# Hashing a list was weirdly harder/more complex than just hashing an image since that image had binary data
def file_hash(im):
    return hashlib.sha256(im.tobytes()).hexdigest()

#Pull subset of pixels from the larger picture, assuming tilesize, and hash them to allow for easy comparisons between tiles
def getTileHashAtXY(pixels, c, r):
    tile = [[] for i in range(TILESIZE)]
    row = 0
    for i in range(r*TILESIZE, r*TILESIZE+TILESIZE):
        for j in range(c*TILESIZE, c*TILESIZE+TILESIZE):
            try:
                tile[row].append(pixels[j,i])
            except:
                print(i, j)
                #pass
        row += 1
    
    hash = file_hash(Image.fromarray(np.array(tile, dtype=np.uint8)))
    return hash

# Find the valid adjacencies
def getNeighbors(pixels, c, r):
    neighbors = [[],[],[],[]]
    if r > 0:
        neighbors[NORTH].append(getTileHashAtXY(pixels, c, r-1))
    if c < IMAGE_X - 1:
        neighbors[EAST].append(getTileHashAtXY(pixels, c+1, r))
    if r < IMAGE_Y - 1:
        neighbors[SOUTH].append(getTileHashAtXY(pixels, c, r+1))
    if c > 0:
        neighbors[WEST].append(getTileHashAtXY(pixels, c-1, r))

    return neighbors

# Break the input into tiles and generate the rules to govern the WFC
def generateTileData():
    tileSprites = {}
    tileWeights = {}
    tileRules = {}

    for r in range(IMAGE_Y):
        for c in range(IMAGE_X):
            hash = getTileHashAtXY(pixels, c, r)
            if hash not in tileSprites:
                tileSprites[hash] = (c*TILESIZE, r*TILESIZE)
                tileWeights[hash] = 1
                tileRules[hash] = getNeighbors(pixels, c, r)
            else:
                tileWeights[hash] += 1
                neighbors = getNeighbors(pixels, c, r)
                for i in range(len(neighbors)):
                    if neighbors[i] != [] and neighbors[i][0] not in tileRules[hash][i]:
                        tileRules[hash][i].append(neighbors[i][0])


    return tileSprites, tileWeights, tileRules

NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3

SPRITESHEET_PATH = ''           # Put filepath to input here
TILESIZE = 16                   # Measured in pixels
SCALETILE = 2

WORLD_X = 20                    # Measured in tiles
WORLD_Y = 20

INTERACTIVE = True              # True if wacthing the algorithm iterate
INTERACTIVE_KEYPRESS = False    # True if requiring input to advance

STOP_THRESHOLD = 15             # Number of short resets before failing out

DEBUG = False

im = Image.open(SPRITESHEET_PATH)
pixels = im.load()
width, height = im.size

IMAGE_X = width//TILESIZE
IMAGE_Y = height//TILESIZE

start = time()
tileSprites, tileWeights, tileRules = generateTileData()
end = time()
if DEBUG: print("Done with setup in {}s".format(end-start))