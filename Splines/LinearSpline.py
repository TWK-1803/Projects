class LinearSpline():
    
    def __init__(self, pointCloud):
        self.pointCloud = pointCloud
        self.endPoint = self.getEndPoint(0)

    def getEndPoint(self, t):
        currentsegment = int(t//1)
        u = t%1
        if currentsegment == len(self.pointCloud) - 1:
            return self.pointCloud[currentsegment]
        
        else:
            vx = (self.pointCloud[currentsegment+1][0] - self.pointCloud[currentsegment][0])*u
            vy = (self.pointCloud[currentsegment+1][1] - self.pointCloud[currentsegment][1])*u
            return [self.pointCloud[currentsegment][0] + vx, self.pointCloud[currentsegment][1] + vy]

    def setPoint(self, index, point):
        self.pointCloud[index] = point

    
    def getMainPointCloud(self):
        return self.pointCloud