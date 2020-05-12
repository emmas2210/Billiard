import tkinter as tk
import random 
import math
from random import randint


class flat_torus(tk.Tk):
    """ This class allows us to visualize a window inside wich we can see mouvements of a ball into a 2d torus 
    In this case the 2d torus is represented by a square in size (350,350)"""
    def __init__(self):
        """ Initialisation of class elements:
        x and y: paramaeters of the initial coordonates of the ball (center of the window)
        size:parameter of radius of the ball
        dx and dy: parameters of deplacement steps
        vitesse : parameters to change the speed
        flag : parameters wich value 0 if no movement and 1 to start movement
        """
        tk.Tk.__init__(self)
        self.x, self.y = 125 , 125
        self.size = 15
        self.vitesse = random.uniform(1.8,2)*3
        self.angle = random.uniform(0,2*math.pi)
        self.dx = self.vitesse*math.sin(self.angle) 
        self.dy = self.vitesse*math.cos(self.angle)
        self.flag = 0
       
       
       
        """Creation of the square window wich represent the 2d torus
        canv: the window
        height : height of the window 
        width : width of the window
        background: color of the window
        bouton_quit: button to quit the game
        bouton_start: to start the ball after stopping it and to change the speed
        bouton_stop : to stop the ball
        """
      
        self.label_title=tk.Label(self,text="Welcome to billiard game")
        self.label_title.pack()
        self.canv = tk.Canvas(self, height=350, width=350, background="green")
        self.canv.pack()
        self.bouton_quit = tk.Button(self, text="Quit",command=self.destroy)
        self.bouton_quit.pack()
        self.bouton_start = tk.Button(self,text="Start",command=self.start)
        self.bouton_start.pack()
        self.bouton_stop = tk.Button(self,text="Stop",command=self.stop)
        self.bouton_stop.pack()
        
        
        """ Creation of the ball"""
        self.ball = self.canv.create_oval(self.x-self.size,self.y-self.size,self.x+self.size,self.y+self.size,width=1,fill='white')
        
        """To make the ball move"""
        """To make the ball move"""
        self.move()

    """ We start by creating a function "start" to start moving the ball after stopping it and to change the 
    speed and also the direction.
    flag: parameter which value 0 to stop the ball and 1 to move it
    """
    def start(self):
        self.flag, self.dx, self.dy = 1,randint(-10,10), randint(-10,10)
        self.move()

    """We create a function "stop" to stop the ball"""
    def stop(self):
        self.flag, self.dx, self.dy = 0,0,0

    """Now we are going to create the function "move" that allows the ball to move.
    The ball enter in a bord of the square and comes out on the opposite bord"""
    def move(self):
        
        if self.y + self.size + self.dy < 0:
            self.y = 350 -self.size
            self.dy = self.dy

        if self.x + self.size + self.dx >350:
            self.x = self.size
            self.dx = self.dx

        if self.x + self.size + self.dx < 0:
            self.x = 350 -self.size
            self.dx = self.dx

        if self.y + self.size + self.dy > 350:
            self.y=self.size
            self.dy=self.dy

        self.x = self.x +self.dx
        self.y = self.y +self.dy

        self.canv.coords(self.ball,self.x-self.size,self.y-self.size,self.x+self.size,self.y+self.size)
       
        """To  remind move every 20ms"""
        self.after(20,self.move)

        
        
        
if __name__ == "__main__":
    fen = flat_torus()
    fen.title("Flat Torus Billiard")
    fen.mainloop()
        
    
      