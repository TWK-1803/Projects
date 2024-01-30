from math import sqrt, sin, cos, atan2
type Vector3 = Vector3

class Vector3:

    def __init__(self, x, y=None, w=None):
        self.x = x
        self.y = y if y is not None else x
        self.w = w if w is not None else 0


    def normalize(self) -> Vector3:
        m = self.length()
        if m == 0:
            return self
        return self/m

    def dot(self, v: Vector3) -> float:
        if type(v) is not Vector3:
            raise TypeError("Unsupported type for dot product")
        return self.x * v.x + self.y * v.y + self.w * v.w

    def dot2(self) -> Vector3:
        return self.dot(self)

    def cross(self, v: Vector3) -> Vector3:
        if type(v) is not Vector3:
            raise TypeError("Unsupported type for cross product")
        return Vector3(self.y * v.w - self.w * v.y, self.w * v.x - self.x * v.w, self.x * v.y - self.y * v.x)
    
    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.w**2)
    
    def angle(self) -> float:
        return atan2(self.y, self.x)
    
    def translate(self, v: Vector3) -> Vector3:
        if type(v) is not Vector3:
            raise TypeError("Cannot translate vector by a non-vector")
        return self + v
    
    def scale(self, s: int | float) -> Vector3:
        if type(s) is not int and type(s) is not float:
            raise TypeError("Cannot scale vector by a non-scalar")
        return self * s
    
    def rotate(self, theta: int | float) -> Vector3:
        if type(theta) is not int and type(theta) is not float:
            raise TypeError("Cannot rotate vector by a non-scalar")
        return Vector3(self.x * cos(theta) - self.y * sin(theta), self.x * sin(theta) + self.y * cos(theta), self.w)

    # Overriding for comparisons to other Vector3
    def __eq__(self, v: Vector3) -> bool: 
        if type(v) is not Vector3:
            raise TypeError("Cannot equate object of type Vector3 to type {}".format(type(v)))
        return self.x == v.x and self.y == v.y and self.w == v.w
    
    def __add__(self, b: int | float | Vector3) -> Vector3:
        if  type(b) is not Vector3 and type(b) is not int and type(b) is not float:
            raise TypeError("Unsupported type for addition")
        if type(b) is Vector3:
            return Vector3(self.x + b.x, self.y + b.y, self.w + b.w)
        else:
            return Vector3(self.x + b, self.y + b, self.w + b)

    def __sub__(self, b: int | float | Vector3) -> Vector3:
        if  type(b) is not Vector3 and type(b) is not int and type(b) is not float:
            raise TypeError("Unsupported type for subtraction")
        if type(b) is Vector3:
            return Vector3(self.x - b.x, self.y - b.y, self.w - b.w)
        else:
            return Vector3(self.x - b, self.y - b, self.w - b)

    def __neg__(self) -> Vector3:
        return Vector3(-self.x, -self.y, -self.w)
    
    def __truediv__(self, b: int | float) -> Vector3:
        if type(b) is not int and type(b) is not float:
            raise TypeError("Division of vectors with non-scalars is unexpected behaviour")
        return Vector3(self.x / b, self.y / b, self.w / b)
    
    def __mul__(self, b: int | float) -> Vector3:
        if type(b) is not int and type(b) is not float:
            raise TypeError("Multiplication of vectors with non-scalars is unexpected behaviour")
        return Vector3(self.x * b, self.y * b, self.w * b)
    
    def __str__(self) -> str:
        return "({},{},{})".format(self.x, self.y, self.w)