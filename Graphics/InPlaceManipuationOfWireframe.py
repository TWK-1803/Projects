####################################################################################
# Tyler Kranz 102-63-704
# 1/14/2022
# Assignment 2, CSC 470
# This program uses wireframe graphics to display a number of geometric shapes.
# These shapes can be manipulated in the xyz space with translations, in-place
# roations, and in-place scaling.
####################################################################################

import math
import copy
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# global variable which points to the currently selected object
selected = 0

# ***************************** Initialize Objects ***************************
# Definition of the pyramid's underlying points
apex = [0, 50, 100]
base1 = [50, -50, 50]
base2 = [50, -50, 150]
base3 = [-50, -50, 150]
base4 = [-50, -50, 50]

# Definition of cube1's underlying points
topfrontleft1 = [-150, 100, 50]
topfrontright1 = [-100, 100, 50]
topbackleft1 = [-150, 100, 100]
topbackright1 = [-100, 100, 100]
bottomfrontleft1 = [-150, 50, 50]
bottomfrontright1 = [-100, 50, 50]
bottombackleft1 = [-150, 50, 100]
bottombackright1 = [-100, 50, 100]

# Definition of cube2's underlying points
topfrontleft2 = [100, 100, 50]
topfrontright2 = [150, 100, 50]
topbackleft2 = [100, 100, 100]
topbackright2 = [150, 100, 100]
bottomfrontleft2 = [100, 50, 50]
bottomfrontright2 = [150, 50, 50]
bottombackleft2 = [100, 50, 100]
bottombackright2 = [150, 50, 100]


# Definition of all polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside

# Pyramid polygons
frontpoly = [apex, base1, base4]
rightpoly = [apex, base2, base1]
backpoly = [apex, base3, base2]
leftpoly = [apex, base4, base3]
bottompoly = [base1, base2, base3, base4]

# Cube 1 polygons
topface1 = [topfrontleft1, topbackleft1, topbackright1, topfrontright1]
leftface1 = [topfrontleft1, bottomfrontleft1, bottombackleft1, topbackleft1]
backface1 = [topbackright1, topbackleft1, bottombackleft1, bottombackright1]
rightface1 = [topfrontright1, topbackright1, bottombackright1, bottomfrontright1]
frontface1 = [topfrontleft1, topfrontright1, bottomfrontright1, bottomfrontleft1]
bottomface1 = [bottomfrontleft1, bottomfrontright1, bottombackright1, bottombackleft1]

# Cube 2 polygons
topface2 = [topfrontleft2, topbackleft2, topbackright2, topfrontright2]
leftface2 = [topfrontleft2, bottomfrontleft2, bottombackleft2, topbackleft2]
backface2 = [topbackright2, topbackleft2, bottombackleft2, bottombackright2]
rightface2 = [topfrontright2, topbackright2, bottombackright2, bottomfrontright2]
frontface2 = [topfrontleft2, topfrontright2, bottomfrontright2, bottomfrontleft2]
bottomface2 = [bottomfrontleft2, bottomfrontright2, bottombackright2, bottombackleft2]


# Definition of all objects
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]
Cube1 = [topface1, leftface1, backface1, rightface1, frontface1, bottomface1]
Cube2 = [topface2, leftface2, backface2, rightface2, frontface2, bottomface2]

# Definition of all object's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
DefaultPyramidPointCloud = copy.deepcopy(PyramidPointCloud)

Cube1PointCloud = [
    topfrontleft1,
    topfrontright1,
    topbackleft1,
    topbackright1,
    bottomfrontleft1,
    bottomfrontright1,
    bottombackleft1,
    bottombackright1,
]
DefaultCube1PointCloud = copy.deepcopy(Cube1PointCloud)

Cube2PointCloud = [
    topfrontleft2,
    topfrontright2,
    topbackleft2,
    topbackright2,
    bottomfrontleft2,
    bottomfrontright2,
    bottombackleft2,
    bottombackright2,
]
DefaultCube2PointCloud = copy.deepcopy(Cube2PointCloud)


# List of all objects in the scene
Scene = [Pyramid, Cube1, Cube2]

# List of all object data in the scene
ObjectData = [
    Pyramid,
    PyramidPointCloud,
    DefaultPyramidPointCloud,
    Cube1,
    Cube1PointCloud,
    DefaultCube1PointCloud,
    Cube2,
    Cube2PointCloud,
    DefaultCube2PointCloud,
]

# ************************************************************************************


# Calculates the "visual center" point in xyz space and returns it as an array
def getReference(current):
    xmax = current[0][0]
    xmin = current[0][0]
    ymax = current[0][1]
    ymin = current[0][1]
    zmax = current[0][2]
    zmin = current[0][2]
    for point in current:
        if point[0] >= xmax:
            xmax = point[0]
        if point[0] <= xmin:
            xmin = point[0]
        if point[1] >= ymax:
            ymax = point[1]
        if point[1] <= ymin:
            ymin = point[1]
        if point[2] >= zmax:
            zmax = point[2]
        if point[2] <= zmin:
            zmin = point[2]
        # print(str(xmax)+" "+str(xmin)+" "+str(ymax)+" "+str(ymin)+" "+str(zmax)+" "+str(zmin))
    return [((xmin + xmax) / 2), ((ymin + ymax) / 2), ((zmin + zmax) / 2)]


# This function resets the selected object to its original size and location in 3D space
def resetObject(current, default):
    for i in range(len(current)):
        for j in range(3):
            current[i][j] = default[i][j]


# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(current, displacement):
    # iterate through each point and update the XYZ values by adding the corresponding
    # value in the displacement vector
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] += displacement[j]
    # print("translate stub executed.")


