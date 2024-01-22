import pygame
from Config import *
from math import sin

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("{} Attractor from the {} perspective".format(ATTRACTORMODE, AXISMODE))

isRunning = True

previousPoints = []
for point in INITIALPOINTS:
    previousPoints.append(point)

def toScreenCoords(p):
    match AXISMODE:
        case "XY": return xy_screen_coords(p)
        case "XZ": return xz_screen_coords(p)
        case "YX": return yx_screen_coords(p)
        case "YZ": return yz_screen_coords(p)
        case "ZX": return zx_screen_coords(p)
        case "ZY": return zy_screen_coords(p)

def attractor(p):
    match ATTRACTORMODE:
        case "LORENZ": return lorenz(p)
        case "THOMAS": return thomas(p)
        case "AIZAWA": return aizawa(p)
        case "DADRAS": return dadras(p)
        case "CHEN": return chen(p)
        case "ROSSLER": return rossler(p)
        case "HALVORSON": return halvorson(p)
        case "RAB_FAB": return rab_fab(p)
        case "TSUCS": return tsucs(p)
        case "FOURWINGS": return fourwings(p)


# All the formulas and their starting conditions were taken from https://www.dynamicmath.xyz/strange-attractors/
# The min and max as well as the DT values are taken from what I thought looked best for each
# dx, dy, and dz, are the technically derivatives of those axies with respect to time
def lorenz(p, a=10, b=28, c=2.667):
    dx = a * (p[1] - p[0])                                                  # a(y-x)
    dy = b * p[0] - p[1] - p[0] * p[2]                                      # bx-y-xz
    dz = p[0] * p[1] - c * p[2]                                             # xy-cz
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def thomas(p, b=0.208186):
    dx = sin(p[1]) - b*p[0]                                                 # sin(y)-bx
    dy = sin(p[2]) - b*p[1]                                                 # sin(z)-by
    dz = sin(p[0]) - b*p[2]                                                 # sin(x)-bz
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def aizawa(p, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
    dx = (p[2]-b)*p[0]-d*p[1]                                               # (z-b)x-dy
    dy = d*p[0]+(p[2]-b)*p[1]                                               # dx+(z-b)y
    dz = c+a*p[2]-p[2]**3/3-(p[0]**2+p[1]**2)*(1+e*p[2])+f*p[2]*(p[0]**3)   # c+az-(z^3)/3-(x^2+y^2)(1+ez)+fz(x^3)
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def dadras(p, a=3, b=2.7, c=1.7, d=2, e=9):
    dx = p[1]-a*p[0]+b*p[1]*p[2]                                            # y-ax+byz
    dy = c*p[1]-p[0]*p[2]+p[2]                                              # cy-xz+z
    dz = d*p[0]*p[1]-e*p[2]                                                 # dxy-ez
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def chen(p, a=5.0, b=-10.0, c=-0.38):
    dx = a*p[0]-p[1]*p[2]                                                   # ax-yz
    dy = b*p[1]+p[0]*p[2]                                                   # by+xz
    dz = c*p[2]+p[0]*p[1]/3                                                 # cz+xy/3
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def rossler(p, a=0.2, b=0.2, c=5.7):
    dx = -(p[1]+p[2])                                                       # -(y+z)
    dy = p[0]+a*p[1]                                                        # x+ay
    dz = b+p[2]*(p[0]-c)                                                    # b+z(x-c)
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def halvorson(p, a=1.89):
    dx = -a*p[0]-4*p[1]-4*p[2]-p[1]**2                                      # ax-4y-4z-y^2
    dy = -a*p[1]-4*p[2]-4*p[0]-p[2]**2                                      # ay-4z-4x-z^2
    dz = -a*p[2]-4*p[0]-4*p[1]-p[0]**2                                      # az-4x-4y-x^2
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

# RABINOVICH-FABRIKANT
def rab_fab(p, a=0.14, b=0.10):
    dx = p[1]*(p[2]-1+p[0]**2)+b*p[0]                                       # y(z-1+x^2)+bx
    dy = p[0]*(3*p[2]+1-p[0]**2)+b*p[1]                                     # x(3z+1-x^2)+by
    dz = -2*p[2]*(a+p[0]*p[1])                                              # -2z(a+xy)

    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

# THREE-SCROLL UNIFIED CHAOTIC SYSTEM
def tsucs(p, a=32.48, b=45.84, c=1.18, d=0.13, e=0.57, f=14.7):
    dx = a*(p[1]-p[0])+d*p[0]*p[2]                                          # a(y-x)+dxz
    dy = b*p[0]-p[0]*p[2]+f*p[1]                                            # bx-xz+fy
    dz = c*p[2]+p[0]*p[1]-e*p[0]**2                                         # cz+xy-ex^2

    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

def fourwings(p, a=0.2, b=0.01, c=-0.4):
    dx = a*p[0]+p[1]*p[2]                                                   # ax+yz
    dy = b*p[0]+c*p[1]-p[0]*p[2]                                            # bx+cy-xz
    dz = -p[2]-p[0]*p[1]                                                    # -z-xy
    
    return [p[0]+dx*DT, p[1]+dy*DT, p[2]+dz*DT]

# The first named axis is displayed on the screen as the x axis and the second the y axis
def xy_screen_coords(p):
    screenx = WIDTH * ((p[0] - XMIN) / (XMAX - XMIN))
    screeny = HEIGHT * ((p[1] - YMIN) / (YMAX - YMIN))
    return [round(screenx), round(screeny)]


def yx_screen_coords(p):
    screenx = HEIGHT * ((p[0] - XMIN) / (XMAX - XMIN))
    screeny = WIDTH * ((p[1] - YMIN) / (YMAX - YMIN))

    return [round(screeny), round(screenx)]

def yz_screen_coords(p):
    screenz = WIDTH * ((p[2] - ZMIN) / (ZMAX - ZMIN))
    screeny = HEIGHT * ((p[1] - YMIN) / (YMAX - YMIN))

    return [round(screenz), round(screeny)]

def zy_screen_coords(p):
    screenz = HEIGHT * ((p[2] - ZMIN) / (ZMAX - ZMIN))
    screeny = WIDTH * ((p[1] - YMIN) / (YMAX - YMIN))

    return [round(screeny), round(screenz)]

def xz_screen_coords(p):
    screenx = WIDTH * ((p[0] - XMIN) / (XMAX - XMIN))
    screenz = HEIGHT * ((p[2] - ZMIN) / (ZMAX - ZMIN))

    return [round(screenx), round(screenz)]

def zx_screen_coords(p):
    screenx = HEIGHT * ((p[0] - XMIN) / (XMAX - XMIN))
    screenz = WIDTH * ((p[2] - ZMIN) / (ZMAX - ZMIN))

    return [round(screenz), round(screenx)]


# Same process, but only displays the final image
if not INTERACTIVE:
    for i in range(1000000):
        for j in range(len(INITIALPOINTS)):
            if DRAWMODE == "LINES":
                next = attractor(previousPoints[j])
                pygame.draw.line(screen, COLORS[j], toScreenCoords(previousPoints[j]), toScreenCoords(next), 1)
                previousPoints[j] = next
            elif DRAWMODE == "POINTS":
                next = attractor(previousPoints[j])
                pygame.draw.circle(screen, COLORS[j], toScreenCoords(next), 1)
                previousPoints[j] = next
    pygame.display.flip()

# Main loop
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    if INTERACTIVE:
        for j in range(len(INITIALPOINTS)):
            if DRAWMODE == "LINES":
                next = attractor(previousPoints[j])
                pygame.draw.line(screen, COLORS[j], toScreenCoords(previousPoints[j]), toScreenCoords(next), 1)
                previousPoints[j] = next
            elif DRAWMODE == "POINTS":
                next = attractor(previousPoints[j])
                pygame.draw.circle(screen, COLORS[j], toScreenCoords(next), 1)
                previousPoints[j] = next
        pygame.display.flip()