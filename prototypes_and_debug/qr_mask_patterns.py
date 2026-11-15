#Créé le 3 Août 2023
from kandinsky import *

fill_rect(0,0,320,222,(0,255,0))

def calculation(n):
  if n==0:
    return lambda i, j: not j % 3
  if n==1:
    return lambda i, j: not (i + j) % 3
  if n==2:
    return lambda i, j: not (i + j) % 2
  if n==3:
    return lambda i, j: not i % 3
  if n==4:
    return lambda i, j: not ((i * j) % 3 + i * j) % 2
  if n==5:
    return lambda i, j: not ((i * j) % 3 + i + j) % 2
  if n==6:
    return lambda i, j: not (i // 2 + j // 3) % 2
  if n==7:
    return lambda i, j: not (i * j) % 2 + (i * j) % 3

def draw(n):
  calcul=calculation(n)
  for i in range(222):
    for j in range(320):
      if calcul(i, j):
        fill_rect(j, i, 1, 1, (0, 0, 255))

draw(4)
