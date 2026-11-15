#Créé le 4 Octobre 2023
from kandinsky import *
from ion import *

def get_pixel_quantifier(color):
  facteur1=31/255
  facteur2=63/255
  r=round(round(color[0]*facteur1)/facteur1)
  g=round(round(color[1]*facteur2)/facteur2)
  b=round(round(color[2]*facteur1)/facteur1)
  return (r,g,b)

r,g,b=0,0,0
new=True
while True:
  if new:
    new=False
    fill_rect(0,0,320,162,(r,g,b))
    fill_rect(250,162,70,60,(255,255,255))
    draw_string(str(r),260,162,(255,0,0))
    draw_string(str(g),260,182,(0,255,0))
    draw_string(str(b),260,202,(0,0,255))
    for i in range(25):
      fill_rect(i*10,162,10,20,(i*10,g,b))
    for i in range(25):
      fill_rect(i*10,182,10,20,(r,i*10,b))
    for i in range(25):
      fill_rect(i*10,202,10,20,(r,g,i*10))
    draw_string(str(get_pixel_quantifier((r,g,b))),0,0)

  if keydown(KEY_TOOLBOX):
    if r>0:r-=1
    else:r=255
    new=True
  elif keydown(KEY_BACKSPACE):
    if r<255:r+=1
    else:r=0
    new=True
  if keydown(KEY_COMMA):
    if g>0:g-=1
    else:g=255
    new=True
  elif keydown(KEY_POWER):
    if g<255:g+=1
    else:g=0
    new=True
  if keydown(KEY_SQRT):
    if b>0:b-=1
    else:b=255
    new=True
  elif keydown(KEY_SQUARE):
    if b<255:b+=1
    else:b=0
    new=True
  
