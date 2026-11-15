#Créé le 15 Novembre 2023
from ion import keydown
from time import monotonic,sleep

print("Appuyez sur 'EXE' pour commencer.")
sleep(0.5)
ok=True
click=True
start=True
to=52 #52 = EXE, 4 = OK
du=1

while ok:
  while start:
    r=0
    ti=monotonic()
    if keydown(to):start=False
  if click:
    if keydown(to):
      r+=1
      click=False
  if not keydown(to):click=True
  if monotonic()-ti>du:
    print(" ")
    if r>=2:print("Nombre de clics total :");print(r)
    print("Nombre de clics par seconde :")
    print(r//du)
    start=True
    sleep(2)
