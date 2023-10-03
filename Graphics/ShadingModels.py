####################################################################################
# Tyler Kranz 102-63-704
# 2/15/2022
# Assignment 4, CSC 470
# This program uses wireframe graphics to display a number of geometric shapes.
# These shapes can be manipulated in the xyz space with translations, in-place
# roations, and in-place scaling. There are a variety of shading modes selectable
# including basic polygon filling, and flat, gouraud, annd phong shading.
####################################################################################

import math
import copy
from tkinter import *

# defining the constants of the frame and z distance of the "camera"
CanvasWidth = 400
CanvasHeight = 400
d = 500

# definition of the coordinate position of the "camera" and
# inititialization of the z-buffer array
MaxDistance = d
zBuffer =  [[MaxDistance for c in range(CanvasHeight)] for r in range(CanvasWidth)]

# The constants for shading
Ia = .3
Ip = .7
Kd = .75
Ks = .25
SpecIndex = 4
L = [1, 1, -1]
V = [0, 0, -d]

# global variables which point to the currently selected object and
# indicate the current drawing mode
selected = 0
mode = 1

# ***************************** Initialize Objects ***************************

# Definition of the pyramid's underlying points
apex = [0, 50, 100]
base1 = [50, -50, 50]
base2 = [50, -50, 150]
base3 = [-50, -50, 150]
base4 = [-50, -50, 50]

# Definition of cube1's underlying points
topfrontleft1 = [-150, 100, 50]
topfrontright1 = [-100, 100, 50]
topbackleft1 = [-150, 100, 100]
topbackright1 = [-100, 100, 100]
bottomfrontleft1 = [-150, 50, 50]
bottomfrontright1 = [-100, 50, 50]
bottombackleft1 = [-150, 50, 100]
bottombackright1 = [-100, 50, 100]

# Definition of cube2's underlying points
topfrontleft2 = [100, 100, 50]
topfrontright2 = [150, 100, 50]
topbackleft2 = [100, 100, 100]
topbackright2 = [150, 100, 100]
bottomfrontleft2 = [100, 50, 50]
bottomfrontright2 = [150, 50, 50]
bottombackleft2 = [100, 50, 100]
bottombackright2 = [150, 50, 100]

# Definition of the cylinder's 16 underlying points
front1 = [-50, 120.7107, 50]
front2 = [50, 120.7107, 50]
front3 = [120.7107, 50, 50]
front4 = [120.7107, -50, 50]
front5 = [50, -120.7107, 50]
front6 = [-50, -120.7107, 50]
front7 = [-120.7107, -50, 50]
front8 = [-120.7107, 50, 50]
back1 = [-50, 120.7107, 450]
back2 = [50, 120.7107, 450]
back3 = [120.7107, 50, 450]
back4 = [120.7107, -50, 450]
back5 = [50, -120.7107, 450]
back6 = [-50, -120.7107, 450]
back7 = [-120.7107, -50, 450]
back8 = [-120.7107, 50, 450]


# Definition of all polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside

# Pyramid polygons
pfrontpoly = [apex, base1, base4]
prightpoly = [apex, base2, base1]
pbackpoly = [apex, base3, base2]
pleftpoly = [apex, base4, base3]
pbottompoly = [base1, base2, base3, base4]

# Cube 1 polygons
ctoppoly1 = [topfrontleft1, topbackleft1, topbackright1, topfrontright1]
cleftpoly1 = [topfrontleft1, bottomfrontleft1, bottombackleft1, topbackleft1]
cbackpoly1 = [topbackright1, topbackleft1, bottombackleft1, bottombackright1]
crightpoly1 = [topfrontright1, topbackright1, bottombackright1, bottomfrontright1]
cfrontpoly1 = [topfrontleft1, topfrontright1, bottomfrontright1, bottomfrontleft1]
cbottompoly1 = [bottomfrontleft1, bottomfrontright1, bottombackright1, bottombackleft1]

# Cube 2 polygons
ctoppoly2 = [topfrontleft2, topbackleft2, topbackright2, topfrontright2]
cleftpoly2 = [topfrontleft2, bottomfrontleft2, bottombackleft2, topbackleft2]
cbackpoly2 = [topbackright2, topbackleft2, bottombackleft2, bottombackright2]
crightpoly2 = [topfrontright2, topbackright2, bottombackright2, bottomfrontright2]
cfrontpoly2 = [topfrontleft2, topfrontright2, bottomfrontright2, bottomfrontleft2]
cbottompoly2 = [bottomfrontleft2, bottomfrontright2, bottombackright2, bottombackleft2]

