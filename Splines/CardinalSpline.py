from BezierCurve import BezierCurve

class CardinalSpline():

    def __init__(self, pointCloud, tension=1):
        self.tension = tension
        self.velocities = self.generateVelocities(pointCloud)
        self.curves = self.generateCurves(pointCloud)
        self.pointCloud = pointCloud
        self.endPoint = self.getEndPoint(0)
    
    def generateVelocities(self, pointCloud):
        velocities = []
        for i in range(len(pointCloud)):
            if i == 0:
                vx = (pointCloud[0][0] - pointCloud[1][0])
                vy = (pointCloud[0][1] - pointCloud[1][1])
                tmp = [pointCloud[0][0] + vx, pointCloud[0][1] + vy]
                velocities.append([(pointCloud[1][0]-tmp[0])*self.tension, (pointCloud[1][1]-tmp[1])*self.tension])
            
            elif i == len(pointCloud)-1:
                vx = (pointCloud[i][0] - pointCloud[i-1][0])
                vy = (pointCloud[i][1] - pointCloud[i-1][1])
                tmp = [pointCloud[i][0] + vx, pointCloud[i][1] + vy]
                velocities.append([(tmp[0]-pointCloud[i-1][0])*self.tension, (tmp[1]-pointCloud[i-1][1])*self.tension])
            
            else:
                vx = (pointCloud[i+1][0] - pointCloud[i-1][0])
                vy = (pointCloud[i+1][1] - pointCloud[i-1][1])
                velocities.append([vx*self.tension, vy*self.tension])
        
        return velocities
    
    def generateCurves(self, pointCloud):
        curves = []
        for i in range(len(pointCloud)-1):
            tmp1 = [pointCloud[i][0]+self.velocities[i][0]/3, pointCloud[i][1]+self.velocities[i][1]/3]
            tmp2 = [pointCloud[i+1][0]-self.velocities[i+1][0]/3, pointCloud[i+1][1]-self.velocities[i+1][1]/3]
            tmpPointCloud = [pointCloud[i], tmp1, tmp2, pointCloud[i+1]]
            curves.append(BezierCurve(tmpPointCloud))

        return curves

    def getEndPoint(self, t):
        currentcurve = int(t//1)
        u = t%1
        return self.curves[currentcurve].getEndPoint(u)
    
    def getMainPointCloud(self):
        return self.pointCloud
    
    def setPoint(self, index, point):
        self.pointCloud[index] = point
        self.velocities = self.generateVelocities(self.pointCloud)

        if index != 0 and index != len(self.pointCloud)-1:
            self.curves[index].pointCloud[0] = point
            self.curves[index-1].pointCloud[-1] = point

            currentCurvePoint = self.curves[index].pointCloud[0]
            currentCurveEndPoint = self.curves[index].pointCloud[-1]
            previousCurvePoint = self.curves[index-1].pointCloud[-1]
            previousCurveStartPoint = self.curves[index-1].pointCloud[0]
            self.curves[index].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[index][0]/3), currentCurvePoint[1]+(self.velocities[index][1]/3)]
            self.curves[index].pointCloud[2] = [currentCurveEndPoint[0]-(self.velocities[index+1][0]/3), currentCurveEndPoint[1]-(self.velocities[index+1][1]/3)]
            self.curves[index-1].pointCloud[1] = [previousCurveStartPoint[0]+(self.velocities[index-1][0]/3),previousCurveStartPoint[1]+(self.velocities[index-1][1]/3)]
            self.curves[index-1].pointCloud[2] = [previousCurvePoint[0]-(self.velocities[index][0]/3), previousCurvePoint[1]-(self.velocities[index][1]/3)]

        elif index == len(self.pointCloud)-1:
            self.curves[index-1].pointCloud[-1] = point
            previousCurvePoint = self.curves[index-1].pointCloud[-1]
            previousCurveStartPoint = self.curves[index-1].pointCloud[0]
            self.curves[index-1].pointCloud[1] = [previousCurveStartPoint[0]+(self.velocities[index-1][0]/3),previousCurveStartPoint[1]+(self.velocities[index-1][1]/3)]
            self.curves[index-1].pointCloud[2] = [previousCurvePoint[0]-(self.velocities[index][0]/3), previousCurvePoint[1]-(self.velocities[index][1]/3)]

        else:
            self.curves[index].pointCloud[0] = point
            currentCurvePoint = self.curves[0].pointCloud[0]
            currentCurveEndPoint = self.curves[0].pointCloud[-1]
            self.curves[index].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[index][0]/3), currentCurvePoint[1]+(self.velocities[index][1]/3)]
            self.curves[index].pointCloud[2] = [currentCurveEndPoint[0]-(self.velocities[index+1][0]/3), currentCurveEndPoint[1]-(self.velocities[index+1][1]/3)]