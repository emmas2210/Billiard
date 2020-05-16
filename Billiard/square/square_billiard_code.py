#code of the billiard square :
from tkinter import *
import math,random
width = 480
height = 480
radius = 15 # rayon de la balle
collision =str()
# position initiale au milieu
X = width/2
Y = height/2
# direction initiale aléatoire
speed = random.uniform(1.8,2)*5
angle = random.uniform(0,2*math.pi)
DX = speed*math.cos(angle)
DY = speed*math.sin(angle)
def deplacement():
    """ 
    The aim of this function is to be able to control hops.
    We start by controlling hops from the right to the left and from the left to the right. Then we add an "V" if the ball hit the         right or left corner.
    It's the same to control hops from top to bottom and from bottom to top. However, we add an "H" if the ball hit the top or the         bottom of the square.
    :param bg: background color
    :type bg: word
        
    :param height: height oh the animation 
    :type height: int

    :param width: width oh the animation 
    :type width: int
    
    :param radius : Radius of the ball
    :type radius : int
    
    :param X : Initial coordinate of the ball
    :type X : int
    
    :param Y : Initial coordinate of the ball
    :type Y : int
    """
    global X,Y,DX,DY,radius,width,height,collision
    # rebond à droite
    if X+radius+DX > width:
        X = 2*(width-radius)-X
        DX = -DX
        collision+='V'
    # rebond à gauche
    if X-radius+DX < 0:
        X = 2*radius-X
        DX = -DX
        collision+='V'
    # rebond en bas
    if Y+radius+DY > height:
        Y = 2*(height-radius)-Y
        DY = -DY
        collision+='H'
    # rebond en haut
    if Y-radius+DY < 0:
        Y = 2*radius-Y
        DY = -DY
        collision+='H'
    X = X+DX
    Y = Y+DY
    print(collision)
    # affichage
    Canevas.coords(Balle,X-radius,Y-radius,X+radius,Y+radius)
    # mise à jour toutes les 50 ms
    Mafenetre.after(20,deplacement)
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")
label_title=Label(Mafenetre,text="Welcome to billiard game")
label_title.pack()
# Création d'un widget Canvas
Canevas = Canvas(Mafenetre,height=height,width=width,bg='green')
Canevas.pack(padx=5,pady=5)
# Création d'un objet graphique
Balle = Canevas.create_oval(X-radius,Y-radius,X+radius,Y+radius,width=1,fill='white')
#Bouton quitter
Bouton_Quitter=Button(Mafenetre, text ='Quit', command = Mafenetre.destroy)
Bouton_Quitter.pack()

deplacement()
Mafenetre.mainloop()