# Cylinder's polygons
northpoly = [front1, back1, back2, front2]
northeastpoly = [front2, back2, back3, front3]
eastpoly = [front3, back3, back4, front4]
southeastpoly = [front4, back4, back5, front5]
southpoly = [front5, back5, back6, front6]
southwestpoly = [front6, back6, back7, front7]
westpoly = [front7, back7, back8, front8]
northwestpoly = [front8, back8, back1, front1]
frontpoly = [front1, front2, front3, front4, front5, front6, front7, front8]
backpoly = [back1, back8, back7, back6, back5, back4, back3, back2]

# Definition of all objects and coloring of each polygon
Pyramid = [pbottompoly, pfrontpoly, prightpoly, pbackpoly, pleftpoly]
PyramidColor = ["black", "red", "green", "blue", "yellow"]
Cube1 = [ctoppoly1, cleftpoly1, cbackpoly1, crightpoly1, cfrontpoly1, cbottompoly1]
Cube1Color = ["white", "black", "red", "green", "blue", "yellow"]
Cube2 = [ctoppoly2, cleftpoly2, cbackpoly2, crightpoly2, cfrontpoly2, cbottompoly2]
Cube2Color = ["white", "black", "red", "green", "blue", "yellow"]
Cylinder = [northpoly, northeastpoly, eastpoly, southeastpoly, southpoly,
            southwestpoly, westpoly, northwestpoly, frontpoly, backpoly]
CylinderColor = ["black", "red", "green", "blue", "yellow", "white", "gray",
                 "orange", "purple", "cyan"]
# Definition of all object's underlying point cloud.  No structure,  just the points.
PyramidPointCloud = [apex, base1, base2, base3, base4]
DefaultPyramidPointCloud = copy.deepcopy(PyramidPointCloud)

Cube1PointCloud = [topfrontleft1, topfrontright1, topbackleft1, topbackright1, bottomfrontleft1, bottomfrontright1, bottombackleft1, bottombackright1]
DefaultCube1PointCloud = copy.deepcopy(Cube1PointCloud)

Cube2PointCloud = [topfrontleft2, topfrontright2, topbackleft2, topbackright2, bottomfrontleft2, bottomfrontright2, bottombackleft2, bottombackright2]
DefaultCube2PointCloud = copy.deepcopy(Cube2PointCloud)

CylinderPointCloud = [front1, front2, front3, front4, front5, front6, front7, front8,
                      back1, back2, back3, back4, back5, back6, back7, back8]

DefaultCylinderPointCloud = copy.deepcopy(CylinderPointCloud)

# List of all relevant object data in the scene
SceneData = [Cylinder, CylinderPointCloud, DefaultCylinderPointCloud, CylinderColor]
#[Cube1, Cube1PointCloud, DefaultCube1PointCloud, Cube1Color,
# Pyramid, PyramidPointCloud, DefaultPyramidPointCloud, PyramidColor,
# Cube2, Cube2PointCloud, DefaultCube2PointCloud, Cube2Color]
             
#*************************Helper/Calculation Functions*************************************************

# Calculate the reflection vector given a surface normal and a lighting vector
def reflect(N, L):
    R = []
    N = normalize(N)
    L = normalize(L)
    twoCosPhi = 2 * (N[0]*L[0] + N[1]*L[1] + N[2]*L[2])
    if twoCosPhi > 0:
        for i in range(3):
            R.append(N[i] - (L[i] / twoCosPhi))
    elif twoCosPhi == 0:
        for i in range(3):
            R.append(-L[i])
    else:
        for i in range(3):
            R.append(-N[i] + (L[i] / twoCosPhi))
    return normalize(R)

# Generate the RBG hex code for a given intensity
def triColorHexCode(ambient, diffuse, specular):
    combinedColorCode = colorHexCode(ambient + diffuse + specular)
    specularColorCode = colorHexCode(specular)
    colorString = "#" + specularColorCode + combinedColorCode + specularColorCode
    return colorString

# Generate the a single hex code for a given intensity
def colorHexCode(intensity):
    hexString = str(hex(round(255 * intensity)))
    if hexString[0] == "-":
        # print("Negative illumination intensity")
        trimmedHexString = "00"
    else:
        trimmedHexString = hexString[2:]
        if len(trimmedHexString) == 1: trimmedHexString = "0" + trimmedHexString
    return trimmedHexString

# calculates the intensity at the given parameters
# note it expects incoming vectors to be normalized already
def getIntensity(Ia, Ip, Kd, Ks, SpecIndex, N, L, V):
    ambient = Ia*Kd
    NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
    if NdotL < 0: NdotL = 0
    diffuse = Ip * Kd * NdotL
    R = reflect(N,L)
    RdotV = R[0]*V[0] + R[1]*V[1] + R[2]*V[2]
    if RdotV < 0: RdotV = 0
    specular = Ip * Ks * RdotV**SpecIndex
    return [ambient, diffuse, specular]
    
