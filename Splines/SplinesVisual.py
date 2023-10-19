from tkinter import *
from BezierCurve import BezierCurve
from BezierSpline import BezierSpline
from HermiteSpline import HermiteSpline
from LinearSpline import LinearSpline
from CardinalSpline import CardinalSpline
from CatmullRomSpline import CatmullRomSpline

width = 800
height = 800
basePointCloud = [[-200, 0], [0, 100], [200, 0], [0, -100], [0, 0]]
splines = []
selectedPoint = -1
drawLines = True
numberOfTSteps = 100
mode = 0


def generateSplines():
    global splines

    splines = [
        BezierCurve(basePointCloud),
        BezierSpline(basePointCloud),
        HermiteSpline(basePointCloud),
        LinearSpline(basePointCloud),
        CardinalSpline(basePointCloud),
        CatmullRomSpline(basePointCloud),
    ]


def drawPointCloud():
    match (mode):
        case 0:
            drawBezierCurvePointCloud()
        case 1:
            drawBezierSplinePointCloud()
        case 2:
            drawHermiteSplinePointCloud()
        case 3:
            drawLinearSplinePointCloud()
        case 4:
            drawCardinalSplinePointCloud()
        case 5:
            drawCatmullRomSplinePointCloud()


def drawSpline():
    match (mode):
        case 0:
            drawBezierCurve()
        case 1:
            drawBezierSpline()
        case 2:
            drawHermiteSpline()
        case 3:
            drawLinearSpline()
        case 4:
            drawCardinalSpline()
        case 5:
            drawCatmullRomSpline()


def drawPoint(point1, point2):
    canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill="black")


def drawBezierCurvePointCloud():
    if drawLines:
        wcoords = []
        for point in splines[0].pointCloud:
            if wcoords != []:
                tmpcoords = getWindowCoords(point)
                canvas.create_line(
                    wcoords[0], wcoords[1], tmpcoords[0], tmpcoords[1], width=1
                )
            wcoords = getWindowCoords(point)
            canvas.create_rectangle(
                wcoords[0] - 5,
                wcoords[1] - 5,
                wcoords[0] + 5,
                wcoords[1] + 5,
                fill="black",
            )


