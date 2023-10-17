from copy import deepcopy

class BezierCurve:
    
    def __init__(self, pointCloud):
        self.pointCloud = pointCloud
        self.endPoint = self.getEndPoint(0)

    def getEndPoint(self, t):
        currentpoints = self.pointCloud
        while len(currentpoints) > 1:
            temppoints = []
            for i in range(len(currentpoints)-1):
                temppoints.append(self.lerp(currentpoints[i], currentpoints[i+1], t))
            
            currentpoints = deepcopy(temppoints)
        
        return currentpoints[0]

    def setPoint(self, index, point):
        self.pointCloud[index] = point

    def lerp(self, start, end, t):
        return [start[0] + (end[0] - start[0]) * t,
                start[1] + (end[1] - start[1]) * t]
    
    def getMainPointCloud(self):
        return self.pointCloud