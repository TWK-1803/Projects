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
        if index != 0 and index != len(self.pointCloud)-1:
            self.curves[index].pointCloud[0] = point
            self.curves[index-1].pointCloud[-1] = point
            
        elif index == len(self.pointCloud)-1:
            self.curves[index-1].pointCloud[-1] = point
            
        else:
            self.curves[index].pointCloud[0] = point

        if index == 0:
            vx = (self.pointCloud[0][0] - self.pointCloud[1][0])
            vy = (self.pointCloud[0][1] - self.pointCloud[1][1])
            tmp = [self.pointCloud[0][0] + vx, self.pointCloud[0][1] + vy]
            self.velocities[0] = [(self.pointCloud[1][0]-tmp[0])*self.tension, (self.pointCloud[1][1]-tmp[1])*self.tension]
            
            currentCurvePoint = self.curves[0].pointCloud[0]
            self.curves[0].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[0][0]/3), currentCurvePoint[1]+(self.velocities[0][1]/3)]
            
        elif index == len(self.pointCloud) - 1:
            vx = (self.pointCloud[index][0] - self.pointCloud[index-1][0])
            vy = (self.pointCloud[index][1] - self.pointCloud[index-1][1])
            tmp = [self.pointCloud[index][0] + vx, self.pointCloud[index][1] + vy]
            self.velocities[index] = [(tmp[0]-self.pointCloud[index-1][0])*self.tension, (tmp[1]-self.pointCloud[index-1][1])*self.tension]

            f = self.velocities[index]
            previousCurvePoint = self.curves[index-1].pointCloud[-1]
            self.curves[index-1].pointCloud[-2] = [previousCurvePoint[0]-(self.velocities[index][0]/3), previousCurvePoint[1]-(self.velocities[index][1]/3)]
            
        elif index == 1:
            vx1 = (self.pointCloud[0][0] - self.pointCloud[index][0])
            vy1 = (self.pointCloud[0][1] - self.pointCloud[index][1])
            tmp1 = [self.pointCloud[0][0] + vx1, self.pointCloud[0][1] + vy1]
            self.velocities[index-1] = [(self.pointCloud[index][0]-tmp1[0])*self.tension, (self.pointCloud[index][1]-tmp1[1])*self.tension]

            vx2 = (self.pointCloud[index+1][0] - self.pointCloud[index][0])
            vy2 = (self.pointCloud[index+1][1] - self.pointCloud[index][1])

            if len(self.pointCloud) == 3:
                tmp2 = [self.pointCloud[index+1][0] + vx2, self.pointCloud[index+1][1] + vy2]
                self.velocities[index+1] = [(tmp[0]-self.pointCloud[index][0])*self.tension, (tmp[1]-self.pointCloud[index][1])*self.tension]
            
            else:
                self.velocities[index+1] = [(self.pointCloud[index+2][0]-self.pointCloud[index][0])*self.tension, (self.pointCloud[index+2][1]-self.pointCloud[index][1])*self.tension]

            currentCurvePoint = self.curves[index].pointCloud[0]
            previousCurvePoint = self.curves[index-1].pointCloud[-1]
            self.curves[index].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[index][0]/3), currentCurvePoint[1]+(self.velocities[index][1]/3)]
            self.curves[index-1].pointCloud[-2] = [previousCurvePoint[0]-(self.velocities[index][0]/3), previousCurvePoint[1]-(self.velocities[index][1]/3)]
            
        elif index == len(self.pointCloud) - 2:
            vx2 = (self.pointCloud[index+1][0] - self.pointCloud[index][0])
            vy2 = (self.pointCloud[index+1][1] - self.pointCloud[index][1])
            tmp2 = [self.pointCloud[index+1][0] + vx2, self.pointCloud[index+1][1] + vy2]
            self.velocities[index+1] = [(tmp2[0]-self.pointCloud[index][0])*self.tension, (tmp2[1]-self.pointCloud[index][1])*self.tension]

            self.velocities[index-1] = [(self.pointCloud[index][0]-self.pointCloud[index-2][0])*self.tension, (self.pointCloud[index][1]-self.pointCloud[index-2][1])*self.tension]

            currentCurvePoint = self.curves[index].pointCloud[0]
            previousCurvePoint = self.curves[index-1].pointCloud[-1]
            self.curves[index].pointCloud[1] = [currentCurvePoint[0]+(self.velocities[index][0]/3), currentCurvePoint[1]+(self.velocities[index][1]/3)]
            self.curves[index-1].pointCloud[-2] = [previousCurvePoint[0]-(self.velocities[index][0]/3), previousCurvePoint[1]-(self.velocities[index][1]/3)]
            
        