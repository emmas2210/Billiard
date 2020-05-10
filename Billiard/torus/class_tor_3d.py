import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class tor_3d():

    def __init__(self,theta,phi,X,Y,Z):
        self.theta=self.np.linspace(0, 2*np.pi,100)
        self.phi=self.np.linspace(0 ,2*np.pi,100)

        self.X=self.np.outer((1+0.2*np.cos(self.phi)),np.cos(self.theta))
        self.Y=self.np.outer((1+0.2*np.cos(self.phi)),np.sin(self.theta))
        self.Z=self.np.outer(np.sin(self.phi), 0.09*np.ones(np.size(self.theta)))


    def fig_tor_3d():
        fig=plt.figure()
        ax=fig.gca(projection='3d')

        ax.plot_surface(self.X ,self.Y ,self.Z, rstride=1, cstride=1)
        ax.set_zlim3d(-0.45,0.45)
        plt.show()
    