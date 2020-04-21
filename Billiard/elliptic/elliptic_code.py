#code pour elliptic billiard
import numpy as np
import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import matplotlib.patches as pch
from tkinter import *
import threading 
import time 
from math import*
import random
from mpl_toolkits.mplot3d import Axes3D
import tkinter
#we start by creating an empty word called "collision"
collison=str()
#We define the function of the ball's movement: 
def deplacement():
    global dx, dy,collision
    if canvas.coords(balle1)[3]>400:
        dy=-1*dy
        collision+='h'
    if (canvas.coords(balle1)[2]>400):
        dx=-1*dx
        collision+='v'
    if (canvas.coords(balle1)[1]<0):
        dy=-1*dy
        collision+='h'
    if (canvas.coords(balle1)[0]<0):
        dx=-1*dx
        collision+='v'
            
    #Ball's movement :
    canvas.move(balle1,dx,dy)
    #We reiterate this function 
    tk.after(20,deplacement)
    print(collision)

#Initial movement
dx=3
dy=5

# We create a new window with the tkinter function 
tk = Tk()
tk.title("Square Billiard Game")
label_title=Label(tk,text="Welcome to billiard game")
label_title.pack()
canvas = tkinter.Canvas(tk, width="400", height="400",background='#096a09') #Dimension square are 400x400
canvas.pack(padx=10,pady=10)

#We create an "exit" button
Bouton_Quitter=Button(tk, text ='Quit', command = tk.destroy)
#We add it to the window:
Bouton_Quitter.pack(side = LEFT, padx=5,pady=5)

#We create an "go" button which change the ball's speed
BoutonGo = Button(tk, text ='Go', command = deplacement)
BoutonGo.pack(side = LEFT, padx=10,pady=10)


#We create the ball 
balle1 = canvas.create_oval(10,10,30,30,fill='white')

deplacement()

#We launch the windomw with animation
tk.mainloop()