def drawBezierCurve():
    t = 0
    previousPoint = []
    while t < 1:
        splines[0].endPoint = splines[0].getEndPoint(t)
        scoords = getWindowCoords(splines[0].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps
        previousPoint = scoords


def drawBezierSplinePointCloud():
    if drawLines:
        currentCurve = []
        for i in range(len(splines[1].pointCloud)):
            point = getWindowCoords(splines[1].pointCloud[i])
            currentCurve.append(point)
            if i % 3 == 0:
                canvas.create_rectangle(
                    point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5, fill="black"
                )
                if len(currentCurve) >= 4:
                    canvas.create_line(
                        currentCurve[0][0],
                        currentCurve[0][1],
                        currentCurve[3][0],
                        currentCurve[3][1],
                    )
                    canvas.create_line(
                        currentCurve[0][0],
                        currentCurve[0][1],
                        currentCurve[1][0],
                        currentCurve[1][1],
                    )
                    canvas.create_line(
                        currentCurve[2][0],
                        currentCurve[2][1],
                        currentCurve[3][0],
                        currentCurve[3][1],
                    )
                    currentCurve = [currentCurve[-1]]
            else:
                canvas.create_oval(
                    point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3
                )


def drawBezierSpline():
    t = 0
    previousPoint = []
    while t < len(splines[1].curves):
        splines[1].endPoint = splines[1].getEndPoint(t)
        scoords = getWindowCoords(splines[1].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps / len(splines[1].curves)
        previousPoint = scoords


def drawHermiteSplinePointCloud():
    if drawLines:
        currentCurve = []
        for i in range(len(splines[2].pointCloud)):
            point = getWindowCoords(splines[2].pointCloud[i])
            currentCurve.append(point)
            if i % 2 == 0:
                canvas.create_rectangle(
                    point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5, fill="black"
                )
                if len(currentCurve) >= 3:
                    canvas.create_line(
                        currentCurve[0][0],
                        currentCurve[0][1],
                        currentCurve[2][0],
                        currentCurve[2][1],
                    )
                    currentCurve = [currentCurve[-1]]
            else:
                canvas.create_oval(
                    point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3
                )
                canvas.create_line(
                    currentCurve[0][0],
                    currentCurve[0][1],
                    currentCurve[1][0],
                    currentCurve[1][1],
                )


def drawHermiteSpline():
    t = 0
    previousPoint = []
    while t < len(splines[2].curves):
        splines[2].endPoint = splines[2].getEndPoint(t)
        scoords = getWindowCoords(splines[2].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps / len(splines[2].curves)
        previousPoint = scoords


def drawLinearSplinePointCloud():
    if drawLines:
        for point in splines[3].pointCloud:
            wcoords = getWindowCoords(point)
            canvas.create_rectangle(
                wcoords[0] - 5,
                wcoords[1] - 5,
                wcoords[0] + 5,
                wcoords[1] + 5,
                fill="black",
            )


def drawLinearSpline():
    t = 0
    previousPoint = []
    while t < len(splines[3].pointCloud) - 1:
        splines[3].endPoint = splines[3].getEndPoint(t)
        scoords = getWindowCoords(splines[3].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps / (len(splines[3].pointCloud) - 1)
        previousPoint = scoords


def drawCardinalSplinePointCloud():
    if drawLines:
        wcoords = []
        for point in splines[4].pointCloud:
            if wcoords != []:
                tmpcoords = getWindowCoords(point)
                canvas.create_line(
                    wcoords[0], wcoords[1], tmpcoords[0], tmpcoords[1], width=1
                )
            wcoords = getWindowCoords(point)
            canvas.create_rectangle(
                wcoords[0] - 5,
                wcoords[1] - 5,
                wcoords[0] + 5,
                wcoords[1] + 5,
                fill="black",
            )


def drawCardinalSpline():
    t = 0
    previousPoint = []
    while t < len(splines[4].curves):
        splines[4].endPoint = splines[4].getEndPoint(t)
        scoords = getWindowCoords(splines[4].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps / len(splines[4].curves)
        previousPoint = scoords


def drawCatmullRomSplinePointCloud():
    if drawLines:
        wcoords = []
        for point in splines[5].pointCloud:
            if wcoords != []:
                tmpcoords = getWindowCoords(point)
                canvas.create_line(
                    wcoords[0], wcoords[1], tmpcoords[0], tmpcoords[1], width=1
                )
            wcoords = getWindowCoords(point)
            canvas.create_rectangle(
                wcoords[0] - 5,
                wcoords[1] - 5,
                wcoords[0] + 5,
                wcoords[1] + 5,
                fill="black",
            )


def drawCatmullRomSpline():
    t = 0
    previousPoint = []
    while t < len(splines[5].curves):
        splines[5].endPoint = splines[5].getEndPoint(t)
        scoords = getWindowCoords(splines[5].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)
        t += 1 / numberOfTSteps / len(splines[5].curves)
        previousPoint = scoords


def getWindowCoords(coords):
    return [coords[0] + width / 2, -coords[1] + height / 2]


def getCartesianCoords(coords):
    return [coords[0] - width / 2, -(coords[1] - height / 2)]


def click(event):
    global selectedPoint

    if drawLines:
        if selectedPoint == -1:
            for i in range(len(splines[mode].pointCloud)):
                pcoords = getWindowCoords(splines[mode].pointCloud[i])
                if (
                    pcoords[0] - 5 < event.x < pcoords[0] + 5
                    and pcoords[1] - 5 < event.y < pcoords[1] + 5
                ):
                    selectedPoint = i
                    break

        if selectedPoint != -1:
            splines[mode].setPoint(
                selectedPoint, getCartesianCoords([event.x, event.y])
            )
            clearCanvas()


def release(event):
    global selectedPoint

    selectedPoint = -1


def spacePressed(event):
    global drawLines

    drawLines = not drawLines
    clearCanvas()


def clearCanvas():
    canvas.delete(ALL)
    drawPointCloud()
    drawSpline()


def setMode(pressed):
    global mode
    global basePointCloud

    basePointCloud = splines[mode].getMainPointCloud()
    matched = False
    match (pressed.char):
        case "1":
            mode = 0
            matched = True
        case "2":
            mode = 1
            matched = True
        case "3":
            mode = 2
            matched = True
        case "4":
            mode = 3
            matched = True
        case "5":
            mode = 4
            matched = True
        case "6":
            mode = 5
            matched = True
        # case '7':
        #    mode = 6
        #   matched = True
    if matched:
        generateSplines()
    clearCanvas()


root = Tk()
root.bind("<space>", spacePressed)
root.bind("<Key>", lambda i: setMode(i))
outerframe = Frame(root)
outerframe.pack()

canvas = Canvas(outerframe, width=width, height=height)
canvas.bind("<B1-Motion>", click)
canvas.bind("<ButtonRelease-1>", release)
canvas.pack()

generateSplines()
clearCanvas()
root.mainloop()
