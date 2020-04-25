#code du torrus billiard
from mayavi import mlab
mlab.init_notebook(backend = 'x3d' , local=False)

theta=np.linspace(0, 2*np.pi,100)
phi= np.linspace(0, 2*np.pi,100)

X = np.outer((1+0.2*np.cos(phi)),np.cos(theta))
Y = np.outer((1+0.2*np.cos(phi)),np.sin(theta))
Z = np.outer(np.sin(phi), 0.09*np.ones(np.size(theta)))

mlab.clf()
mlab.mesh(X,Y,Z, representation='wireframe')

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