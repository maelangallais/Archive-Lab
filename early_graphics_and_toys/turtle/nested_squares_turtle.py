#Créé le 9 Mars 2023
from math import *
from turtle import *
from time import *

def carre(l):
  for i in range(4):
    forward(l)
    right(90)

def figure1():
  l=int(input("Quel longueur en pixels (200) ? "))
  n=int(input("Combien de carrés embriqués ? "))
  penup()
  speed(10)
  goto(-0.5*l,0.5*l)
  pendown()
  for i in range(n):
    carre(l)
    forward(l*0.5)
    right(45)
    l=sqrt((l**2)/2)
  hideturtle()
  sleep(5)
  instructions()

def figure2():
 l=int(input("Quel longueur en pixels (200) ? "))
 n=int(input("Combien de carrés embriqués ? "))
 penup()
 speed(10)
 goto(-0.5*l,0.5*l)
 pendown()
 for i in range(n):
  carre(l)
  forward(l*0.25)
  angle=atan(1/3)*180/pi
  right(angle)
  l=sqrt((0.75*l)**2+(0.25*l)**2)
 hideturtle()
 sleep(5)
 instructions()

def figure3():
 l=int(input("Quel longueur en pixels (200) ? "))
 n=int(input("Combien de carrés embriqués ? "))
 a=float(input("Quel angle d'orientation (<1) ? "))
 speed(10)
 if a>1:
   raise ValueError("Impossible")
 penup()
 goto(-0.5*l,0.5*l)
 pendown()
 for i in range(n):
  carre(l)
  forward(l*a)
  angle=atan(a/(1-a))*180/pi
  right(angle)
  l=sqrt(((1-a)*l)**2+(a*l)**2)
 hideturtle()
 sleep(5)
 instructions()

def figure4():
 l=int(input("Quel longueur en pixels (200) ? "))
 a=float(input("Quel angle d'orientation (<1) ? "))
 speed(10)
 if a>1: 
   raise ValueError("Impossible")
 penup()
 x=-160+((320-l)/2)
 y=111-((222-l)/2)
 goto(x,y)
 pendown()
 color(0,0,255)
 while l>5:
  color(l,255-l,255-l)
  carre(l)
  forward(l*a)
  angle=atan(a/(1-a))*180/pi
  right(angle)
  l=sqrt(((1-a)*l)**2+(a*l)**2)
 hideturtle()
 sleep(5)
 instructions()

def instructions():
  print(" ")
  print(" ")
  print("Il y a 4 figures que tu peux tester.")
  print("La figure 1, 2, 3 ou la figure 4.")
  print("Tape simplement 1, 2, 3 ou 4.")
  print("Entrez le nom de la fonction")
  resultat=input("à utiliser : ")
  n=eval(resultat)
  if n==1:
    figure1()
  if n==2:
    figure2()
  if n==3:
    figure3()
  if n==4:
    figure4()

instructions()
