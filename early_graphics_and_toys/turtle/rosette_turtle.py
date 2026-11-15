#Créé le 5 Février 2023
from turtle import * 
from random import *

couleurs = ['blue', 'red', 'green', 'yellow', 'brown', 'black', 'white', 'pink', 'orange', 'purple', 'gray']

def rosace():
  speed(10)
  color(choice(couleurs))
  c=int(input("Quel largeur fera la rosace (55) ? "))
  b=int(input("Combien de boucles aura la rosace (20) ? "))
  d=360/b
  for a in range(b):
    circle(c)
    backward(1)
    right(d)
  hideturtle()

rosace()
