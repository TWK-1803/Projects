from Utils import *

class Circle:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def SignedDistance(self, a):
        distance = length([(a[0] - self.position[0]), (a[1] - self.position[1])])
        return distance - self.radius

class Square:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def SignedDistance(self, a):
        a = [abs(a[0]-self.position[0]), abs(a[1]-self.position[1])]
        return length([max(a[0]-self.radius, 0),max(a[1]-self.radius, 0)])
    
class Triangle:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def SignedDistance(self, a):
        a = [a[0]-self.position[0], -(a[1]-self.position[1])]
        k = sqrt(3.0)
        a[0] = abs(a[0]) - self.radius
        a[1] = a[1] + self.radius/k
        if(a[0]+k*a[1] > 0.0 ): a = [(a[0]-k*a[1])/2, (-k*a[0]-a[1])/2.0]
        a[0] -= clamp(a[0], -2.0*self.radius, 0.0)
        return -length(a)*-1 if a[1] < 0.0 else 0.0 if a[1] == 0.0 else -length(a)
    
class Pentagon:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def SignedDistance(self, a):
        a = [abs(a[0]-self.position[0]), (a[1]-self.position[1])]
        k = [0.809016994,0.587785252,0.726542528]
        scalar = 2.0*min(dot([-k[0],k[1]],a),0.0)
        a[0] -= scalar*-k[0]
        a[1] -= scalar*k[1]
        scalar = 2.0*min(dot([k[0],k[1]],a),0.0)
        a[0] -= scalar*k[0]
        a[1] -= scalar*k[1]
        a[0] -= clamp(a[0],-self.radius*k[2],self.radius*k[2])
        a[1] -= self.radius
        return length(a)*-1 if a[1] < 0.0 else 0.0 if a[1] == 0.0 else length(a)
    
class Hexagram:
    def __init__(self, x, y, radius):
        self.position = [x, y]
        self.radius = radius

    def SignedDistance(self, a):
        a = [abs(a[0]-self.position[0]), abs(a[1]-self.position[1])]
        k = [-0.5,0.8660254038,0.5773502692,1.7320508076]
        scalar = 2.0*min(dot([k[0],k[1]],a),0.0)
        a[0] -= scalar*k[0]
        a[1] -= scalar*k[1]
        scalar = 2.0*min(dot([k[1],k[0]],a),0.0)
        a[0] -= scalar*k[1]
        a[1] -= scalar*k[0]
        a[0] -= clamp(a[0],self.radius*k[2],self.radius*k[3])
        a[1] -= self.radius
        return length(a)*-1 if a[1] < 0.0 else 0.0 if a[1] == 0.0 else length(a)