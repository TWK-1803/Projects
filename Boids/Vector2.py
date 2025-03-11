from math import sqrt, sin, cos, atan2
type Vector2=Vector2

class Vector2:

    def __init__(self, x, y=None):
        self.x = x
        self.y = y if y is not None else x

    def normalize(self) -> Vector2:
        m = self.length()
        if m == 0:
            return self
        return self/m

    def dot(self, v: Vector2) -> float:
        if type(v) is not Vector2:
            raise TypeError("Unsupported type for dot product")
        return self.x * v.x + self.y * v.y

    def dot2(self) -> Vector2:
        return self.dot(self)
    
    def length(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    
    def angle(self) -> float:
        return atan2(self.y, self.x)
    
    def translate(self, v: Vector2) -> Vector2:
        if type(v) is not Vector2:
            raise TypeError("Cannot translate vector by a non-vector")
        return self + v
    
    def scale(self, s: int | float) -> Vector2:
        if type(s) is not int and type(s) is not float:
            raise TypeError("Cannot scale vector by a non-scalar")
        return self * s
    
    def rotate(self, theta: int | float) -> Vector2:
        if type(theta) is not int and type(theta) is not float:
            raise TypeError("Cannot rotate vector by a non-scalar")
        return Vector2(self.x * cos(theta) - self.y * sin(theta), self.x * sin(theta) + self.y * cos(theta))
    
    def limit(self, l: int | float) -> Vector2:
        if type(l) is not int and type(l) is not float:
            raise TypeError("Cannot limit vector length to a non-scalar")
        if self.length() > l:
            return self.normalize() * l
        return self

    # Overriding for comparisons to other Vector2
    def __eq__(self, v: Vector2) -> bool: 
        if type(v) is not Vector2:
            raise TypeError("Cannot equate object of type Vector2 to type {}".format(type(v)))
        return self.x == v.x and self.y == v.y
    
    def __add__(self, b: Vector2) -> Vector2:
        if  type(b) is not Vector2:
            raise TypeError("Unsupported type for addition")
        return Vector2(self.x + b.x, self.y + b.y)

    def __sub__(self, b: Vector2) -> Vector2:
        if  type(b) is not Vector2:
            raise TypeError("Unsupported type for subtraction")
        return Vector2(self.x - b.x, self.y - b.y)
        
    def __neg__(self) -> Vector2:
        return Vector2(-self.x, -self.y)
    
    def __truediv__(self, b: int | float) -> Vector2:
        if type(b) is not int and type(b) is not float:
            raise TypeError("Division of vectors with non-scalars is unexpected behaviour")
        return Vector2(self.x / b, self.y / b)
    
    def __mul__(self, b: int | float) -> Vector2:
        if type(b) is not int and type(b) is not float:
            raise TypeError("Multiplication of vectors with non-scalars is unexpected behaviour")
        return Vector2(self.x * b, self.y * b)
    
    def __str__(self) -> str:
        return "({},{})".format(self.x, self.y)