# return the normalized xyz values of a 3 dimensional vector
def normalize(vector):
    normalizedVector = [0]*3
    magnitude = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
    for i in range(3):
        normalizedVector[i] = vector[i]/magnitude
    return normalizedVector

def getNormal(poly):
    P = [0, 0, 0]
    Q = [0, 0, 0]
    N = [0, 0, 0]
    P0, P1, P2 = poly[0], poly[1], poly[2]
    for i in range(3):
        P[i] = P1[i]-P0[i]
        Q[i] = P2[i]-P0[i]
    N[0], N[1], N[2] = P[1]*Q[2]-P[2]*Q[1], P[2]*Q[0]-P[0]*Q[2], P[0]*Q[1]-P[1]*Q[0]
    return normalize(N)

# calculate the visibility score for a given polygon and return
# true if it is visible and false if it is not
def isVisible(poly):
    N = getNormal(poly)
    ABC = N[0]*V[0]+N[1]*V[1]+N[2]*V[2]
    D = N[0]*poly[0][0]+N[1]*poly[0][1]+N[2]*poly[0][2]
    
    return (ABC-D) > 0
    
# Calculates the "visual center" point in xyz space and returns it as an array
def getReference(current):
    xmax = current[0][0]
    xmin = current[0][0]
    ymax = current[0][1]
    ymin = current[0][1]
    zmax = current[0][2]
    zmin = current[0][2]
    for point in current:
        if point[0]>=xmax:
            xmax = point[0]
        if point[0]<=xmin:
            xmin = point[0]
        if point[1]>=ymax:
            ymax = point[1]
        if point[1]<=ymin:
            ymin = point[1]
        if point[2]>=zmax:
            zmax = point[2]
        if point[2]<=zmin:
            zmin = point[2]
        # print(str(xmax)+" "+str(xmin)+" "+str(ymax)+" "+str(ymin)+" "+str(zmax)+" "+str(zmin))
    # print("reference stub executed")
    return [((xmin+xmax)/2), ((ymin+ymax)/2), ((zmin+zmax)/2)]

# helper funtion to generate a list of the vertex normals
def getVertexNormals(prevpoly, poly, nextpoly):
    normal = getNormal(poly)
    # print(normal)
    prevNormal = getNormal(prevpoly)
    nextNormal = getNormal(nextpoly)
    vertexNormals = []
    # if the current vertex is closer to the previous poly, use that for the
    # vertex normal, and if it is closer to the next poly then use that for the
    # vertex normal. After, normalize the result and add to the result
    for vertex in poly:
        vertexNormal = [0, 0, 0]
        if vertex in prevpoly:
            for i in range(3):
                vertexNormal[i] = prevNormal[i] + normal[i]
        else:
            for i in range(3):
                vertexNormal[i] = nextNormal[i] + normal[i]
        vertexNormals.append(normalize(vertexNormal))
    # print(vertexNormals,end="\n\n")
    return vertexNormals
        
