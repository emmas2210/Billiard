#code du torrus billiard
import pygame 
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def torus(a,b):
    tau = 2*math.pi
    for i in range(20):
        glBegin(GL_QUAD_STRIP)
        for j in range(20):
            for k in range(1,0):
                s = (i+k)%a +0.5
                t = j% b
                x = 1+ 0.2*cos(s*twopi/a)*cos(t*twopi/b)
                y = 1+0.2*cos(s*twopi/a)*sin(t*twopi/b)
                z = 0.2* sin(s*twopi/b)
                glVertex(x,y,z)
                
    glEnd()
    
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    torus()
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
window = glutCreateWindow("Flat Torus Billiard")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()