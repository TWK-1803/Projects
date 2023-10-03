####################################################################################
# Tyler Kranz 102-63-704
# 12/20/2021
# Assignment 1
# This program draws the wireframe of a pyramid and allows the use to manipulate the
# object using mathematical transformative equations such as: Scaling, Translation,
# and rotation. Note that all math is performed in 3D space where the object is not
# necessarily at the origin
####################################################################################

import math
import copy
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Pyramid Object ***************************
# Definition  of the five underlying points
apex = [0,50,100]
base1 = [50,-50,50]
base2 = [50,-50,150]
base3 = [-50,-50,150]
base4 = [-50,-50,50]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside
frontpoly = [apex,base1,base4]
rightpoly = [apex,base2,base1]
backpoly = [apex,base3,base2]
leftpoly = [apex,base4,base3]
bottompoly = [base1,base2,base3,base4]

# Definition of the object
Pyramid = [bottompoly, frontpoly, rightpoly, backpoly, leftpoly]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
DefaultPyramidPointCloud = copy.deepcopy(PyramidPointCloud)
#************************************************************************************

# This function resets the pyramid to its original size and location in 3D space
# Note that you have to be careful to update the values in the existing PyramidPointCloud
# structure rather than creating a new structure or just switching a pointer.  In other
# words, you'll need manually update the value of every x, y, and z of every point in
# point cloud (vertex list).
def resetPyramid():
    for i in range(len(PyramidPointCloud)):
        for j in range(3):
            PyramidPointCloud[i][j] = DefaultPyramidPointCloud[i][j]

# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.

def translate(object, displacement):
    # iterate through each point and update the XYZ values by adding the corresponding
    # value in the displacement vector
    for i in range (0, len(PyramidPointCloud)):
        for j in range (0,3):
            # print("old: "+PyramidPointCloud[i][j])
            PyramidPointCloud[i][j] += displacement[j]
            # print("new: "+PyramidPointCloud[i][j])
    # print("translate stub executed.")
    
    
# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
def scale(object,scalefactor):
    # iterate through each point and update the XYZ values by multiplying it with the
    # corresponding value in the displacement vector
    for i in range (0, len(PyramidPointCloud)):
        for j in range (0,3):
             # print("old: "+PyramidPointCloud[i][j])
             PyramidPointCloud[i][j] *= scalefactor
             # print("new: "+PyramidPointCloud[i][j])
    # print("scale stub executed.")
    

# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]
def rotateZ(object,degrees):
    # iterate through the points in the cloud and caluculate the rotated positions for
    # each. Only afterward, to avoid pointer issues, does itchange the values of the
    # actual points in the cloud itself using another method to avoid pointer issues
    count = 0
    for point in PyramidPointCloud:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0]*math.cos(dtor)-point[1]*math.sin(dtor))
        rotatedcoords.append(point[0]*math.sin(dtor)+point[1]*math.cos(dtor))
        rotatedcoords.append(point[2])
        point = copy.deepcopy(rotatedcoords)
        for i in range (0,3):
            PyramidPointCloud[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    # print("rotateZ stub executed.")

    
# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object,degrees):
    # iterate through the points in the cloud and caluculate the rotated positions for
    # each. Only afterward, to avoid pointer issues, does itchange the values of the
    # actual points in the cloud itself using another method to avoid pointer issues
    count = 0
    for point in PyramidPointCloud:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0]*math.cos(dtor)+point[2]*math.sin(dtor))
        rotatedcoords.append(point[1])
        rotatedcoords.append(point[2]*math.cos(dtor)-point[0]*math.sin(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range (0,3):
            PyramidPointCloud[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    # print("rotateY stub executed.")


# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object,degrees):
    # iterate through the points in the cloud and caluculate the rotated positions for
    # each. Only afterward, to avoid pointer issues, does itchange the values of the
    # actual points in the cloud itself using another method to avoid pointer issues
    count = 0
    for point in PyramidPointCloud:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0])
        rotatedcoords.append(point[1]*math.cos(dtor)-point[2]*math.sin(dtor))
        rotatedcoords.append(point[1]*math.sin(dtor)+point[2]*math.cos(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range (0,3):
            PyramidPointCloud[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    # print("rotateX stub executed.")


# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(object):
    # for each polygon in the object, draw it
    for polygon in Pyramid:
        drawPoly(polygon)
    # print("drawObject stub executed.")


# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly):
    # for each point in a polygon, draw a line between them
    for i in range (0, len(poly)):
        drawLine(poly[i],poly[(i+1)%len(poly)])
    # print("drawPoly stub executed.")


# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start,end):
    # get the perspective projection for both points, then convert it to display coordinates, then
    # finally draw a line between the two.
    startproject = project(start)
    # print(startproject)
    endproject = project(end)
    # print(endproject)
    startdisplay = convertToDisplayCoordinates(startproject)
    enddisplay = convertToDisplayCoordinates(endproject)
    w.create_line(startdisplay[0],startdisplay[1],enddisplay[0],enddisplay[1])
    # print("drawLine stub executed.")
    

# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    # calculate the perspective projection for each axis of a point and add them to an array which is returned
    ps = []
    for coord in point:
        ps.append(coord/(-d+point[2])*-d)
    return ps


# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    # calculate the 2D display coordinate for the X and Y axis and return both in an array
    displayXY = []
    displayXY.append(CanvasWidth/2+point[0])
    displayXY.append(CanvasHeight/2-point[1])
    return displayXY
    

# **************************************************************************
# Everything below this point implements the interface
def reset():
    w.delete(ALL)
    resetPyramid()
    drawObject(Pyramid)

def larger():
    w.delete(ALL)
    scale(PyramidPointCloud, 1.1)
    drawObject(Pyramid)

def smaller():
    w.delete(ALL)
    scale(PyramidPointCloud, .9)
    drawObject(Pyramid)

def forward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,5])
    drawObject(Pyramid)

def backward():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,0,-5])
    drawObject(Pyramid)

def left():
    w.delete(ALL)
    translate(PyramidPointCloud,[-5,0,0])
    drawObject(Pyramid)

def right():
    w.delete(ALL)
    translate(PyramidPointCloud,[5,0,0])
    drawObject(Pyramid)

def up():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,5,0])
    drawObject(Pyramid)

def down():
    w.delete(ALL)
    translate(PyramidPointCloud,[0,-5,0])
    drawObject(Pyramid)

def xPlus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,5)
    drawObject(Pyramid)

def xMinus():
    w.delete(ALL)
    rotateX(PyramidPointCloud,-5)
    drawObject(Pyramid)

def yPlus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,5)
    drawObject(Pyramid)

def yMinus():
    w.delete(ALL)
    rotateY(PyramidPointCloud,-5)
    drawObject(Pyramid)

def zPlus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,5)
    drawObject(Pyramid)

def zMinus():
    w.delete(ALL)
    rotateZ(PyramidPointCloud,-5)
    drawObject(Pyramid)

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawObject(Pyramid)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

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
