#Créé le 13 Octobre 2025

from kandinsky import fill_rect as fr

c=[(255,0,0),(0,255,0),(0,0,255),(255,0,255)]

for x in range(320):
  xt=x/320
  for y in range(222):
    yt=y/222
    color=[(c[0][i]*(1-xt)+c[1][i]*xt)*(1-yt)+(c[2][i]*(1-xt)+c[3][i]*xt)*yt for i in range(3)]
    fr(x,y,1,1,color)
