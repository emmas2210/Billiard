from tkinter import *
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
    if Y-RAYON+DY < 0:
        Y = 2*RAYON-Y
        DY = -DY
        collision+='H'
    X = X+DX
    Y = Y+DY
    print(collision)
    # affichage
    Canevas.coords(Balle,X-RAYON,Y-RAYON,X+RAYON,Y+RAYON)
    # mise à jour toutes les 50 ms
    Mafenetre.after(20,deplacement)
# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")
label_title=Label(Mafenetre,text="Welcome to billiard game")
label_title.pack()
# Création d'un widget Canvas
Canevas = Canvas(Mafenetre,height=HAUTEUR,width=LARGEUR,bg='green')
Canevas.pack(padx=5,pady=5)
# Création d'un objet graphique
Balle = Canevas.create_oval(X-RAYON,Y-RAYON,X+RAYON,Y+RAYON,width=1,fill='white')
#Bouton quitter
Bouton_Quitter=Button(Mafenetre, text ='Quit', command = Mafenetre.destroy)
Bouton_Quitter.pack()

deplacement()
Mafenetre.mainloop()


from mayavi import mlab
mlab.init_notebook(backend = 'x3d' , local=False)

theta=np.linspace(0, 2*np.pi,100)
phi= np.linspace(0, 2*np.pi,100)

X = np.outer((1+0.2*np.cos(phi)),np.cos(theta))
Y = np.outer((1+0.2*np.cos(phi)),np.sin(theta))
Z = np.outer(np.sin(phi), 0.09*np.ones(np.size(theta)))

mlab.clf()
mlab.mesh(X,Y,Z, representation='wireframe')