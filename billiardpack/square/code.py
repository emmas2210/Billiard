#code of the billiard square :
import tkinter
import random

window = tkinter.Tk()
tk = Tk()
tk.title("Square Billiard Game")
label_title=Label(tk,text="Welcome to billiard game")
label_title.pack()
canvas = tkinter.Canvas(tk, width="400", height="400",background='#096a09') #Dimension square are 400x400
canvas.pack(padx=10,pady=10)

balle1 = canvas.create_oval(10,10,30,30,fill='white')

dx=3
dy=5

def deplacement():
     global dx, dy
if (canvas.coords(balle1)[3]>400):
    dy=-1*dy
if (canvas.coords(balle1)[2]>400):
    dx=-1*dx
if (canvas.coords(balle1)[1]<0):
    dy=-1*dy
if (canvas.coords(balle1)[0]<0):
    dx=-1*dx
            
    #Ball's movement :
canvas.move(balle1,dx,dy)
    #We reiterate this function 
tk.after(20,deplacement)
 
Bouton_Quitter=Button(tk, text ='Quit', command = tk.destroy)
Bouton_Quitter.pack()
  
deplacement()



collision = str()

X2= (canvas.coords(balle1)[2]== 400)
X3= (canvas.coords(balle1)[3]== 400)
Z0= (canvas.coords(balle1)[0] == 0)
Z1= (canvas.coords(balle1)[1] == 0)
        

while len(collision)<200:
        X2=X3=random.randint(0,1)
        Z0=Z1=random.randint(0,1)
        if X2==X3==0:
            collision += 'h'
        if X2==X3==1:
            collision
        if Z0==Z1==0:
            collision += 'v'
        if Z0==Z1==1:
            collision


print(collision)
tk.mainloop()