
#Functions tests for square billiard:
import numpy as np 
import random 
import math 

def test_deplacement():
    vitesse=random.uniform(1,3)*4
    angle=random.uniform(0,3*math.pi)
    DX=vitesse*math.cos(angle)
    DY=vitesse*math.sin(angle)
                           



 

