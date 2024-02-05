from Vector3 import Vector3
from math import cos, sin, sqrt, pi
import pygame

# Circles are not considered polygons
class Circle:

    def __init__(self, x, y, r):
        self.pos = Vector3(x, y)
        self.radius = r
        self.colliding = False

    # all transformations are performed assuming the origin provided or the origin of the screen if none
    def translate(self, v):
        self.pos = self.pos + v
    
    def scale(self, s):
        self.radius = self.radius * s

    # Included for consistency
    def rotate(self, theta):
        pass

    def furthestPoint(self, d):
        theta = d.angle()
        return Vector3(self.radius * cos(theta), self.radius * sin(theta)) + self.pos
    
    def display(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos.x, self.pos.y), self.radius, 1)

class Polygon:

    def __init__(self, x, y, points):
        self.pos = Vector3(x, y)
        self.points = points
        self.colliding = False

    # all transformations are performed assuming the origin provided or the origin of the screen if none
    def translate(self, v):
        for i in range(len(self.points)):
            self.points[i] = self.points[i] + v
        self.pos = self.pos + v
    
    def scale(self, s):
        for i in range(len(self.points)):
            self.points[i]= (self.points[i] - self.pos).scale(s) + self.pos

    # Negated theta because a y-up coordinate system is assumed
    def rotate(self, theta):
        for i in range(len(self.points)):
            self.points[i] = (self.points[i] - self.pos).rotate(-theta) + self.pos

    def furthestPoint(self, d):
        result = self.points[0]
        dotmax = d.dot(result)
        for point in self.points:
            product = d.dot(point)
            if product > dotmax:
                dotmax = product
                result = point
        return result
    
    def toScreenCoords(self):
        screenCoords = []
        for point in self.points:
            screenCoords.append((point.x, point.y))
        return (tuple(screenCoords))
    
    def display(self, screen, color):
        pygame.draw.polygon(screen, color, self.toScreenCoords(), 1)
    
class Square(Polygon):

    def __init__(self, x, y, s):
        r = s/2
        points = [Vector3(x-r, y-r),
                  Vector3(x+r, y-r),
                  Vector3(x+r, y+r),
                  Vector3(x-r, y+r),]
        super().__init__(x, y, points)

class Triangle(Polygon):

    def __init__(self, x, y, s):
        points = [Vector3(x, y-sqrt(3)/3*s),
                  Vector3(x+s/2, y+sqrt(3)/6*s),
                  Vector3(x-s/2, y+sqrt(3)/6*s),]
        super().__init__(x, y, points)

class Pentagon(Polygon):

    def __init__(self, x, y, s):
        r = sin(3*pi/10)*s/sin(2*pi/5)
        points = [Vector3(x+r*cos(pi/10), y-r*sin(pi/10)),
                  Vector3(x+r*cos(pi/2), y-r*sin(pi/2)),
                  Vector3(x+r*cos(9*pi/10), y-r*sin(9*pi/10)),
                  Vector3(x+r*cos(13*pi/10), y-r*sin(13*pi/10)),
                  Vector3(x+r*cos(17*pi/10), y-r*sin(17*pi/10)),]
        super().__init__(x, y, points)