from tkinter import *
from Circle import Circle
from Square import Square

from Config import *

shapes = [
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Circle(),
            Square()
        ]

# X_i = A_i + (B_i - A_i)((1-f(A))/(f(B)-f(A)))
def interpolate(r1, c1, r2, c2, mode):
    if mode == "x":
        ai = c1*gridsize
        bi = c2*gridsize
    else:
        ai = r1*gridsize
        bi = r2*gridsize
    xi = ai+(bi-ai)*((threshold-gridvalues[r1][c1])/(gridvalues[r2][c2]-gridvalues[r1][c1]))
    return xi
    
def getValues():
    global gridvalues

    for r in range(gridHeight):
        for c in range(gridWidth):
            sum = 0
            for shape in shapes:
                implicit = shape.calculateImplicitFunction(c*gridsize, r*gridsize)
                sum += implicit
            gridvalues[r][c] = sum

def marchSquares():
    getValues()
    for r in range(len(gridvalues)-1):
        for c in range(len(gridvalues[0])-1):
            bits = 0
            bits += 8 if gridvalues[r][c] >= threshold else 0
            bits += 4 if gridvalues[r][c+1] >= threshold else 0
            bits += 2 if gridvalues[r+1][c+1] >= threshold else 0
            bits += 1 if gridvalues[r+1][c] >= threshold else 0
            if 0 < bits < 15 :
                edges = arrangements[bits]
                for edge in edges:
                    start = []
                    end = []
                    match(edge[0]):
                        case 0: start = [interpolate(r, c, r, c+1, "x"), r*gridsize]
                        case 1: start = [c*gridsize+gridsize, interpolate(r, c+1, r+1, c+1, "y")]
                        case 2: start = [interpolate(r+1, c+1, r+1, c, "x"), r*gridsize+gridsize]
                    match(edge[1]):
                        case 1: end = [c*gridsize+gridsize, interpolate(r, c+1, r+1, c+1, "y")]
                        case 2: end = [interpolate(r+1, c+1, r+1, c, "x"), r*gridsize+gridsize]
                        case 3: end = [c*gridsize,interpolate(r+1, c, r, c, "y")]
                    canvas.create_line(start[0], start[1], end[0], end[1])

def updateShapes():
    for shape in shapes:
        shape.update()

def spacePressed(event):
    global isRunning

    isRunning = not isRunning

def resetCanvas():
    if isRunning:
        canvas.delete(ALL)
        marchSquares()
        updateShapes()
    
    root.after(tickrate, resetCanvas)

root = Tk()
outerframe = Frame(root)
root.bind("<space>", spacePressed)
outerframe.pack()

canvas = Canvas(outerframe, width=canvasWidth, height=canvasHeight)
canvas.pack()

resetCanvas()
root.mainloop()