def generateEdgeTable(prevpoly, prevpoly2, poly, poly2, nextpoly, nextpoly2):
    global Ia
    global Ip
    global Kd
    global Ks
    global SpecIndex
    global L
    global V
    # create an empty list for the table, one for the
    # points aleady used as the start of an edge and create a
    # copy of the poly data to avoid changing the poly itself
    # after, find all the vertex normals for Gouraud and Phong shading
    edgeTable = []
    polyPoints = poly
    visited = []
    vertexNormals = getVertexNormals(prevpoly2, poly2, nextpoly2)
    
    # While there are two or more points to draw edges between
    while len(polyPoints) - len(visited) >= 2:
        Ymin = CanvasHeight
        # find the point in the poly that has the lowest Y not already picked 
        indx = 0
        for elem in polyPoints:
            if elem[1] < Ymin and elem not in visited:
                Ymin = elem[1]
                indx = polyPoints.index(elem)

        # get all relevant data for edge 1
        Xstart1 = polyPoints[indx][0]
        Xend1 = polyPoints[(indx+1)%len(polyPoints)][0]
        Ystart1 = polyPoints[indx][1]
        Yend1 = polyPoints[(indx+1)%len(polyPoints)][1]
        Zstart1 = polyPoints[indx][2]
        Zend1 = polyPoints[(indx+1)%len(polyPoints)][2]
        Istart1 = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, vertexNormals[indx], normalize(L), normalize(V))
        Iend1 = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, vertexNormals[(indx+1)%len(vertexNormals)], normalize(L), normalize(V))
        Nxstart1 = vertexNormals[indx][0]
        Nxend1 = vertexNormals[(indx+1)%len(vertexNormals)][0]
        Nystart1 = vertexNormals[indx][1]
        Nyend1 = vertexNormals[(indx+1)%len(vertexNormals)][1]
        Nzstart1 = vertexNormals[indx][2]
        Nzend1 = vertexNormals[(indx+1)%len(vertexNormals)][2]
        
        
        # get all relevant data for edge 2
        Xstart2 = polyPoints[indx][0]
        Xend2 = polyPoints[(indx-1)%len(polyPoints)][0]
        Ystart2 = polyPoints[indx][1]
        Yend2 = polyPoints[(indx-1)%len(polyPoints)][1]
        Zstart2 = polyPoints[indx][2]
        Zend2 = polyPoints[(indx-1)%len(polyPoints)][2]
        Istart2 = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, vertexNormals[indx], normalize(L), normalize(V))
        Iend2 = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, vertexNormals[(indx-1)%len(vertexNormals)], normalize(L), normalize(V))
        Nxstart2 = vertexNormals[indx][0]
        Nxend2 = vertexNormals[(indx-1)%len(vertexNormals)][0]
        Nystart2 = vertexNormals[indx][1]
        Nyend2 = vertexNormals[(indx-1)%len(vertexNormals)][1]
        Nzstart2 = vertexNormals[indx][2]
        Nzend2 = vertexNormals[(indx-1)%len(vertexNormals)][2]
        
        # check for division by 0 and horizontal edges and for edges already made
        if Ystart1 != Yend1 and polyPoints[(indx+1)%len(polyPoints)] not in visited:
            dZ1 = (Zend1-Zstart1)/(Yend1-Ystart1)
            dId1 = (Iend1[1]-Istart1[1])/(Yend1-Ystart1)
            dIs1 = (Iend1[2]-Istart1[2])/(Yend1-Ystart1)
            dNx1 = (Nxend1-Nxstart1)/(Yend1-Ystart1)
            dNy1 = (Nyend1-Nystart1)/(Yend1-Ystart1)
            dNz1 = (Nzend1-Nzstart1)/(Yend1-Ystart1)
            if Xend1 != Xstart1:
                dX1 = (Xend1-Xstart1)/(Yend1-Ystart1)
            else:
                dX1 = "undefined"
            edgeTable.append([polyPoints[indx],polyPoints[(indx+1)%len(polyPoints)],
                              Xstart1, Ystart1, Yend1, dX1, Zstart1, dZ1,
                              Istart1[1], dId1, Istart1[2], dIs1,
                              Nxstart1, dNx1, Nystart1, dNy1, Nzstart1, dNz1])
            
        # if there are only 2 points left, there doesnt need to be a duplicate edge
        if Ystart2 != Yend2 and len(polyPoints) - len(visited) >= 2 and polyPoints[(indx-1)%len(polyPoints)] not in visited:
            dZ2 = (Zend2-Zstart2)/(Yend2-Ystart2)
            dId2 = (Iend2[1]-Istart2[1])/(Yend2-Ystart2)
            dIs2 = (Iend2[2]-Istart2[2])/(Yend2-Ystart2)
            dNx2 = (Nxend2-Nxstart2)/(Yend2-Ystart2)
            dNy2 = (Nyend2-Nystart2)/(Yend2-Ystart2)
            dNz2 = (Nzend2-Nzstart2)/(Yend2-Ystart2)
            if Xend2 != Xstart2:
                dX2 = (Xend2-Xstart2)/(Yend2-Ystart2)
            else:
                dX2 = "undefined"
            edgeTable.append([polyPoints[indx], polyPoints[(indx-1)%len(polyPoints)],
                              Xstart2, Ystart2, Yend2, dX2, Zstart2, dZ2,
                              Istart2[1], dId2, Istart2[2], dIs2,
                              Nxstart2, dNx2, Nystart2, dNy2, Nzstart2, dNz2])
        
        visited.append(polyPoints[indx])
        # print(polyPoints)
    #print(edgeTable,end = "\n\n")
    return edgeTable

# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    # calculate the perspective projection for each axis of a point and add them to an array which is returned
    ps = []
    for coord in point:
        ps.append(d*int(coord)/(d+point[2]))
    return ps

# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    # calculate the 2D display coordinate for the X and Y axis and return both in an array
    displayXYZ = []
    displayXYZ.append(float(round((CanvasWidth/2)+point[0])))
    displayXYZ.append(float(round((CanvasHeight/2)-point[1])))
    displayXYZ.append(point[2])
    return displayXYZ

