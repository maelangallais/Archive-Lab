#Cree le 9 Mai 2024
from math import cos,sin,radians,floor,ceil
from kandinsky import fill_rect as fr
from time import sleep as sl

projectile=[[0,0,0,0,0,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,2,2,2,2,2,2,1,1],[1,1,1,1,2,2,2,2,2,2,2,2,2,2,1],[0,0,1,1,1,1,1,2,2,2,2,2,2,1,1],[0,0,0,0,0,0,1,1,1,1,1,1,1,1,0]]
col=[[(0,0,255),(0,0,150)],[(255,0,0),(150,0,0)]]

def draw_b(x, y, t=2, d=0, cl=0, l=projectile):
  rad=radians(360-d%360)
  px,py=cos(rad),sin(rad)
  cols,rows=len(l[0]),len(l)
  hw,hh=(cols*t)/2,(rows*t)/2
  palette=col[cl]
  # Bounding box des 4 coins centrés sur (0, 0)
  corners=((-hw,-hh),(hw,-hh),(-hw,hh),(hw,hh))
  xs=[cx*px-cy*py for cx,cy in corners]
  ys=[cx*py+cy*px for cx,cy in corners]
  min_x,max_x=floor(min(xs)),ceil(max(xs))
  min_y,max_y=floor(min(ys)),ceil(max(ys))
  for dy in range(min_y,max_y+1):
    run_col,run_start=0,min_x
    for dx in range(min_x,max_x+1):
      #Debug line:fr(x+dx,y+dy,1,1,(0,255,0))
      sx,sy=dx*px+dy*py+hw,-dx*py+dy*px+hh
      ix,iy=floor(sx/t),floor(sy/t)
      val=l[iy][ix]if(0<=ix<cols and 0<=iy<rows)else 0
      if val!=run_col:
        if run_col!=0:fr(x+run_start,y+dy,dx-run_start,1,palette[run_col-1])
        run_col,run_start=val,dx
    if run_col!=0:fr(x+run_start,y+dy,max_x+1-run_start,1,palette[run_col-1])

for i in range(91):
  fr(0,0,320,222,(255,)*3)
  draw_b(160,111,5,i)
  sl(0.01)

