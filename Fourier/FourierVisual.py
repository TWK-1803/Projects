import pygame
from math import pi, e, sqrt
from svgpathtools import svg2paths

file = svg2paths("./8thNote.svg")
paths = file[0][0]
width, height = 1000, 800
size = (width, height)
black = (20, 20, 20)
white = (247, 247, 247)
gray = (100, 100, 100)
green = (20, 247, 20)
circles = []
points = []
origin = [width//2, height//2]
lengths = []
t = 0
svgVisible = True
pointsVisible = True
circlesVisible = True

NUM_SAMPLES = 1000
NUM_CIRCLES = 4
COMPLEX_SCALE = 6
CIRCLE_COLOR = white
SVG_COLOR = gray
POINT_COLOR = green
j = complex(0, 1)

#pygame configurations
pygame.init()
pygame.display.set_caption("Fourier Drawing with {} Cirles".format(NUM_CIRCLES*2))
screen = pygame.display.set_mode(size)
pointSurface = pygame.Surface(size)
circleSurface = pygame.Surface(size)
svgSurface = pygame.Surface(size)
pointSurface.set_colorkey(black)
circleSurface.set_colorkey(black)
svgSurface.set_colorkey(black)


def reset():
    global points
    global circles
    global t
    global lengths
    global loopFinished

    pygame.display.set_caption("Fourier Drawing with {} Cirles".format(NUM_CIRCLES*2))
    pointSurface.fill(black)
    circleSurface.fill(black)
    svgSurface.fill(black)
    screen.fill(black)
    origin = [width//2, height//2]
    circles = []
    points = []
    lengths = []
    loopFinished = False
    t = 0
    l = 0
    step = 1/NUM_SAMPLES
    realsum = 0
    imagsum = 0
    while l < 1:
        p = paths.point(l)
        realsum += p.real
        imagsum += p.imag
        point = complex(p.real*COMPLEX_SCALE+origin[0], p.imag*COMPLEX_SCALE+origin[1])
        points.append(point)
        l += step
    centeroffset = [realsum/NUM_SAMPLES*COMPLEX_SCALE, imagsum/NUM_SAMPLES*COMPLEX_SCALE]
    points = [complex(x.real-centeroffset[0], x.imag-centeroffset[1]) for x in points]

    for n in range(-NUM_CIRCLES, NUM_CIRCLES+1):
        cn = calculate_cn(n)
        circles.append(cn)
        lengths.append(0 if n == 0 else sqrt(cn.real**2 + cn.imag**2))

    for point in points:
        pygame.draw.circle(svgSurface, SVG_COLOR, (point.real, point.imag), 1)

def calculate_cn(n):
    interval = 1/NUM_SAMPLES
    sum = 0.0
    for i in range(NUM_SAMPLES):
        exp = e**(-n*2*pi*j*(i*interval))
        sum += points[i] * exp * interval
    return sum

reset()
run = True
loopFinished = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            NUM_CIRCLES += 1
            reset()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_o and NUM_CIRCLES > 0:
            NUM_CIRCLES -= 1
            reset()
        if not loopFinished and event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            svgVisible = not svgVisible
        if not loopFinished and event.type == pygame.KEYDOWN and event.key == pygame.K_w and NUM_CIRCLES > 0:
            pointsVisible = not pointsVisible
        if not loopFinished and event.type == pygame.KEYDOWN and event.key == pygame.K_e and NUM_CIRCLES > 0:
            circlesVisible = not circlesVisible

    sum = 0
    if t < 1:
        circleSurface.fill(black)
        endpoint = complex(circles[NUM_CIRCLES].real, circles[NUM_CIRCLES].imag)
        sum += endpoint
        pygame.draw.line(circleSurface, CIRCLE_COLOR, (origin[0], origin[1]), (endpoint.real, endpoint.imag))
        for i in range(1, NUM_CIRCLES+1):
            sum += circles[NUM_CIRCLES+i]*e**(i*2*pi*j*t) + circles[NUM_CIRCLES-i]*e**(-i*2*pi*j*t)
            temp = complex(endpoint + circles[NUM_CIRCLES+i]*e**(i*2*pi*j*t))
            pygame.draw.line(circleSurface, CIRCLE_COLOR, (endpoint.real, endpoint.imag), (temp.real, temp.imag))
            pygame.draw.circle(circleSurface, CIRCLE_COLOR, (endpoint.real, endpoint.imag), lengths[NUM_CIRCLES+i], 1)
            endpoint = complex(temp + circles[NUM_CIRCLES-i]*e**(-i*2*pi*j*t))
            pygame.draw.line(circleSurface, CIRCLE_COLOR, (temp.real, temp.imag), (endpoint.real, endpoint.imag))
            pygame.draw.circle(circleSurface, CIRCLE_COLOR, (temp.real, temp.imag), lengths[NUM_CIRCLES-i], 1)

        
        t += 0.0002
        screen.fill(black)
        pygame.draw.circle(pointSurface, POINT_COLOR, (sum.real, sum.imag), 1)
        if svgVisible:
            screen.blit(svgSurface, (0,0))
        if pointsVisible:
            screen.blit(pointSurface, (0, 0))
        if circlesVisible:
            screen.blit(circleSurface, (0, 0))
    else:
        # t = 0
        loopFinished = True

    pygame.display.update()
    
pygame.quit()