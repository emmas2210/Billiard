from __future__ import absolute_import, division, print_function
import mayavi
from mayavi import mlab
from numpy import array, cos, sin, cos
import random, math
import numpy as np

theta=np.linspace(0, 2*np.pi,100)
phi= np.linspace(0, 2*np.pi,100)

X = np.outer((20+4*np.cos(phi)),np.cos(theta))
Y = np.outer((20+4*np.cos(phi)),np.sin(theta))
Z = np.outer(np.sin(phi), 1.8*np.ones(np.size(theta)))

#the position of the ball
x_coord = array([0.0, 1.0, 0.0, -1.0])
y_coord = array([1.0, 0.0, -1.0, 0.0])
z_coord = array([0.2, -0.2, 0.2, -0.2])

mlab.clf()
plt=mlab.points3d(x_coord,y_coord,z_coord, color=(1,1,1),resolution=10,scale_factor=3)
mlab.mesh(X,Y,Z, representation='wireframe')



msplt = plt.mlab_source
@mlab.animate(delay=500)
def anim():
    angle = 0.0
    while True:
        x_coord = array([15*sin(angle)])
        y_coord = array([15*cos(angle)])
        msplt.set(x=x_coord, y=y_coord)
        yield
        angle += random.uniform(0,2*math.pi)

anim()
mlab.show()

