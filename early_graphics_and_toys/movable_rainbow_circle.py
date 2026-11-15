#Créé le 15 Septembre 2023
from math import pi,cos,sin,floor,ceil
from kandinsky import fill_rect
from ion import *
from time import sleep
from random import randint

def ent(n):
  if n-floor(n)<0.5:n=floor(n)
  else:n=ceil(n)
  return int(n)

def rond(cx,cy,r,c):
  hyp=r
  for ang in range(4*r*pi):
    adj=cos(ang)*hyp
    x=cx+adj
    opp=sin(ang)*hyp
    y=cy+opp
    if y<0:y+=222
    elif y>222:y-=222
    if x>320:x-=320
    elif x<0:x+=320
    fill_rect(ent(x),ent(y),1,-2*ent(opp),(randint(0,255),randint(0,255),randint(0,255)))
    fill_rect(ent(x),ent(y),-2*ent(adj),1,(randint(0,255),randint(0,255),randint(0,255)))

new=True
x,y=160,111
a=20
t=0

while True:
  if new:
    new=False
    fill_rect(0,0,320,222,(255,255,255))
    rond(x,y,40,(0,0,0))
    sleep(t)
  if keydown(KEY_UP):
    if y>0+a:y-=a
    else:y+=222-a
    new=True
  elif keydown(KEY_DOWN):
    if y<222-a:y+=a
    else:y-=222-a
    new=True
  if keydown(KEY_RIGHT):
    if x<320-a:x+=a
    else:x-=320-a
    new=True
  elif keydown(KEY_LEFT):
    if x>0+a:x-=a
    else:x+=320-a
    new=True
