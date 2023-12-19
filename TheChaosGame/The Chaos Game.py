#############################################################################################################################
# Name: Tyler Kranz
# Date: 03/25/19
# Description: This program creates points on a coordinate plane and can output a variety of mathmatical facts involving them
#############################################################################################################################
import math
from tkinter import *
from random import randint


# the 2D point class
class Point(object):
    # x and y are not declared floats in the parameters because the function needs to translate integer inputs
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    # getters and setters for both x and y
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # the magic function for the output of points as a string
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # this method calculates the float value of the distance between two given points
    def dist(self, point2):
        return math.sqrt(pow(point2.x - self.x, 2) + pow(point2.y - self.y, 2))

    # this method calculates a floating point exactly between itself and another point
    def midpt(self, point2):
        tx = (point2.x + self.x) / 2
        ty = (point2.y + self.y) / 2
        return Point(tx, ty)


# The Coordinate System class
class CoordinateSystem(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, numPoints):
        # manually draw the initial verticies  and the first calculated midpoint to the canvas
        for i in range(0, len(verts)):
            self.draw(verts[i], 2, "red")

        firstMid = verts[0].midpt(verts[1])
        listPoints.append(firstMid)
        self.draw(firstMid, 0, "black")

        # find the midpoint between the last generated midpoint and random vertex and draw it to the canvas
        for i in range(numPoints):
            newMid = listPoints[len(listPoints) - 1].midpt(verts[randint(0, 2)])
            listPoints.append(newMid)
            self.draw(listPoints[len(listPoints) - 1], 0, "black")

    def draw(self, p1, radius, color):
        # This draws the point provided to the canvas"
        self.create_oval(
            p1.x, p1.y, p1.x + radius * 2, p1.y + radius * 2, outline=color, fill=color
        )


# predefining the first 3 points of the pattern
vert1 = Point(300, 3)
vert2 = Point(4, 516)
vert3 = Point(596, 516)
verts = [vert1, vert2, vert3]
listPoints = []

##########################################################
# the default size of the canvas is 600x520

WIDTH = 600
HEIGHT = 520
# the number of points to plot
NUM_POINTS = 10000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
