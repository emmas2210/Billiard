import tkinter 
from tkinter import *
import math,random
from random import randint



LARGEUR = 350
HAUTEUR = 350
RAYON = 15 # rayon de la balle

# position initiale au milieu
X = LARGEUR/2
Y = HAUTEUR/2
#pas de déplacement
vitesse = random.uniform(1.8,2)*3
angle = random.uniform(0,2*math.pi)
dx = vitesse*math.sin(angle)
dy = vitesse*math.cos(angle)

#variable 0 for stopping et 1 for moving
flag=0
#to start mobing the ball after stopping it and to change the speed and the direction 
def start():
    global flag, dx,dy
    dx,dy,flag = randint(-10,10),randint(-10,10),1
    move()
#to stop the ball    
def stop():
    global flag,dx,dy
    dx,dy,flag=0,0,0
#to move of the ball
def move():
    global X ,Y, dx,dy
     
    if Y+RAYON+dy < 0:
        Y = 350-RAYON
        dy = dy 
        
    if X+RAYON+dx > 350:
        X= RAYON
        dx = dx 
        
    if X+RAYON+dx < 0:
        X= 350-RAYON
        dx=dx
   
    if Y+RAYON+dy > 350:
        Y = RAYON
        dy = dy 
    
        
    X = X+dx
    Y = Y+dy
        
    canvas.coords(balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    # mise à jour toutes les 50 ms
    tk.after(20,move)
    
tk = tkinter.Tk()
tk = Tk()
tk.title("Flat Torus Billiard Game")
label_title=Label(tk,text="Welcome to billiard game")
label_title.pack()
canvas = tkinter.Canvas(tk, width=LARGEUR, height=HAUTEUR,background='green') 
canvas.pack(padx=10,pady=10)

balle = canvas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,fill='white')
button = Button(tk, text='Quit',command=tk.destroy)
button.pack()
button1 = Button(tk, text='Start',command=start)
button1.pack()

button2 = Button(tk,text='Stop',command=stop)
button2.pack()

move()
tk.mainloop()