from random import randint

WIDTH, HEIGHT = 640, 480

INTERACTIVE = True
ATTRACTORMODE = "FOURWINGS"
AXISMODE = "XY"
DRAWMODE = "LINES"

if ATTRACTORMODE == "THOMAS":
    INITIALPOINTS = [[1.1, 1.1, -0.01]]
    DT = 0.001
    XMIN, XMAX = -10, 10
    YMIN, YMAX = -10, 10
    ZMIN, ZMAX = -10, 10
    
elif ATTRACTORMODE == "LORENZ":
    INITIALPOINTS = [[1.1, 2.0, 7.0]]
    DT = 0.0004
    XMIN, XMAX = -50, 50
    YMIN, YMAX = -50, 50
    ZMIN, ZMAX = -50, 50

elif ATTRACTORMODE == "AIZAWA":
    INITIALPOINTS = [[0.1, 1, 0.01]]
    DT = 0.001
    XMIN, XMAX = -3, 3
    YMIN, YMAX = -3, 3
    ZMIN, ZMAX = -3, 3

elif ATTRACTORMODE == "DADRAS":
    INITIALPOINTS = [[1.1, 2.1, -2.0]]
    DT = 0.001
    XMIN, XMAX = -20, 20
    YMIN, YMAX = -20, 20
    ZMIN, ZMAX = -20, 20

elif ATTRACTORMODE == "CHEN":
    INITIALPOINTS = [[5.0, 10.0, 10.0], [-7.0, -5.0, -10.0]]
    DT = 0.0004
    XMIN, XMAX = -20, 20
    YMIN, YMAX = -20, 20
    ZMIN, ZMAX = -20, 20

elif ATTRACTORMODE == "ROSSLER":
    INITIALPOINTS = [[10.0, 0.0, 10.0]]
    DT = 0.002
    XMIN, XMAX = -25, 25
    YMIN, YMAX = -25, 25
    ZMIN, ZMAX = -25, 25

elif ATTRACTORMODE == "HALVORSON":
    INITIALPOINTS = [[-1.48, -1.51, 2.04]]
    DT = 0.009
    XMIN, XMAX = -20, 20
    YMIN, YMAX = -20, 20
    ZMIN, ZMAX = -20, 20

elif ATTRACTORMODE == "RAB_FAB":
    INITIALPOINTS = [[-1.0, 0.0, 0.5],[1.1, 0.0, 0.5]]
    DT = 0.001
    XMIN, XMAX = -5, 5
    YMIN, YMAX = -5, 5
    ZMIN, ZMAX = -5, 5

elif ATTRACTORMODE == "TSUCS":
    INITIALPOINTS = [[-0.29, -0.25, -0.59]]
    DT = 0.0001
    XMIN, XMAX = -300, 300
    YMIN, YMAX = -300, 300
    ZMIN, ZMAX = -300, 300

elif ATTRACTORMODE == "FOURWINGS":
    INITIALPOINTS = [[1.3, -0.18, 0.01]]
    DT = 0.03
    XMIN, XMAX = -5, 5
    YMIN, YMAX = -5, 5
    ZMIN, ZMAX = -5, 5

COLORS = []
for point in INITIALPOINTS:
    COLORS.append([randint(10, 255), randint(10, 255), randint(10, 255)])