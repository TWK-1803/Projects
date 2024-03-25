from math import sqrt

def distance(p1, p2): return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

class Segment:

    def __init__(self, points: list, connectors: list):
        self.points = points
        self.connectors = connectors
        self.totalLength = 0
        for connector in connectors:
            self.totalLength += connector.length

class Connector:

    def __init__(self, point1, point2, length):
        self.point1 = point1
        self.point2 = point2
        self.length = length
        self.angle = 0