from mayavi import mlab
mlab.init_notebook(backend = 'x3d' , local=False)

theta=np.linspace(0, 2*np.pi,100)
phi= np.linspace(0, 2*np.pi,100)

X = np.outer((1+0.2*np.cos(phi)),np.cos(theta))
Y = np.outer((1+0.2*np.cos(phi)),np.sin(theta))
Z = np.outer(np.sin(phi), 0.09*np.ones(np.size(theta)))
x, y, z, value = np.random.random((4,2))
mlab.clf()
mlab.points3d(x, y, z,value,color=(1,1,1))
mlab.mesh(X,Y,Z, representation='wireframe')