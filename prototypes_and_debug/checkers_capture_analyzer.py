#Créé le 17 Juin 2024
from time import monotonic
jeu=[[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,1,0,6,0],
     [0,0,0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0]]
tp=[]

def ap(x,y,p,r,cj):
 [a1,a2,e1,e2]=[1,2,6,7]if p in[1,2]else[6,7,1,2]
 if p in[1,6]:
  for dx in[-1,1]:
   for dy in[-1,1]:
    px,py=x+dx,y+dy
    if 0<=px<=9 and 0<=py<=9 and cj[py][px]in[e1,e2]:
     nx,ny=x+2*dx,y+2*dy
     if 0<=nx<=9 and 0<=ny<=9 and cj[ny][nx]==0:
      if r==0:tp.append([x,y,0,r])
      tp.append([px,py,2,r+1]),tp.append([nx,ny,1,r+1])
      nj=[row[:]for row in cj]
      nj[py][px],nj[ny][nx],nj[y][x]=0,nj[y][x],0
      ap(nx,ny,p,r+1,nj)
 else:
  for dx in[-1,1]:
   for dy in[-1,1]:
    for n in range(1,10):
     px,py=x+dx*n,y+dy*n
     if not 0<=px<=9 or not 0<=py<=9 or cj[py][px]in[a1,a2]:break
     if cj[py][px]in[e1,e2]:
      for i in range(1,8):
       nx,ny=px+dx*i,py+dy*i
       if not 0<=nx<=9 or not 0<=ny<=9 or cj[ny][nx]!=0:break
       if cj[ny][nx]==0:
        if r==0:tp.append([x,y,0,r])
        tp.append([px,py,2,r+1]),tp.append([nx,ny,1,r+1])
        nj=[row[:]for row in cj]
        nj[py][px],nj[ny][nx],nj[y][x]=0,nj[y][x],0
        ap(nx,ny,p,r+1,nj)
      break

t=monotonic()
for a in range(10):
 for b in range(10):
  if jeu[b][a]in[6,7]:continue
  cj=jeu
  if jeu[b][a]!=0:ap(a,b,jeu[b][a],0,cj)

print("Temps de calcul pour l'analyse : \n"+str(round(monotonic()-t,3)))
#print(tp)
#print(len(tp))

t=monotonic()
np=[]
hv=0
for vx,vy,ch,r in tp:
 if r>hv:hv=r
rep=0
for i,[vx,vy,ch,r] in enumerate(tp):
 if[r,ch]==[hv,1]:
  ok,na,pbf=False,hv,[]
  np.append([])
  for ni,[nx,ny,nc,nr]in enumerate(reversed(tp)):
   if not ok and ni>=len(tp)-1-i and[nx,ny,nc,r]==[vx,vy,ch,r]:ok=True
   if ok and nr==na:
    pbf.append([nx,ny,nc])
    if nc==2:na-=1
    if nr==0:break
  for val in reversed(pbf):
   np[rep].append(val)
  rep+=1

print("Temps de calcul pour l'interprétation : \n"+str(round(monotonic()-t,3)))
print("Voici les "+str(len(np))+" possibilités d'action : ")
for n in np:
  print(n)
