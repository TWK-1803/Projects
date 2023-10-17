from BezierCurve import BezierCurve

class HermiteSpline():

    def __init__(self, pointCloud):
        self.velocities = self.generateVelocities(pointCloud)
        self.curves = self.generateCurves(pointCloud)
        self.pointCloud = self.generatePointCloud(pointCloud)
        self.endPoint = self.getEndPoint(0)
    
    def generateVelocities(self, pointCloud):
        velocities = []
        for i in range(len(pointCloud)-1):
            tmp = [(pointCloud[i][0]+pointCloud[i+1][0])/2, (pointCloud[i][1]+pointCloud[i+1][1])/2] 
            velocities.append([tmp[0]-pointCloud[i][0], tmp[1]-pointCloud[i][1]])
        
        velocities.append([30, 30])
        return velocities
    
    def generateCurves(self, pointCloud):
        curves = []
        for i in range(len(pointCloud)-1):
            tmp1 = [pointCloud[i][0]+self.velocities[i][0]/3, pointCloud[i][1]+self.velocities[i][1]/3]
            tmp2 = [pointCloud[i+1][0]-self.velocities[i+1][0]/3, pointCloud[i+1][1]-self.velocities[i+1][1]/3]
            tmpPointCloud = [pointCloud[i], tmp1, tmp2, pointCloud[i+1]]
            curves.append(BezierCurve(tmpPointCloud))

        return curves
    
    def generatePointCloud(self, pointCloud):
        tmp = []
        for i in range(len(pointCloud)):
            tmp.append(pointCloud[i])
            tmp.append([pointCloud[i][0]+self.velocities[i][0], pointCloud[i][1]+self.velocities[i][1]])

        return tmp

    def getEndPoint(self, t):
        currentcurve = int(t//1)
        u = t%1
        return self.curves[currentcurve].getEndPoint(u)
    
    def getMainPointCloud(self):
        return [self.pointCloud[i] for i in range(0,len(self.pointCloud), 2)]
    
    def setPoint(self, index, point):
        i = int(index//2)
        i1 = int(index//2)-1
        self.pointCloud[index] = point

        if index%2 == 0:
            if index != 0 and index != len(self.pointCloud)-2:
                self.curves[i].pointCloud[0] = point
                self.curves[i1].pointCloud[-1] = point
            
            elif index == len(self.pointCloud)-2:
                self.curves[i1].pointCloud[-1] = point
            
            else:
                self.curves[i].pointCloud[0] = point
        
        else:
            self.velocities[i] = [point[0]-self.pointCloud[index-1][0], point[1]-self.pointCloud[index-1][1]]

            if index != 1 and index != len(self.pointCloud)-1:
                currentCurvePoint = self.curves[i].pointCloud[0]
                previousCurvePoint = self.curves[i1].pointCloud[-1]
                self.curves[i].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[i][0]/3), currentCurvePoint[1]+(self.velocities[i][1]/3)]
                self.curves[i1].pointCloud[-2] = [previousCurvePoint[0]-(self.velocities[i][0]/3), previousCurvePoint[1]-(self.velocities[i][1]/3)]
            
            elif index == len(self.pointCloud)-1:
                previousCurvePoint = self.curves[i1].pointCloud[-1]
                self.curves[i1].pointCloud[-2] = [previousCurvePoint[0]+(self.velocities[i][0]/3), previousCurvePoint[1]+(self.velocities[i][1]/3)]
            
            else:
                currentCurvePoint = self.curves[i].pointCloud[0]
                self.curves[i].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[i][0]/3), currentCurvePoint[1]+(self.velocities[i][1]/3)]