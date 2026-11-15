#Cree le 5 Février 2023
from kandinsky import *
from math import *
from random import *
from time import *

couleurs = ['blue', 'red', 'green', 'yellow', 'brown', 'black', 'pink', 'orange', 'purple', 'gray']

def cercle1(x0,y0,r,c,e):
  for i in range(2*e):
    xd=x0-int((r-i*0.5)/sqrt(2))
    xf=x0+int((r-i*0.5)/sqrt(2))
    for x in range(xd,xf+1):
      x1=x
      y1=y0+int(sqrt((r-i*0.5)**2-(x-x0)**2))
      set_pixel(x,y1,c)
      for j in range(3):
        x2=x0+y1-y0
        y2=y0+x0-x1
        set_pixel(x2,y2,c)
        x1,y1=x2,y2
        
def cercle2(x0,y0,r,c,e):
  for i in range(2*e):
    xd=x0-int((r-i*0.5)/sqrt(2))
    xf=x0+int((r-i*0.5)/sqrt(2))
    for x in range(xd,xf+1):
      x1=x
      y1=y0+int(sqrt((r-i*0.5)**2-(x-x0)**2))
      if sqrt((160-x1)**2+(111-y1)**2)<r:
        set_pixel(x1,y1,c)
      for j in range(3):
        x2=x0+y1-y0
        y2=y0+x0-x1
        if sqrt((160-x2)**2+(111-y2)**2)<r:
          set_pixel(x2,y2,c)
        x1,y1=x2,y2

def cercle3(x0,y0,r,c,e):
  for i in range(2*e):
    xd=x0-int((r-i*0.5)/sqrt(2))
    xf=x0+int((r-i*0.5)/sqrt(2))
    for x in range(xd,xf+1):
      x1=x
      y1=y0+int(sqrt((r-i*0.5)**2-(x-x0)**2))
      set_pixel(x,y1,c)
      for j in range(3):
        x2=x0+y1-y0
        y2=y0+x0-x1
        set_pixel(x2,y2,c)
        x1,y1=x2,y2

def rosace1():
  r=float(input("De quel taille sera la rosace (50) ? "))
  n=float(input("Combien de boucles aura la rosace (12) ? "))
  c=color(choice(couleurs))
  e=float(input("De quel taille sera le pinceau (1-5) ? "))
  x,y=160+r,111
  for i in range(n):
    x1=int(160+r*cos(i*2*pi/n))
    y1=int(111+r*sin(i*2*pi/n))
    cercle1(x1,y1,r,c,e)
  sleep(5)
  instructions()

def rosace2():
  r=float(input("De quel taille sera la rosace (100) ? "))
  n=float(input("Combien de boucles aura la rosace (6) ? "))
  c=color(choice(couleurs))
  e=float(input("De quel taille sera le pinceau (2-10) ? "))
  x,y=160+r,111
  for i in range(n):
    x1=int(160+r*cos(i*2*pi/n))
    y1=int(111+r*sin(i*2*pi/n))
    cercle2(x1,y1,r,c,e)
  cercle2(160,111,r,c,e)
  sleep(5)
  instructions()

def rosace3():
  r=float(input("De quel taille sera la rosace (50) ? "))
  n=float(input("Combien de boucles aura la rosace (10) ? "))
  c1=color(choice(couleurs))
  c2=color(choice(couleurs))
  e=float(input("De quel taille sera le pinceau (1) ? "))
  rj=r
  for j in range(n-2):
    rj=int(rj-rj/n)
    for i in range(n):
      x1=int(160+rj*cos(i*2*pi/n))
      y1=int(111+rj*sin(i*2*pi/n))
      if j==0 or j>n-4:
        col=c2
      else:
        col=c1
      cercle3(x1,y1,rj,col,e)
  sleep(5)
  instructions()

def instructions():
  print(" ")
  print(" ")
  print("Il y a 3 rosaces que tu peux tester.")
  print("La rosace 1, 2 ou 3.")
  print("Par exemple, tape simplement rosace1().")
  print("Entrez le nom de la fonction")
  fonction=input("à utiliser : ")
  resultat = eval(fonction)

instructions()
