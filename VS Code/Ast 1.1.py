import math as muth
x,y,z=map(int,input().split())
V=x*y*z
Sn=int(V/8)
SA=2*(x*y+y*z+z*x)
sA=Sn*24
Q=sA-SA
print(V,Sn,Q)   