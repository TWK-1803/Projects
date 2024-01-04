canvasWidth = 600
canvasHeight = 600
gridsize = 10
gridWidth = canvasWidth//gridsize + 1
gridHeight = canvasHeight//gridsize + 1
gridvalues = [[[] for i in range(gridWidth)] for j in range(gridHeight)]
isRunning = True
threshold = 1
fps = 30
tickrate = 1000//fps
north = 0
east = 1
south = 2
west = 3

# Each corner is represented as the bit in the given position. 0b1234 converted to decimal
# Each case where an edge is to be drawn is given as [from, to] with
# the possibility of multiple edges
# 1---N---2
# -       -
# W       E
# -       -
# 4---S---3


arrangements = {
    1: [[south, west]],
    2: [[east, south]],
    4: [[north, east]],
    8: [[north, west]],
    12: [[east, west]],
    10: [[north, east], [south, west]],
    9: [[north, south]],
    6: [[north, south]],
    5: [[north, west],[east, south]],
    3: [[east, west]],
    14: [[south, west]],
    13: [[east, south]],
    11: [[north, east]],
    7: [[north, west]],
}