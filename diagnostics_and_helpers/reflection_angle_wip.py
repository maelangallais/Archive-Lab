#Cree le 02 Avril 2024

def rebond(ri,si):
  def nearer(ri,n1,n2):
    if n1>=n2:b,c=n1,n2
    else:b,c=n2,n1
    m=(b+c)/2
    if ri>=m+180:ri-=180
    elif ri<=m-180:ri+=180
    r=b if ri>=m else c
    return r
  #Les deux angle de normale
  n1,n2=si-90,si+90
  n1=n1+360 if n1<0 else n1-360 if n1>359 else n1
  n2=n2+360 if n2<0 else n2-360 if n2>359 else n2
  #Lequel est le plus pres pour l"utiliser
  n=nearer(ri,n1,n2)
  #Calcul de l"angle de reflection
  ar=n+(n-ri) if n>=ri else n-(ri-n)
  ar=ar-360 if ar>359 else ar+360 if ar<0 else ar
  return ar

print(rebond(60,00))
