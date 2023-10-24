from tkinter import *
from GameOfLife import GameOfLife
import copy

canvasWidth = 800
windowHeight = 800
canvasHeight = windowHeight - 100
simulationInput = [[False for i in range(3)] for j in range(3)]
running = False
mintickrate = 100
tickrate = mintickrate
maxtickrate = 2000
largegrid = False
lowermaxscale = 30
highermaxscale = 100
wrapping = False
drawlines = True
game = GameOfLife(simulationInput, wrapping)


def startSimulation():
    global running

    if not running:
        resetGame()
        disableControls()
        running = True
        playSimulation()


def playSimulation():
    if running:
        stepSimulation()
        root.after(tickrate, playSimulation)


def pauseSimulation():
    global running

    running = False
    enableControls()


def advanceOneStep():
    if not running:
        resetGame()
        stepSimulation()


def stepSimulation():
    global simulationInput
    global game

    game.updateState()
    simulationInput = copy.deepcopy(game.state)
    resetCanvas()
    drawState(simulationInput)


def click(event):
    global simulationInput

    if not running:
        wspace = canvasWidth / wscale.get()
        xstart = event.x // wspace * wspace
        hspace = canvasHeight / hscale.get()
        ystart = event.y // hspace * hspace
        x = int(event.x // wspace)
        y = int(event.y // hspace)
        simulationInput[y][x] = not simulationInput[y][x]

        if simulationInput[y][x]:
            canvas.create_rectangle(xstart, ystart, xstart + wspace, ystart + hspace, fill="black")

        else:
            resetCanvas()
            drawState(simulationInput)


def drawWalls():
    canvas.create_rectangle(2, 2, canvasWidth, canvasHeight, width=1)


def drawVerticalLines():
    space = canvasWidth / wscale.get()
    for i in range(wscale.get()):
        canvas.create_line(i * space, 0, i * space, canvasHeight, width=1)


def drawHorizontalLines():
    space = canvasHeight / hscale.get()
    for i in range(hscale.get()):
        canvas.create_line(0, i * space, canvasWidth, i * space, width=1)


def drawState(state):
    for r in range(hscale.get()):
        for c in range(wscale.get()):
            wspace = canvasWidth / wscale.get()
            hspace = canvasHeight / hscale.get()
            if state[r][c]:
                canvas.create_rectangle(wspace * c, hspace * r, wspace * c + wspace, hspace * r + hspace, fill="black")


def wrappingChange():
    global wrapping

    wrapping = not wrapping
    resetGame()


def drawlinesChange():
    global drawlines

    drawlines = not drawlines
    resetCanvas()
    drawState(simulationInput)


def largegridChange():
    global largegrid
    global maxscale

    scale = 0
    largegrid = not largegrid
    if largegrid:
        scale = highermaxscale

    else:
        if wscale.get() > lowermaxscale:
            wscale.set(lowermaxscale)

        if hscale.get() > lowermaxscale:
            hscale.set(lowermaxscale)

        scale = lowermaxscale

    wscale.configure(to=scale)
    hscale.configure(to=scale)


def tickrateChange(event):
    global tickrate

    tickrate = tickratescale.get()


def rescale(event):
    clearCanvas()


def clearCanvas():
    if running:
        pauseSimulation()

    resetInput()
    resetCanvas()
    resetGame()


def resetCanvas():
    canvas.delete(ALL)
    if drawlines:
        drawHorizontalLines()
        drawVerticalLines()

    drawWalls()


def resetInput():
    global simulationInput

    simulationInput = [[False for i in range(wscale.get())] for j in range(hscale.get())]


def resetGame():
    global game

    game = GameOfLife(simulationInput, wrapping)


def disableControls():
    disableFrame(simulationControls)
    disableFrame(simulationVariables)
    disableFrame(simulationSettings)


def enableControls():
    enableFrame(simulationControls)
    enableFrame(simulationVariables)
    enableFrame(simulationSettings)


def disableFrame(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if child is pausebtn:
            pass
        elif wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="disable")
        else:
            disableFrame(child)


def enableFrame(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if child is pausebtn:
            pass
        elif wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="normal")
        elif child is pausebtn:
            pass
        else:
            enableFrame(child)


root = Tk()
outerframe = Frame(root)
outerframe.pack()

canvasframe = Frame(outerframe, height=canvasHeight)
canvasframe.pack(side=TOP)

canvas = Canvas(canvasframe, width=canvasWidth, height=canvasHeight)
canvas.bind("<Button-1>", click)
canvas.pack()

controlpanel = Frame(outerframe, height=windowHeight - canvasHeight, width=canvasWidth)
controlpanel.pack(side=BOTTOM)

simulationControls = Frame(controlpanel, borderwidth=2, relief="ridge")
simulationControls.pack(side=LEFT)

simulationVariables = Frame(controlpanel, borderwidth=2, relief="ridge")
simulationVariables.pack(side=RIGHT)

simulationSettings = Frame(controlpanel, borderwidth=2, relief="ridge")
simulationSettings.pack(side=RIGHT)

wscalelabel = Label(simulationVariables, text="Columns")
wscalelabel.pack(side=LEFT)

wscale = Scale(simulationVariables, from_=3, to=lowermaxscale, command=rescale)
wscale.pack(side=LEFT)

hscalelabel = Label(simulationVariables, text="Rows")
hscalelabel.pack(side=LEFT)

hscale = Scale(simulationVariables, from_=3, to=lowermaxscale, command=rescale)
hscale.pack(side=LEFT)

tickratescalelabel = Label(simulationVariables, text="Tickrate")
tickratescalelabel.pack(side=LEFT)

tickratescale = Scale(simulationVariables, from_=mintickrate, to=maxtickrate, command=tickrateChange)
tickratescale.pack(side=LEFT)

resetbtn = Button(simulationControls, text="Reset", bd="5", command=clearCanvas)
resetbtn.pack(side=LEFT)

startbtn = Button(simulationControls, text="Play", bd="5", command=startSimulation)
startbtn.pack(side=LEFT)

pausebtn = Button(simulationControls, text="Pause", bd="5", command=pauseSimulation)
pausebtn.pack(side=LEFT)

stepbtn = Button(simulationControls, text="Step", bd="5", command=advanceOneStep)
stepbtn.pack(side=LEFT)

wrappingchkbox = Checkbutton(simulationSettings, text="Wrap Around", command=wrappingChange)
wrappingchkbox.pack(side=TOP)

drawlineschkbox = Checkbutton(simulationSettings, text="Draw Grid", command=drawlinesChange)
drawlineschkbox.pack(side=TOP)
drawlineschkbox.select()

largegridchkbox = Checkbutton(simulationSettings, text="Large Grid", command=largegridChange)
largegridchkbox.pack(side=TOP)

resetCanvas()
root.mainloop()