#*****************************Transformations**************************************************************

# This function resets the selected object to its original size and location in 3D space
def resetObject(current, default):
    for i in range(len(current)):
        for j in range(3):
            current[i][j] = default[i][j]

# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(current, displacement):
    # iterate through each point and update the XYZ values by adding the corresponding
    # value in the displacement vector
    for i in range (len(current)):
        for j in range (3):
            current[i][j] += displacement[j]
    # print("translate stub executed.")

    
# This function performs a simple uniform in-place scale of an object. The scalefactor is a scalar.
def scale(current, scalefactor):
    # Adjust each point according to the visual center, then iterate through each point
    # and multipy each by the scalefactor and readjust back using the reference point again
    refPoint = getReference(current)
    for i in range (len(current)):
        for j in range (3):
            current[i][j] -= refPoint[j]
        for j in range (3):
            current[i][j] *= scalefactor
        for j in range (3):
            current[i][j] += refPoint[j]
    # print("scale stub executed.")
    
# This function performs a free rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from -Z [the location of the Viewer in the standard postion]
def rotateZ(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range (len(current)):
        for j in range (3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0]*math.cos(dtor)-point[1]*math.sin(dtor))
        rotatedcoords.append(point[0]*math.sin(dtor)+point[1]*math.cos(dtor))
        rotatedcoords.append(point[2])
        point = copy.deepcopy(rotatedcoords)
        for i in range (3):
            current[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    for i in range (len(current)):
        for j in range (3):
            current[i][j] += refPoint[j]
    # print("rotateZ stub executed.")
 
# This function performs a free rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from +Y looking toward the origin.
def rotateY(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range (len(current)):
        for j in range (3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0]*math.cos(dtor)+point[2]*math.sin(dtor))
        rotatedcoords.append(point[1])
        rotatedcoords.append(point[2]*math.cos(dtor)-point[0]*math.sin(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range (3):
            current[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    for i in range (len(current)):
        for j in range (3):
            current[i][j] += refPoint[j]
    # print("rotateY stub executed.")

# This function performs a free rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', in-place. The rotation is CCW in a LHS when viewed from +X looking toward the origin.
def rotateX(current, degrees):
    # Adjust each point according to the visual center, then iterate through the points
    # in the cloud and caluculate the rotated positions for each. Only afterward, to avoid
    # pointer issues, does it change the values of the actual points in the cloud itself
    # using another method to avoid pointer issues. After, readjust back using the visual
    # center again
    refPoint = getReference(current)
    count = 0
    for i in range (len(current)):
        for j in range (3):
            current[i][j] -= refPoint[j]
    for point in current:
        # print(point)
        rotatedcoords = []
        dtor = degrees*(math.pi/180)
        rotatedcoords.append(point[0])
        rotatedcoords.append(point[1]*math.cos(dtor)-point[2]*math.sin(dtor))
        rotatedcoords.append(point[1]*math.sin(dtor)+point[2]*math.cos(dtor))
        point = copy.deepcopy(rotatedcoords)
        for i in range (3):
            current[count][i] = point[i]
        count+=1
        # print(PyramidPointCloud[i])
    for i in range (len(current)):
        for j in range (3):
            current[i][j] += refPoint[j]
    # print("rotateX stub executed.")

#**********************************Draw Scene**************************************************************

# Draw all objects in the scene
def drawScene(mode):
    #displayCoords = []
    #prevcoords = []
    #nextcoords = []
    #for i in range (4):
    #    displayCoords.append(convertToDisplayCoordinates(project(SceneData[0][0][i])))
    #    prevcoords.append(convertToDisplayCoordinates(project(SceneData[0][7][i])))
    #    nextcoords.append(convertToDisplayCoordinates(project(SceneData[0][1][i])))
    
    # create an edge table for the current poly
    # print(displayCoords, end = "\ndisplay\n")
    #edgeTable = generateEdgeTable(prevcoords, displayCoords, nextcoords)
    #print(edgeTable, end = "\n\n")
    #print(getVertexNormals(SceneData[0][7], SceneData[0][0], SceneData[0][1]),end="\n\n")
    #print(getVertexNormals(SceneData[0][8], SceneData[0][8], SceneData[0][8]),end="\n\n")
    #print(generateEdgeTable(SceneData[0][8], SceneData[0][8], SceneData[0][8]),end="\n\n")
    global MaxDistance
    global CanvasWidth
    global CanvasHeight
    global zBuffer
    # Reset the zBuffer array to its initial state before drawing anything
    zBuffer =  [[MaxDistance for c in range(CanvasHeight)] for r in range(CanvasWidth)]
    # If the shape being drawn is the currently selected one, draw it in red
    for i in range(0, len(SceneData),4):
       if i == selected:
           drawObject(mode, SceneData[i], "red", SceneData[i+3])
       else:
           drawObject(mode, SceneData[i], "black", SceneData[i+3])
    # print("break")
    # drawObject(mode, SceneData[4], "black", SceneData[4+3])
    
# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(mode, Shape, edgeColor, faceColors):
    # for each polygon in the given object, draw it
    # this is a hack so that I can do access the neighboring polys in the
    # cylinder for shading calculations
    for i in range(len(Shape)):
        if i <= 7:
            drawPoly(mode, Shape[(i-1)%8], Shape[i], Shape[(i+1)%8], edgeColor, faceColors[i])
        else:
            drawPoly(mode, Shape[i], Shape[i], Shape[i], edgeColor, faceColors[i])
    # print("drawObject stub executed.")

# This function determines the visibilty of a poly annd only draws the visible ones
# Then is determines the current drawing mode and either calls only drawEdges, only fillPoly,
# or both drawEdges and fillPoly. Only fillPoly implements z-buffer but both use backface culling
def drawPoly(mode, prevpoly, poly, nextpoly, edgeColor, faceColor):
    if isVisible(poly):
        fillPoly(mode, prevpoly, poly, nextpoly, edgeColor, faceColor)
        # print("drawPoly stub executed.")

# Fill in the poly pixel by pixel, only filling the pixels closest in
# the Z direction to the viewpoint. Color can be predetermined or generated per
# Flat, Gouraud, or Phong shading
def fillPoly(mode, prevpoly, poly, nextpoly, edgeColor, faceColor):
    #[polyPoints[indx],polyPoints[(indx+-1)%len(polyPoints)],
    # Xstart, Ystart, Yend, dX, Zstart, dZ,
    # Istart[1], dId, Istart[2], dIs,
    # Nxstart, dNx, Nystart, dNy, Nzstart, dNz1]
    
    # point A = 0
    # point B = 1
    # Xstart = 2
    # Ystart = 3
    # Yend = 4
    # dX = 5
    # Zstart = 6
    # dZ = 7
    # Diffuse start = 8
    # dIdiffuse = 9
    # Specular start = 10
    # dIspecular = 11
    # x of start normal = 12
    # dNx of start normal = 13
    # y of start normal = 14
    # dNy of start normal = 15
    # z of start normal = 16
    # dNz of start normal = 17
    
    global Ia
    global Ip
    global Kd
    global Ks
    global SpecIndex
    global L
    global V
    # If we are doing flat shading change faceColor by finding the intensity
    # at a single point and assigning faceColor to it
    if mode == 4:
        N = getNormal(poly)
        intensity = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, N, normalize(L), normalize(V))
        faceColor = triColorHexCode(intensity[0], intensity[1], intensity[2])
        
    # if only drawing the frame, just draw the frame
    if mode == 1:
        for i in range (len(poly)):
            start = convertToDisplayCoordinates(project(poly[i]))
            end = convertToDisplayCoordinates(project(poly[(i+1)%len(poly)]))
            w.create_line(start[0], start[1], end[0], end[1], fill=edgeColor)
        return
    
    # for any other mode, fill the polygon with the appropriate parameters
    # 2 is faceColor and the only one which also includes the wireframe,
    # 3 is faceColor, 4 is flat shading, 5 is Gouraud, 6 is Phong
    else:
        global zBuffer
        # generate an array storing the display coordinates and z values of each point in poly
        displaycoords = []
        prevcoords = []
        nextcoords = []
        for i in range (len(poly)):
            displaycoords.append(convertToDisplayCoordinates(project(poly[i])))
            prevcoords.append(convertToDisplayCoordinates(project(prevpoly[i])))
            nextcoords.append(convertToDisplayCoordinates(project(nextpoly[i])))
        
        # create an edge table for the current poly
        # print(displayCoords, end = "\ndisplay\n")
        edgeTable = generateEdgeTable(prevcoords, prevpoly, displaycoords, poly, nextcoords, nextpoly)
        # print(edgeTable, end = "\n\n")

        if edgeTable == []:
            return
        
        # find the start and end fill lines
        try:
            firstFillLine = edgeTable[0][3]
        except:
            firstFillLine = 0.0
        try:
            lastFillLine = edgeTable[len(edgeTable)-1][4]
        except:
            lastFillLine = CanvasHeight

        # initialize the first few edges X and Z values into variables
        # p.s. I will always suck as naming variables, so I took O'Neal's
        I, J, Next = 0, 1, 2
        EdgeIX = edgeTable[I][2]
        EdgeIZ = edgeTable[I][6]
        EdgeIId = edgeTable[I][8]
        EdgeIIs = edgeTable[I][10]
        EdgeINx = edgeTable[I][12]
        EdgeINy = edgeTable[I][14]
        EdgeINz = edgeTable[I][16]
        
        EdgeJX = edgeTable[J][2]
        EdgeJZ = edgeTable[J][6]
        EdgeJId = edgeTable[J][8]
        EdgeJIs = edgeTable[J][10]
        EdgeJNx = edgeTable[J][12]
        EdgeJNy = edgeTable[J][14]
        EdgeJNz = edgeTable[J][16]
        
        # Go fillLine by fillLine, pixel by pixel and only draw the closest pixels in the z direction
        for r in range(int(firstFillLine), int(lastFillLine+1)):
            # Determine which edge is Left and which is Right
            if EdgeIX < EdgeJX:
                LeftX, LeftZ = EdgeIX, EdgeIZ
                LeftId, LeftIs = EdgeIId, EdgeIIs
                LeftNx, LeftNy, LeftNz = EdgeINx, EdgeINy, EdgeINz
                
                RightX, RightZ = EdgeJX, EdgeJZ
                RightId, RightIs = EdgeJId, EdgeJIs
                RightNx, RightNy, RightNz = EdgeJNx, EdgeJNy, EdgeJNz

            else:
                LeftX, LeftZ = EdgeJX, EdgeJZ
                LeftId, LeftIs = EdgeJId, EdgeJIs
                LeftNx, LeftNy, LeftNz = EdgeJNx, EdgeJNy, EdgeJNz
                
                RightX, RightZ = EdgeIX, EdgeIZ
                RightId, RightIs = EdgeIId, EdgeIIs
                RightNx, RightNy, RightNz = EdgeINx, EdgeINy, EdgeINz
                
            # The initial Z for the current fill line
            Z = LeftZ
            ambient = Ia * Kd
            diffuse = LeftId
            specular = LeftIs
            Nx = LeftNx
            Ny = LeftNy
            Nz = LeftNz
            
            # Compute dZ for the fill line. Can be 0 if line is 1 pixel long
            if RightX-LeftX != 0:
                dZFillLine = (RightZ-LeftZ)/(RightX-LeftX)
                dIdFillLine = (RightId-LeftId)/(RightX-LeftX)
                dIsFillLine = (RightIs-LeftIs)/(RightX-LeftX)
                dNxFillLine = (RightNx-LeftNx)/(RightX-LeftX)
                dNyFillLine = (RightNy-LeftNy)/(RightX-LeftX)
                dNzFillLine = (RightNz-LeftNz)/(RightX-LeftX)
            else:
                dZFillLine = 0
                dIdFillLine = 0
                dIsFillLine = 0
                dNxFillLine = 0
                dNyFillLine = 0
                dNzFillLine = 0
                    
            # Paint across a fill line
            for c in range(int(LeftX), int(RightX)+1):
                # check if the current pixel is an edge
                onEdge = (c == int(LeftX) or c == int(RightX)) or (r == int(firstFillLine) or r == int(lastFillLine))
                try:
                    # if the current pixel is the closest according to the zBuffer, draw it
                    if Z < zBuffer[r][c]:
                        # if in mode 2 and on edge, draw the pixel in the edgeColor
                        if mode == 2 and onEdge:
                            w.create_line(c, r, c+1, r, fill=edgeColor)
                        elif mode == 5:
                            faceColor = triColorHexCode(ambient, diffuse, specular)
                            w.create_line(c, r, c+1, r, fill=faceColor)
                        elif mode == 6:
                            intensity = getIntensity(Ia, Ip, Kd, Ks, SpecIndex, normalize([Nx, Ny, Nz]), normalize(L), normalize(V))
                            #print(intensity)
                            faceColor = triColorHexCode(intensity[0], intensity[1], intensity[2])
                            w.create_line(c, r, c+1, r, fill=faceColor)
                        else:
                            w.create_line(c, r, c+1, r, fill=faceColor)
                        zBuffer[r][c] = Z
                    Z += dZFillLine
                    diffuse += dIdFillLine
                    specular += dIsFillLine
                    Nx += dNxFillLine
                    Ny += dNyFillLine
                    Nz += dNzFillLine
                except:
                    pass
            
            # Update the X and Z values of edges I and J for the next fill line
            if edgeTable[I][5] == "undefined":
                EdgeIX += 0
            else:
                EdgeIX += edgeTable[I][5]
            if edgeTable[J][5] == "undefined":
                EdgeJX += 0
            else:
                EdgeJX += edgeTable[J][5]
                
            EdgeIZ += edgeTable[I][7]
            EdgeJZ += edgeTable[J][7]

            EdgeIId += edgeTable[I][9]
            EdgeIIs += edgeTable[I][11]
            EdgeJId += edgeTable[J][9]
            EdgeJIs += edgeTable[J][11]

            EdgeINx += edgeTable[I][13]
            EdgeINy += edgeTable[I][15]
            EdgeINz += edgeTable[I][17]
            EdgeJNx += edgeTable[J][13]
            EdgeJNy += edgeTable[J][15]
            EdgeJNz += edgeTable[J][17]

            # Upon reaching the bottom of an edge switch out with next edge
            if (r >= edgeTable[I][4]) and (r < lastFillLine):
                I = Next
                EdgeIX = edgeTable[I][2]
                EdgeIZ = edgeTable[I][6]
                EdgeIId = edgeTable[I][8]
                EdgeIIs = edgeTable[I][10]
                EdgeINx = edgeTable[I][12]
                EdgeINy = edgeTable[I][14]
                EdgeINz = edgeTable[I][16]
                Next += 1
            if (r >= edgeTable[J][4]) and (r < lastFillLine):
                J = Next
                EdgeJX = edgeTable[J][2]
                EdgeJZ = edgeTable[J][6]
                EdgeJId = edgeTable[J][8]
                EdgeJIs = edgeTable[J][10]
                EdgeJNx = edgeTable[J][12]
                EdgeJNy = edgeTable[J][14]
                EdgeJNz = edgeTable[J][16]
                Next += 1
    
# ****************************Interface/Management******************************************

def switchObject():
    w.delete(ALL)
    global selected
    global mode
    selected = (selected + 4) % len(SceneData)
    drawScene(mode)

def setMode(pressed):
    w.delete(ALL)
    global mode
    keypressed = pressed.char
    if keypressed == '1': mode = 1
    if keypressed == '2': mode = 2
    if keypressed == '3': mode = 3
    if keypressed == '4': mode = 4
    if keypressed == '5': mode = 5
    if keypressed == '6': mode = 6
    drawScene(mode)

def reset():
    w.delete(ALL)
    resetObject(SceneData[selected+1], SceneData[selected+2])
    global mode
    drawScene(mode)

def larger():
    w.delete(ALL)
    scale(SceneData[selected+1], 1.1)
    global mode
    drawScene(mode)

def smaller():
    w.delete(ALL)
    scale(SceneData[selected+1], .9)
    global mode
    drawScene(mode)

def forward():
    w.delete(ALL)
    translate(SceneData[selected+1], [0, 0, 5])
    global mode
    drawScene(mode)

def backward():
    w.delete(ALL)
    translate(SceneData[selected+1], [0, 0, -5])
    global mode
    drawScene(mode)

def left():
    w.delete(ALL)
    translate(SceneData[selected+1], [-5, 0, 0])
    global mode
    drawScene(mode)

def right():
    w.delete(ALL)
    translate(SceneData[selected+1], [5, 0, 0])
    global mode
    drawScene(mode)

def up():
    w.delete(ALL)
    translate(SceneData[selected+1], [0, 5, 0])
    global mode
    drawScene(mode)

def down():
    w.delete(ALL)
    translate(SceneData[selected+1], [0, -5, 0])
    global mode
    drawScene(mode)

def xPlus():
    w.delete(ALL)
    rotateX(SceneData[selected+1], 5)
    global mode
    drawScene(mode)

def xMinus():
    w.delete(ALL)
    rotateX(SceneData[selected+1], -5)
    global mode
    drawScene(mode)

def yPlus():
    w.delete(ALL)
    rotateY(SceneData[selected+1], 5)
    global mode
    drawScene(mode)

def yMinus():
    w.delete(ALL)
    rotateY(SceneData[selected+1], -5)
    global mode
    drawScene(mode)

def zPlus():
    w.delete(ALL)
    rotateZ(SceneData[selected+1], 5)
    global mode
    drawScene(mode)

def zMinus():
    w.delete(ALL)
    rotateZ(SceneData[selected+1], -5)
    global mode
    drawScene(mode)

root = Tk()
root.bind('<Key>', lambda i: setMode(i))
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
drawScene(mode)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

selectioncontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
selectioncontrols.pack(side=LEFT)

selectioncontrolslabel = Label(selectioncontrols, text="Select")
selectioncontrolslabel.pack()

selectNextButton = Button(selectioncontrols, text="Next", command=switchObject)
selectNextButton.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

downButton = Button(translatecontrols, text="DN", command=down)
downButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

root.mainloop()
