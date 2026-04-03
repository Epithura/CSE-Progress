import math as meth
a,b,c=map(float,input().split())
x,y,z=map(float,input().split())
def distance(x1,y1,z1,x2,y2,z2):
    dx=x2-x1
    dy=y2-y1
    dz=z2-z1
    d=meth.sqrt(dx*dx+dy*dy+dz*dz)
    return d
print(f"{distance(a,b,c,x,y,z):.2f}")