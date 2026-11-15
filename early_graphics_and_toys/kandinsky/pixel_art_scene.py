#Créé le 21 Mai 2023
from kandinsky import fill_rect
from turtle import *

fill_rect(0,0,320,2,(255,181,59))
l,ble,rou,ve,ja,ma,no,bla,ros,ora,vi,gr=20,'blue','red','green','yellow','brown','black','white','pink','orange','purple','gray'
image=[[ja,ja,ja,ble,bla,bla,bla,bla,bla,ble,ble,bla,bla,bla,bla,bla],
      [ja,ja,ble,ble,ble,bla,bla,bla,ble,ble,ble,ble,ble,bla,bla,bla],
      [ja,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble],
      [ble,ble,rou,bla,rou,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble],
      [ble,rou,bla,rou,bla,rou,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble],
      [rou,bla,rou,bla,rou,bla,rou,ble,ble,ble,ble,ble,ble,ble,ble,ble],
      [ble,ble,ble,no,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble,ble],
      [ja,ja,ja,no,ja,ja,ja,ja,ja,ja,ja,ja,ja,ja,ja,ja],
      [ja,ja,ja,no,ja,ja,ja,ja,ja,ora,ve,ora,ve,ora,ja,ja],
      [ja,ja,ja,no,ja,ja,ja,ja,ja,ve,ora,ve,ora,ve,ja,ja],
      [ja,ja,ja,ja,ja,ja,ja,ja,ja,ora,ve,ora,ve,ora,ja,ja]]
for a in range(16):
  for b in range(11):
    fill_rect(a*l,b*l+2,l,l,image[b][a])
