from math import log,ceil
def GetP3(n):
    powers=[]
    p=1
    while p<=n:
        powers.append(p)
        p*=3
    powers.reverse()
    result=[]
    for p in powers:
        while n>=p:
            result.append(p)
            n-=p
    return result
def Price(x):
    return ceil(log(x,3))*(x/3)+3*x
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=GetP3(n)
    num=0
    for i in range(len(L)):
        num+=Price(L[i])
    print(int(num))