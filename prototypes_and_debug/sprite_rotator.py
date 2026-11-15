#Cree le 9 Mai 2024
from math import cos,sin,radians,floor,fabs
from kandinsky import fill_rect as fr
from time import sleep as sl

def ent(x):
 if x-floor(x)>.5:return floor(x)+1
 elif x-floor(x)<=.5:return floor(x)
c,s=lambda x:round(cos(radians(x)),2),lambda x:round(sin(radians(x)),2)
projectile=[[0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,2,2,2,2,2,2,1,1],[1,1,1,1,2,2,2,2,2,2,2,2,2,2,1],[0,0,1,1,1,1,1,2,2,2,2,2,2,1,1],[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0]]
col=[[(0,0,255),(0,0,150)],[(255,0,0),(150,0,0)]]

def ls(x,y,t,d,col):
 global c,s
 px,py=c(d),s(d)
 for a in range(t):
  for b in range(t):
   ax,ay=ent(a*px-b*py),ent(a*py+b*px)
   fr(ent(x+ax),ent(y+ay),1,1,col)
def draw(x,y,t,d,col):
 px,py,k=c(d),s(d),t-1
 for a,b in [[0,0],[1,0],[1,1],[0,1]]:
  ax,ay=a*k*px-b*k*py,a*k*py+b*k*px
  ls(x+ax,y+ay,t,d,col)
  d=(d+90)%360

def draw_b(x,y,t=2,d=0,cl=0,l=projectile):
 d,f=360-d%360,draw
 px,py=c(d),s(d)
 for i in range(4):
  if fabs(d-i*90)<7:f=ls
 for a in range(len(l[0])):
  for b in range(len(l)):
   nx,ny=x+a*t*px-b*t*py,y+a*t*py+b*t*px
   if l[b][a]!=0:f(nx,ny,t,d,col[cl][l[b][a]-1])

for i in range(360):
  fr(0,0,320,222,(255,)*3)
  draw_b(160,111,5,i)
  sl(0.01)
