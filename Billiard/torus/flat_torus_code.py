import tkinter as tk
import random 
import math

class flat_torus(tk.Tk):
    """ This class allows us to visualize a window inside wich we can see mouvements of a ball into a 2d torus"""
    def __init__(self):
        """ Initialisation of class elements:
        x and y: paramaeters of the initial coordonates of the ball (center of the window)
        size:parameter of radius of the ball
        dx and dy: parameters of deplacement steps
        """
        tk.Tk.__init__(self)
        self.x, self.y = 125 , 125
        self.size = 15
        self.vitesse = random.uniform(1.8,2)*5
        self.angle = random.uniform(0,2*math.pi)
        self.dx = self.vitesse*math.cos(self.angle) 
        self.dy = self.vitesse*math.sin(self.angle)
        
        """Creation of the window
        canv: the window
        height : height of the window 
        width : width of the window
        background: color of the window
        oval : oval shape which represents the 2d torus 
        fill : color of the torus 
        bouton_quit: button to quit the game"""
        self.label_title=tk.Label(self,text="Welcome to billiard game")
        self.label_title.pack()
        self.canv = tk.Canvas(self, height=350, width=350, background="green")
        self.canv.pack()
        self.bouton_quit = tk.Button(self, text="Quit",command=self.destroy)
        self.bouton_quit.pack()

        """ Creation of the ball"""
        self.ball = self.canv.create_oval(self.x-self.size,self.y-self.size,self.x+self.size,self.y+self.size,width=1,fill='white')
        """ To make the ball move we should add this"""
        self.move()

        
    def move(self):
        """ Ball bounces"""
        """Rebound right"""
        if self.x + self.size+ self.dx > 350:
            self.x = 2*(350-self.size)-self.x
            self.dx = -self.dx

        """Rebound left"""   
        if self.x - self.size+ self.dx < 0:
            self.x = 2*(self.size)-self.x
            self.dx = -self.dx

        """Rebound down"""    
        if self.y+self.size+self.dy > 350:
            self.y = 2*(350-self.size)-self.y
            self.dy = -self.dy

        """Rebound up"""    
        if self.y-self.size+self.dy < 0:
            self.y = 2*(self.size)-self.y
            self.dy = -self.dy
            
            
        self.x = self.x + self.dx
        self.y = self.y + self.dy   
        self.canv.coords(self.ball, self.x-self.size, self.y-self.size, self.x+self.size,self.y+self.size)
        """ Remind move every 20 ms"""
        self.after(20, self.move)
        


if __name__ == "__main__":
    fen = flat_torus()
    fen.title("Flat Torus Billiard")
    fen.mainloop()