#Créé le 31 Mars 2023
from kandinsky import fill_rect as fr
from random import randint as rd
from ion import keydown as kd
from time import sleep as sl

g,ifc=(150,)*3,(255,182,57)
z,bw,bh,m=0,320,222,3
w,h=bw//m,bh//m
sw,sh=bw%m,bh%m
fr(z,z,bw,sh,ifc),fr(z,z,sw,bh,ifc)
dspl=[[z]*h for i in range(w)]
for i in range(w*h//2):
  dspl[rd(z,w-1)][rd(z,h-1)]=1
for a in range(w):
  for b in range(h):
    if dspl[a][b]!=z:
      fr(a*m+sw,b*m+sh,m,m,g)
x,y,t=0,0,0.1
gr,w=(0,255,0),(255,)*3
dc=[w,g]
while True:
 x,y=x+kd(3)-kd(0),y+kd(2)-kd(1)
 fr(x*m+sw,y*m+sh,m,m,gr),sl(t)
# fr(x*m+sw,y*m+sh,m,m,dc[dspl[x][y]])
