import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fig_tor_3d():
    theta=np.linspace(0, 2*np.pi,100)
    phi= np.linspace(0, 2*np.pi,100)

    X = np.outer((1+0.2*np.cos(phi)),np.cos(theta))
    Y = np.outer((1+0.2*np.cos(phi)),np.sin(theta))
    Z = np.outer(np.sin(phi), 0.09*np.ones(np.size(theta)))

    fig=plt.figure()
    ax=fig.gca(projection='3d')

    ax.plot_surface(X ,Y ,Z, rstride=1, cstride=1)
    ax.set_zlim3d(-0.45,0.45)
    plt.show()
    
fig_tor_3d()