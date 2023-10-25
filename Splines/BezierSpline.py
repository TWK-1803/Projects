from BezierCurve import BezierCurve


class BezierSpline:
    def __init__(self, pointCloud):
        self.pointCloud = self.generatePointCloud(pointCloud)
        self.curves = self.generateCurves(self.pointCloud)
        self.endPoint = self.getEndPoint(0)

    def getEndPoint(self, t):
        currentcurve = int(t // 1)
        u = t % 1
        return self.curves[currentcurve].getEndPoint(u)

    def generateCurves(self, pointCloud):
        curves = []
        for i in range(0, len(pointCloud)-1, 3):
            tmpPointCloud = [pointCloud[i], pointCloud[i+1], pointCloud[i+2], pointCloud[i + 3]]
            curves.append(BezierCurve(tmpPointCloud))

        return curves
    
    def generatePointCloud(self, pointCloud):
        points = []
        for i in range(len(pointCloud) - 1):
            tmp1 = [
                1 / 4 * (3 * pointCloud[i][0] + pointCloud[i + 1][0]),
                1 / 4 * (3 * pointCloud[i][1] + pointCloud[i + 1][1]),
            ]
            tmp2 = [
                1 / 4 * (pointCloud[i][0] + 3 * pointCloud[i + 1][0]),
                1 / 4 * (pointCloud[i][1] + 3 * pointCloud[i + 1][1]),
            ]
            points.append(pointCloud[i])
            points.append(tmp1)
            points.append(tmp2)
        points.append(pointCloud[-1])

        return points

    def getMainPointCloud(self):
        return [self.pointCloud[i] for i in range(0, len(self.pointCloud), 3)]

    def setPoint(self, index, point):
        if index % 3 != 0:
            self.pointCloud[index] = point

        else:
            if index != 0:
                velocityBehind = [self.pointCloud[index-1][0] - self.pointCloud[index][0], self.pointCloud[index-1][1] - self.pointCloud[index][1]]
                self.pointCloud[index-1] = [point[0] + velocityBehind[0], point[1] + velocityBehind[1]]

            if index != len(self.pointCloud) - 1:
                velocityAhead = [self.pointCloud[index+1][0] - self.pointCloud[index][0], self.pointCloud[index+1][1] - self.pointCloud[index][1]]
                self.pointCloud[index+1] = [point[0] + velocityAhead[0], point[1] + velocityAhead[1]]

            self.pointCloud[index] = point

        self.curves = self.generateCurves(self.pointCloud)