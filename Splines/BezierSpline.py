from BezierCurve import BezierCurve

class BezierSpline:

    def __init__(self, pointCloud):
        self.curves = self.generateCurves(pointCloud)
        self.pointCloud = self.generatePointCloud()
        self.endPoint = self.getEndPoint(0)

    def getEndPoint(self, t):
        currentcurve = int(t//1)
        u = t%1
        return self.curves[currentcurve].getEndPoint(u)
        
    def generateCurves(self, pointCloud):
        curves = []
        for i in range(len(pointCloud)-1):
            tmp1 = [1/4*(3*pointCloud[i][0]+pointCloud[i+1][0]), 1/4*(3*pointCloud[i][1]+pointCloud[i+1][1])]
            tmp2 = [1/4*(pointCloud[i][0]+3*pointCloud[i+1][0]), 1/4*(pointCloud[i][1]+3*pointCloud[i+1][1])]
            tmpPointCloud = [pointCloud[i], tmp1, tmp2, pointCloud[i+1]]
            curves.append(BezierCurve(tmpPointCloud))
        
        return curves

    def setPoint(self, index, point):
        i = int(index//3)
        i1 = int(index//3)-1
        self.pointCloud[index] = point
        if index%3 != 0:
            self.curves[i].pointCloud[index%3] = point
        
        elif index != 0 and index != len(self.pointCloud)-1:
            self.curves[i].pointCloud[0] = point
            self.curves[i1].pointCloud[-1] = point
        
        elif index == len(self.pointCloud)-1:
            self.curves[i1].pointCloud[-1] = point
        
        else:
            self.curves[i].pointCloud[0] = point
            
    def generatePointCloud(self):
        pointCloud = []
        for curve in self.curves:
            for point in curve.pointCloud:
                if point not in pointCloud:
                    pointCloud.append(point)
        
        return pointCloud
    
    def getMainPointCloud(self):
        return [self.pointCloud[i] for i in range(0,len(self.pointCloud), 3)]