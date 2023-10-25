from tkinter import *
from BezierCurve import BezierCurve
from BezierSpline import BezierSpline
from HermiteSpline import HermiteSpline
from LinearSpline import LinearSpline
from CardinalSpline import CardinalSpline
from CatmullRomSpline import CatmullRomSpline

windowWidth = 800
windowHeight = 700
controlWidth = windowWidth
controlHeight = 100
canvasWidth = windowWidth
canvasHeight = windowHeight - controlHeight
basePointCloud = [[-200, 0], [-100, 100], [100, 100], [200, 0]]
splines = []
selectedPoint = -1
drawLines = True
addingPoint = False
removingPoint = False
numberOfTSteps = 50
mode = 0
splineWidth = 1


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

    clearCanvas()


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
    t = 0
    previousPoint = []
    maxt = 1 if mode == 0 else len(basePointCloud) - 1
    while t < maxt:
        splines[mode].endPoint = splines[mode].getEndPoint(t)
        scoords = getWindowCoords(splines[mode].endPoint)
        if previousPoint != []:
            drawPoint(previousPoint, scoords)

        t += 1 / numberOfTSteps
        previousPoint = scoords

    drawPoint(previousPoint, getWindowCoords(splines[mode].getEndPoint(maxt-0.000001)))

def drawPoint(point1, point2):
    canvas.create_line(point1[0], point1[1], point2[0], point2[1], width=splineWidth, fill="black")


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


def getWindowCoords(coords):
    return [coords[0] + canvasWidth / 2, -coords[1] + canvasHeight / 2]


def getCartesianCoords(coords):
    return [coords[0] - canvasWidth / 2, -(coords[1] - canvasHeight / 2)]


def click(event):
    global selectedPoint
    global addingPoint
    global removingPoint

    if drawLines and not addingPoint and not removingPoint:
        if selectedPoint == -1:
            for i in range(len(splines[mode].pointCloud)):
                pcoords = getWindowCoords(splines[mode].pointCloud[i])
                if (pcoords[0] - 5 < event.x < pcoords[0] + 5 and pcoords[1] - 5 < event.y < pcoords[1] + 5):
                    selectedPoint = i
                    break

        if selectedPoint != -1:
            if event.x >= canvasWidth:
                x = canvasWidth

            elif event.x <= 0:
                x = 0

            else:
                x = event.x

            if event.y >= canvasHeight:
                y = canvasHeight

            elif event.y <= 0:
                y = 0

            else:
                y = event.y

            splines[mode].setPoint(selectedPoint, getCartesianCoords([x, y]))
            clearCanvas()


def release(event):
    global selectedPoint
    global addingPoint
    global removingPoint
    global basePointCloud
    
    if addingPoint:
        if (0 <= event.x <= canvasWidth) and (0 <= event.y <= canvasHeight):
            basePointCloud.append(getCartesianCoords([event.x, event.y]))
            addingPoint = False
            enableFrame(controlPanel)
            generateSplines()
    
    elif removingPoint:
        tmp = splines[mode].getMainPointCloud()
        for i in range(len(tmp)):
            pcoords = getWindowCoords(tmp[i])
            if (pcoords[0] - 5 < event.x < pcoords[0] + 5 and pcoords[1] - 5 < event.y < pcoords[1] + 5):
                index = i
                break
        basePointCloud.pop(index)
        removingPoint = False
        enableFrame(controlPanel)
        generateSplines()

    selectedPoint = -1


def clearCanvas():
    canvas.delete(ALL)
    drawPointCloud()
    drawSpline()


def addPoint():
    global addingPoint

    disableFrame(controlPanel)
    addingPoint = True


def removePoint():
    global removingPoint

    if len(splines[mode].getMainPointCloud()) > 2:
        disableFrame(controlPanel)
        removingPoint = True


