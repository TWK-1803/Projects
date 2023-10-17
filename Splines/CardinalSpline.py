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
        self.curves = self.generateCurves(self.pointCloud)