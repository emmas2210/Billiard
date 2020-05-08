from mayavi import mlab
import numpy as np
mlab.init_notebook('x3d',400,200,local=False)

mlab.clf()

theta=np.linspace(0, 2*np.pi,100)
phi= np.linspace(0, 2*np.pi,100)

X = np.outer((20+4*np.cos(phi)),np.cos(theta))
Y = np.outer((20+4*np.cos(phi)),np.sin(theta))
Z = np.outer(np.sin(phi), 1.8*np.ones(np.size(theta)))

#the position of the ball
x = np.array([2.5,3.0,3.0]) 
y = np.array([3.0,2.5,3.0]) 
z = np.array([3.0,3.0,2.5])

mlab.clf()
mlab.points3d(x[1:-1],y[1:-1],z[1:-1], color=(1,1,1),resolution=20,scale_factor=3)
mlab.mesh(X,Y,Z, representation='wireframe')
