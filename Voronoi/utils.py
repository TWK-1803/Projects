from math import sqrt

def clamp(s, n, l) : return max(s, min(n, l))

# Assumes that it is in fact being given a triangle like a silly little program
def calcCircumCirc(A, B, C):

    
    D = 2*(A.x*(B.y-C.y) + B.x*(C.y-A.y) + C.x*(A.y-B.y))
    # Evil hack which makes the spaghetti gods happy and math students cry
    if D == 0:
        D = 1
    
    Cx = (1/D)*((A.x**2+A.y**2)*(B.y-C.y)+(B.x**2+B.y**2)*(C.y-A.y)+(C.x**2+C.y**2)*(A.y-B.y))
    Cy = (1/D)*((A.x**2+A.y**2)*(C.x-B.x)+(B.x**2+B.y**2)*(A.x-C.x)+(C.x**2+C.y**2)*(B.x-A.x))

    a = (A-B).length()
    b = (A-C).length()
    c = (B-C).length()
    denom = (a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c)
    if denom == 0:
        R = 0
    else:
        R = (a*b*c)/sqrt(denom)

    return CircumCircle(Cx, Cy, R)

def superTriangle(vertices):
    minx, miny = 9999, 9999
    maxx, maxy = -9999, -9999
    for vertex in vertices:
        minx = min(minx, vertex.x)
        miny = min(minx, vertex.y)
        maxx = max(maxx, vertex.x)
        maxy = max(maxx, vertex.y)

    dx = (maxx - minx) * 10
    dy = (maxy - miny) * 10

    v0 = Vertex(minx - dx, miny - dy * 3)
    v1 = Vertex(minx - dx, maxy + dy)
    v2 = Vertex(maxx + dx * 3, maxy + dy)

    return Triangle(v0, v1, v2)

def triangulate(vertices):
    st = superTriangle(vertices)

    triangles = [st]

    for vertex in vertices:
        triangles = addVertex(vertex, triangles)

    for triangle in triangles:
        if sharesVertex(triangle, st):
            triangle.sharesVertexWithSuper = True

    return triangles


def sharesEdge(t1, t2):
    return (t1.e0 == t2.e0 or t1.e0 == t2.e1 or t1.e0 == t2.e2 or
        t1.e1 == t2.e0 or t1.e1 == t2.e1 or t1.e1 == t2.e2 or
        t1.e2 == t2.e0 or t1.e2 == t2.e1 or t1.e2 == t2.e2)

def sharesVertex(t1, t2):
    return (t1.v0 == t2.v0 or t1.v0 == t2.v1 or t1.v0 == t2.v2 or
        t1.v1 == t2.v0 or t1.v1 == t2.v1 or t1.v1 == t2.v2 or
        t1.v2 == t2.v0 or t1.v2 == t2.v1 or t1.v2 == t2.v2)

def addVertex(vertex, t):
    edges = []

    triangles = []
    
    for triangle in t:
        if (triangle.inCircumcircle(vertex)):
            edges.append(Edge(triangle.v0, triangle.v1))
            edges.append(Edge(triangle.v1, triangle.v2))
            edges.append(Edge(triangle.v2, triangle.v0))
            continue
        triangles.append(triangle)

    edges = uniqueEdges(edges)

    for edge in edges:
        triangles.append(Triangle(edge.v0, edge.v1, vertex))

    return triangles

def uniqueEdges(edges):
    uniqueEdges = []
    for i in range(len(edges)):
        isUnique = True
        for j in range(len(edges)):
            if (i != j and edges[i] == edges[j]):
                isUnique = False
                break

        if isUnique:
            uniqueEdges.append(edges[i])

    return uniqueEdges

class Vertex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, vertex):
        return self.x == vertex.x and self.y == vertex.y
    
    def __sub__(self, v):
        return Vertex(self.x-v.x, self.y-v.y)

    def length(self):
        return sqrt(self.x**2+self.y**2)
    
class Edge:

    def __init__(self, v0, v1):
        self.v0 = v0
        self.v1 = v1
    
    def __eq__(self, edge):
        return (self.v0 == edge.v0 and self.v1 == edge.v1) or (self.v0 == edge.v1 and self.v1 == edge.v0)
    
class Triangle:
    
    def __init__(self, v0, v1, v2):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.e0 = Edge(v0, v1)
        self.e1 = Edge(v0, v2)
        self.e2 = Edge(v1, v2)
        self.circumCirc = calcCircumCirc(v0,v1,v2)
        self.sharesVertexWithSuper = False
        
    def inCircumcircle(self, v):
        dx = self.circumCirc.x - v.x
        dy = self.circumCirc.y - v.y
        return sqrt(dx**2 + dy**2) <= self.circumCirc.r

class CircumCircle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r