def optionChanged(selection):
    global mode
    global basePointCloud

    basePointCloud = splines[mode].getMainPointCloud()
    match (selection):
        case "Bezier Curve": mode = 0
        case "Bezier Spline": mode = 1
        case "Hermite Spline": mode = 2
        case "Linear Spline": mode = 3
        case "Cardinal Spline": mode = 4
        case "Catmull-Rom Spline": mode = 5
    
    generateSplines()


def drawLinesChange():
    global drawLines

    drawLines = not drawLines
    clearCanvas()


def splineWidthChange(event):
    global splineWidth

    splineWidth = splineWidthScale.get()
    clearCanvas()


def numberOfTStepsChange(event):
    global numberOfTSteps

    numberOfTSteps = numberOfTStepsScale.get()
    clearCanvas()


def disableFrame(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="disable")
        else:
            disableFrame(child)


def enableFrame(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="normal")
        else:
            enableFrame(child)


root = Tk()
outerframe = Frame(root, width=windowWidth, height=windowHeight)
outerframe.pack()

canvas = Canvas(outerframe, width=canvasWidth, height=canvasHeight)
canvas.bind("<B1-Motion>", click)
canvas.bind("<ButtonRelease-1>", release)
canvas.pack(side=TOP)

controlPanel = Frame(outerframe, width=controlWidth, height=controlHeight)
controlPanel.pack(side=BOTTOM)

pointControlFrame = Frame(controlPanel, borderwidth=2, relief=RIDGE)
pointControlFrame.pack(side=LEFT)

pointControlFrameLabel = Label(pointControlFrame, text="Point Controls", font='Ariel 9 bold underline')
pointControlFrameLabel.pack()

addPointButton = Button(pointControlFrame, text="Add Point", command=addPoint)
addPointButton.pack(side=TOP)

removePointButton = Button(pointControlFrame, text="Remove Point", command=removePoint)
removePointButton.pack(side=TOP)

visualControlFrame = Frame(controlPanel, borderwidth=2, relief=RIDGE)
visualControlFrame.pack(side=LEFT)

visualControlFrameLabel = Label(visualControlFrame, text="Visual Controls", font='Ariel 9 bold underline')
visualControlFrameLabel.pack()

splineSelection = StringVar(outerframe) 
splineSelection.set("Bezier Curve")
splineSelectionSelector = OptionMenu(visualControlFrame,
                                     splineSelection,
                                     *['Bezier Curve',
                                       'Bezier Spline',
                                       'Hermite Spline',
                                       'Linear Spline',
                                       'Cardinal Spline',
                                       'Catmull-Rom Spline'],
                                     command=optionChanged
                                    )
splineSelectionSelector.pack(side=TOP)

drawlineschkbox = Checkbutton(visualControlFrame, text="Draw Points", command=drawLinesChange)
drawlineschkbox.pack(side=TOP)
drawlineschkbox.select()

splineControlFrame = Frame(controlPanel, borderwidth=2, relief=RIDGE, height=controlHeight)
splineControlFrame.pack(side=LEFT)

splineControlFrameLabel = Label(splineControlFrame, text="Spline Controls", font='Ariel 9 bold underline')
splineControlFrameLabel.pack()

splineWidthScale = Scale(splineControlFrame, orient=VERTICAL, from_= 1, to=5, command=splineWidthChange)
splineWidthScale.pack(side=LEFT)

splineWidthScaleLabel = Label(splineControlFrame, text="Spline Width")
splineWidthScaleLabel.pack(side=LEFT)

numberOfTStepsScale = Scale(splineControlFrame, orient=VERTICAL, from_= 3, to=50, command=numberOfTStepsChange)
numberOfTStepsScale.set(numberOfTSteps)
numberOfTStepsScale.pack(side=LEFT)

numberOfTStepsScaleLabel = Label(splineControlFrame, text="# of Iterations")
numberOfTStepsScaleLabel.pack(side=LEFT)

generateSplines()
clearCanvas()
root.mainloop()