# This function performs a simple uniform in-place scale of an object. The scalefactor is a scalar.
def scale(current, scalefactor):
    # Adjust each point according to the visual center, then iterate through each point
    # and multipy each by the scalefactor and readjust back using the reference point again
    refPoint = getReference(current)
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] -= refPoint[j]
        for j in range(0, 3):
            current[i][j] *= scalefactor
        for j in range(0, 3):
            current[i][j] += refPoint[j]
    # print("scale stub executed.")


# This function performs a free rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from -Z [the location of the viewer in the standard postion]
def rotateZ(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees * (math.pi / 180)
        rotatedcoords.append(point[0] * math.cos(dtor) - point[1] * math.sin(dtor))
        rotatedcoords.append(point[0] * math.sin(dtor) + point[1] * math.cos(dtor))
        rotatedcoords.append(point[2])
        point = copy.deepcopy(rotatedcoords)
        for i in range(0, 3):
            current[count][i] = point[i]
        count += 1
        # print(PyramidPointCloud[i])
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] += refPoint[j]
    # print("rotateZ stub executed.")


# This function performs a free rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from +Y looking toward the origin.
def rotateY(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees * (math.pi / 180)
        rotatedcoords.append(point[0] * math.cos(dtor) + point[2] * math.sin(dtor))
        rotatedcoords.append(point[1])
        rotatedcoords.append(point[2] * math.cos(dtor) - point[0] * math.sin(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range(0, 3):
            current[count][i] = point[i]
        count += 1
        # print(PyramidPointCloud[i])
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] += refPoint[j]
    # print("rotateY stub executed.")


# This function performs a free rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from +X looking toward the origin.
def rotateX(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees * (math.pi / 180)
        rotatedcoords.append(point[0])
        rotatedcoords.append(point[1] * math.cos(dtor) - point[2] * math.sin(dtor))
        rotatedcoords.append(point[1] * math.sin(dtor) + point[2] * math.cos(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range(0, 3):
            current[count][i] = point[i]
        count += 1
        # print(PyramidPointCloud[i])
    for i in range(0, len(current)):
        for j in range(0, 3):
            current[i][j] += refPoint[j]
    # print("rotateX stub executed.")


# Draw all objects in the scene
def drawScene():
    # If the shape being drawn is the currently selected one, draw it in red
    for shape in Scene:
        if shape == ObjectData[selected]:
            drawObject(shape, "red")
        else:
            drawObject(shape, "black")


# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(Shape, color):
    # for each polygon in the given object, draw it
    for polygon in Shape:
        drawPoly(polygon, color)
    # print("drawObject stub executed.")


# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.
def drawPoly(poly, color):
    # for each point in a polygon, draw a line between them
    for i in range(0, len(poly)):
        drawLine(poly[i], poly[(i + 1) % len(poly)], color)
    # print("drawPoly stub executed.")


# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# then draw the actual line using the built-in create_line method
def drawLine(start, end, color):
    # get the perspective projection for both points, convert it to display coordinates, then
    # finally draw a line between the two.
    startproject = project(start)
    # print(startproject)
    endproject = project(end)
    # print(endproject)
    startdisplay = convertToDisplayCoordinates(startproject)
    enddisplay = convertToDisplayCoordinates(endproject)
    w.create_line(
        startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1], fill=color
    )
    # print("drawLine stub executed.")


# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    # calculate the perspective projection for each axis of a point and add them to an array which is returned
    ps = []
    for coord in point:
        ps.append(coord / (-d + point[2]) * -d)
    return ps


# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    # calculate the 2D display coordinate for the X and Y axis and return both in an array
    displayXY = []
    displayXY.append(CanvasWidth / 2 + point[0])
    displayXY.append(CanvasHeight / 2 - point[1])
    return displayXY


# **************************************************************************
# Everything below this point implements the interface
def switchObject():
    w.delete(ALL)
    global selected
    selected = (selected + 3) % 9
    drawScene()


def reset():
    w.delete(ALL)
    resetObject(ObjectData[selected + 1], ObjectData[selected + 2])
    drawScene()


def larger():
    w.delete(ALL)
    scale(ObjectData[selected + 1], 1.1)
    drawScene()


def smaller():
    w.delete(ALL)
    scale(ObjectData[selected + 1], 0.9)
    drawScene()


def forward():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [0, 0, 5])
    drawScene()


def backward():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [0, 0, -5])
    drawScene()


def left():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [-5, 0, 0])
    drawScene()


def right():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [5, 0, 0])
    drawScene()


def up():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [0, 5, 0])
    drawScene()


def down():
    w.delete(ALL)
    translate(ObjectData[selected + 1], [0, -5, 0])
    drawScene()


def xPlus():
    w.delete(ALL)
    rotateX(ObjectData[selected + 1], 5)
    drawScene()


def xMinus():
    w.delete(ALL)
    rotateX(ObjectData[selected + 1], -5)
    drawScene()


def yPlus():
    w.delete(ALL)
    rotateY(ObjectData[selected + 1], 5)
    drawScene()


def yMinus():
    w.delete(ALL)
    rotateY(ObjectData[selected + 1], -5)
    drawScene()


def zPlus():
    w.delete(ALL)
    rotateZ(ObjectData[selected + 1], 5)
    drawScene()


def zMinus():
    w.delete(ALL)
    rotateZ(ObjectData[selected + 1], -5)
    drawScene()


root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawScene()
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

selectioncontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
selectioncontrols.pack(side=LEFT)

selectioncontrolslabel = Label(selectioncontrols, text="Select")
selectioncontrolslabel.pack()

selectNextButton = Button(selectioncontrols, text="Next", command=switchObject)
selectNextButton.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

downButton = Button(translatecontrols, text="DN", command=down)
downButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

root.mainloop()
