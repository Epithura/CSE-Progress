import math as muth
p,q=map(int,input().split())
x=p/q
a=int(x)
b=x-int(x)
e=(muth.floor(b*100))/100
print(a,f"{e:.2f}")