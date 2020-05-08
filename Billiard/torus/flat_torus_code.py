import tkinter as tk
import random as rd

class TORUS(tk.Tk):
    def __init__(self):
        """Constructeur de l'application."""
        tk.Tk.__init__(self)
        # coord  initial of the ball
        self.x, self.y = 300, 200
        # ball's radius
        self.size = 15
        # pas de deplacement
        self.vitesse = random.uniform(1.8,2)*5
        self.angle = random.uniform(0,2*math.pi)
        self.dx = self.vitesse*math.cos(self.angle) 
        self.dy = self.vitesse*math.sin(self.angle)
        
        # Creation of the window
        self.label_title=tk.Label(self,text="Welcome to billiard game")
        self.label_title.pack()
        self.canv = tk.Canvas(self, height=400, width=600, background="white")
        self.canv.pack()
        self.oval = self.canv.create_oval(50,50,550,350,fill="green")
        self.bouton_quit = tk.Button(self, text="Quit",command=self.destroy)
        self.bouton_quit.pack()

        # ball's creation
        self.ball = self.canv.create_oval(self.x-self.size,self.y-self.size,self.x+self.size,self.y+self.size,width=1,fill='white')
        # ball's movement
        self.move()

        
    def move(self):
        # collisions
        if self.x + self.size+ self.dx > 550:
            self.x = 2*(550-self.size)-self.x
            self.dx = -self.dx
            
        if self.x - self.size+ self.dx < 50:
            self.x = 2*(50+self.size)-self.x
            self.dx = -self.dx
            
        if self.y+self.size+self.dy > 350:
            self.y = 2*(350-self.size)-self.y
            self.dy = -self.dy
            
        if self.y-self.size+self.dy < 50:
            self.y = 2*(50+self.size)-self.y
            self.dy = -self.dy
            
            
        self.x = self.x + self.dx
        self.y = self.y + self.dy   
        self.canv.coords(self.ball, self.x-self.size, self.y-self.size, self.x+self.size,self.y+self.size)
        # rappel de move toutes les 20ms
        self.after(20, self.move)
        


if __name__ == "__main__":
    fen = TORUS()
    fen.title("Flat Torus Billiard")
    fen.mainloop()