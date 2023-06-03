from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import sin, cos, pi
import math
import time
UserAngle = float(input("Enter Angle (0 < Angle < 180): "))


def Plot(x, y, g):
    if g == 'p':

        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(3.0)

    glBegin(GL_POINTS)

    glVertex2f(x, y)
    glEnd()


def Line(p1, p2):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])

    glEnd()


def Circle(cx, cy, radius):
    xi, yi = radius, 0

    angle = 15*math.pi/180
    theta = 0
    while theta <= 2*pi:

        glColor3f(1.0, 1.0, .0)
        glBegin(GL_TRIANGLES)
        glVertex2f(cx, cy)
        glVertex2f(xi+cx, yi+cy)
        nxi = radius * math.cos(theta)
        nyi = radius * math.sin(theta)
        glVertex2f(nxi+cx, nyi+cy)
        xi, yi = nxi, nyi
        theta = theta+angle
        glEnd()


def Rebound():

    p1 = (3, 40)
    p2 = (135, 40)
    p3 = (3, 5)
    p4 = (135, 5)
    h = p3[1]-p1[1]
    h = abs(h)
    global UserAngle
    theta = UserAngle

    Line(p1, p2)
    Line(p3, p4)

    if theta > 90:
        x1 = p4[0]
        y1 = p4[1]
        xadd = -3
    elif theta < 90:
        x1 = p3[0]
        y1 = p3[1]
        xadd = +3
    else:
        x1 = (p3[0] + p4[0])/2
        y1 = (p3[1] + p4[1])/2
        xadd = 0

    x = y = 0
    hypo = h/sin(theta*pi/180)

    r = hypo/500
    c = 0

    Up = []
    while c < hypo:
        glClear(GL_COLOR_BUFFER_BIT)
        Line((p1[0], p1[1]+2), (p2[0], p2[1]+2))
        Line((p3[0], p3[1]-2), (p4[0], p4[1]-2))

        x = c * cos(theta*pi / 180)
        y = c * sin(theta*pi/180)
        Up.append((x+xadd, y))
        for point in Up:
            Plot(x1+point[0], y1+point[1], "g")
        Circle(x+x1+xadd, y+y1, 2)
        Plot(x+x1+xadd, y+y1, "g")
        c = c+r
        glutSwapBuffers()
        time.sleep(0.001)
    x0 = x
    y0 = y
    x, y = 0, 0
    c = 0
    Down = []
    while c < hypo:
        glClear(GL_COLOR_BUFFER_BIT)
        Line((p1[0], p1[1]+2), (p2[0], p2[1]+2))
        Line((p3[0], p3[1]-2), (p4[0], p4[1]-2))

        x = c * cos(-theta*pi / 180)
        y = c * sin(-theta*pi/180)
        for point in Up:
            Plot(x1+point[0], y1+point[1], "g")
        Down.append((x+xadd, y))
        for point in Down:
            Plot(x0+x1+point[0], y0+y1+point[1], "g")

        Circle(x+x0+x1+xadd, y+y0+y1, 2)
        Plot(x+x0+x1+xadd, y+y0+y1, "g")
        c = c+r
        glutSwapBuffers()
        time.sleep(0.001)

    glutSwapBuffers()


def Transformations():
    glClear(GL_COLOR_BUFFER_BIT)
    Rebound()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(1400, 450)
    glutInitWindowPosition(00, 00)
    glutCreateWindow("Ball Rebound")
    gluOrtho2D(0.0, 140, 0, 45)
    glutDisplayFunc(Transformations)
    glutMainLoop()


main()
