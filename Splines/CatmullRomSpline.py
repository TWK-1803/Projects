from CardinalSpline import CardinalSpline

class CatmullRomSpline(CardinalSpline):

    def __init__(self, pointCloud):
        super().__init__(pointCloud, 0.5)