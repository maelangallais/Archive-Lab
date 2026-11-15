#Créé le 17 Juin 2024
from kandinsky import *

tp=[
[4, 9, 0], [2, 7, 2], [1, 6, 1], [3, 4, 2], [5, 2, 1], [6, 3, 2], [8, 5, 1], [6, 7, 2], [4, 9, 1]
]

c1,c2=(0,85,66),(231,227,206)
n,wh=(54,21,31),(223,175,121)
re,gr,bl=(255,0,0),(48,246,49),(0,0,255)
s=22

for a in range(10):
  for b in range(10):
    if (20-a+b)%2==1:fill_rect(a*s,b*s,s,s,c1)
    else:fill_rect(a*s,b*s,s,s,c2)

color=[n,bl,re]
for i,[vx,vy,ch] in enumerate(tp):
  fill_rect(vx*s,vy*s,s,s,color[ch])
  draw_string(str(i),vx*s,vy*s)
