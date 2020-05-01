#code of flat torus billiard
from tkinteer import*
import math,random
LARGEUR = 480
HAUTEUR = 320
RAYON = 15 # rayon de la balle
collision =str()
# position initiale au milieu
X = LARGEUR/2
Y = HAUTEUR/2
# direction initiale aléatoire
vitesse = random.uniform(1.8,2)*5
angle = random.uniform(0,2*math.pi)
DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)
def deplacement():
    """ Déplacement de la balle """
    global X,Y,DX,DY,RAYON,LARGEUR,HAUTEUR,collision
    # rebond à droite
    if X+RAYON+DX > LARGEUR:
        X = 2*(LARGEUR-RAYON)-X
        DX = -DX
        collision+='V'
    # rebond à gauche
    if X-RAYON+DX < 0:
        X = 2*RAYON-X
        DX = -DX
        collision+='V'
    # rebond en bas
    if Y+RAYON+DY > HAUTEUR:
        Y = 2*(HAUTEUR-RAYON)-Y
        DY = -DY
        collision+='H'
    # rebond en haut
    if Y-RAYON+DY < HAUTEUR-350:
        Y = 2*RAYON-Y
        DY = -DY
        collision+='H'
    X = X+DX
    Y = Y+DY
    print(collision)
    # affichage
    Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    # mise à jour toutes les 50 ms
    tk.after(20,deplacement)
    
tk = tkinter.Tk()
tk = Tk()
tk.title("Flat Torus Billiard Game")
label_title=Label(tk,text="Welcome to billiard game")
label_title.pack()
canvas = tkinter.Canvas(tk, width=LARGEUR, height=HAUTEUR,background='white') 
canvas.pack(padx=10,pady=10)
oval=canvas.create_oval(50,50,550,350,fill="green")

button = Button(tk, text='Quit',command=tk.destroy)
button.pack()

balle=canvas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,fill='white')
tk.mainloop()


