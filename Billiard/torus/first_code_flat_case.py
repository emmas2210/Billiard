from tkinter import*
import math,random

LARGEUR = 600
HAUTEUR = 400
RAYON = 15 # radius of the ball
collision =str()
# initial position in the center of the window
X = LARGEUR/2
Y = HAUTEUR/2
# directions 
vitesse = random.uniform(1.8,2)*5
angle = random.uniform(0,2*math.pi)
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)

def deplacement():
    """ deplacement of the ball """
    global X,Y,DX,DY,RAYON,LARGEUR,HAUTEUR,collision
    # rebound right
    if X+RAYON+DX > 550:
        X = 2*(550-RAYON)-X
        DX = -DX
        
        # rebound left
    if X-RAYON+DX < 50:
        X = 2*(50+RAYON)-X
        DX = -DX
        
    # rebound down
    if Y+RAYON+DY > 350:
        Y = 2*(350-RAYON)-Y
        DY = -DY
        
    # rebound up
    if Y-RAYON+DY < 50:
        Y = 2*(50+RAYON)-Y
        DY = -DY
        
    X = X+DX
    Y = Y+DY
    
    #create the ball
    canvas.coords(balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    # up to date every 20 ms
    tk.after(20,deplacement)

#creation of the window    
tk = tkinter.Tk()
tk = Tk()
tk.title("Flat Torus Billiard Game")
label_title=Label(tk,text="Welcome to billiard game")
label_title.pack()
canvas = tkinter.Canvas(tk, width=LARGEUR, height=HAUTEUR,background='white') 
canvas.pack(padx=10,pady=10)
oval=canvas.create_oval(50,50,550,350,fill="green")
balle = canvas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,fill='white')
button = Button(tk, text='Quit',command=tk.destroy)
button.pack()

deplacement()
tk.mainloop()