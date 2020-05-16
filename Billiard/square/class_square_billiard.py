import tkinter as tk
import random as rd
#Usage: python tk_baballe.py
#- left click: grow the ball
#- right click: shrink the ball
#- clicking on the computer mouse wheel: change the ball's speed and its trajectory.
#- Esc: leave the game


class Billiard(tk.Tk):
    """
    This class allows to run an animation representing the ball's trajectory in a square billiard. 
    In this animation you can :
    - change the ball's speed and its trajectory by clicking on the computer mouse wheel
    - enlarge the ball by clicking on the left button of the computer mouse
    - shrink the ball by clicking on the right button of the computer mouse
    - leave the animation clicking on the "esc" button
    Here are parameters we used build the class :
    
    :param x: Ball's coordinate in width
    :type x: int

    :param y: Ball's coordinate in height
    :type y: int

    :param size: Radius of the ball
    :type size: int
    
    :param dx: Movement speed in width
    :type dx: int

    :param dy: Movement speed in height
    :type dy: int
    """
    def __init__(self):
        """We build the application using the packing "canvas". This packink allows us to create the widget
        :param bg: background color
        :type bg: word
        
        :param height: height oh the animation 
        :type height: int

       :param width: width oh the animation 
        :type width: int
        """

        tk.Tk.__init__(self)
        # coord baballe
        #self.collision="a"
        self.x, self.y = 20, 20
        # ball's radius
        self.size = 25.
        # pas de deplacement
        self.dx, self.dy = 20, 20
        # création et packing du canvas
        self.label_title=tk.Label(self,text="Welcome to billiard game")
        self.label_title.pack()
        self.canv = tk.Canvas(self, bg='green', height=400, width=400)
        self.canv.pack()
        self.bouton_quitter = tk.Button(self, text="Quitter",command=self.destroy)
        self.bouton_quitter.pack(side=tk.BOTTOM)

        # ball's creation
        self.ball = self.canv.create_oval(self.x, self.y,
                                             self.x+self.size,
                                             self.y+self.size,
                                             width=2, fill="white")
    
    
    
    # binding des actions
        self.canv.bind("<Button-1>", self.incr)
        self.canv.bind("<Button-2>", self.boom)
        self.canv.bind("<Button-3>", self.decr)
        self.bind("<Escape>", self.stop)
        # ball's movement
        self.move()

    def move(self):
        """This function create the ball's movement. We used the after's method to call this function every 50ms.
        """
        # incr coord baballe
        self.x += self.dx
        self.y += self.dy
        # vérifier que la baballe ne sort pas du canvas (choc élastique)
        if self.x < 10:
            self.dx = abs(self.dx)
            #self.collision+='h'
        if self.x > 400-self.size-10:
            self.dx = -abs(self.dx)
            #self.collision+='h'
        if self.y < 10:
            self.dy = abs(self.dy)
            #self.collision+='v'
        if self.y > 400-self.size-10:
            self.dy = -abs(self.dy)
            #self.collision+='v'
        # mise à jour des coord
        self.canv.coords(self.ball, self.x, self.y, self.x+self.size,
                         self.y+self.size)
        # rappel de move toutes les 50ms
        self.after(50, self.move)
    
    
    #print(collsion)

    def boom(self, mclick):
        """Launch the ball to some random direction at the click point"""
        self.x = mclick.x
        self.y = mclick.y
        self.canv.create_text(self.x, self.y, text="Boom !", fill="black")
        self.dx = rd.choice([-30, -20, -10, 10, 20, 30])
        self.dy = rd.choice([-30, -20, -10, 10, 20, 30])

    def incr(self, lclick):
        """Increase ball's size"""
        self.size += 10
        if self.size > 200:
            self.size = 200

    def decr(self, rclick):
        """Decrease ball's size"""
        self.size -= 10
        if self.size < 10:
            self.size = 10

    def stop(self, esc):
        """Stop the animation."""
        self.quit()


if __name__ == "__main__":
    window = Billiard()
    window.title("Ball's animation")
    window.mainloop()

