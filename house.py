
from turtle import *
import random

# lengths of the sides of the house

length = 100
diagonale = 140

# angles
square_angle = 90
acute_angle = 45
obtuse_angle = 135

""" 
diagonale bas droite - haut gauche
bas
droite
haut
toit montant droite
toit descendant gauche
droite
diagonale haut droite - bas gauche


"""
colors = ["green","red","blue","purple","grey"]
def create_house(size,colour,coord):
    
    color(colour)

    up()
    setpos(coord)
    down()

    begin_fill()

    hideturtle()
    
    left(obtuse_angle)
    forward(size*diagonale)

    left(obtuse_angle)
    forward(size*length)

    
    left(square_angle)
    forward(size*length)

    
    left(square_angle)
    forward(size*length)

    left(acute_angle)
    forward(size*diagonale/2)

    left(square_angle)
    forward(size*diagonale/2)

    left(obtuse_angle)
    forward(size*length)

    left(-obtuse_angle)
    forward(size*diagonale)



def create_city(nb_houses,colour,distance,size):
    i = 1
    
    while i < nb_houses:
        print("l'angle de depart "+ str(heading()))
        setheading(0)
        create_house(size,colour[i],[-550+(i*distance),-200])
        i+=1
        print("langle d'arrivée "+ str(heading()))

size = random.randint(1,3)
create_city(len(colors),colors,120,size)
screen = done()

