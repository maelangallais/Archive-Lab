#Créé le 01 Mai 2023
from turtle import *

while True:
  n=int(input("Combien de rep ? "))
  speed(10)
  penup()
  goto(-53,45)
  pendown()
  right(0)
  a,b=0,1
  for i in range(n):
    circle(a,90)
    a,b=b,a+b
