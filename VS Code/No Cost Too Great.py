from math import gcd
def No_Cost_Too_Great(a):
    GCD=1
    P=1
    for i in range(len(a)):
        P*=a[i]
    for i in range(len(a)):
        GCD=max(GCD,gcd(P//a[i],a[i]))
        if GCD>1:
            return 0
    P=1
    for i in range(len(a)):
        P*=a[i]+1
    for i in range(len(a)):
        GCD=max(GCD,gcd(P//(a[i]+1),a[i]))
        if GCD>1:
            return 1
    return 2
t=int(input("")) 
Final=[]
for i in range(t):
    n=int(input(""))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    Final.append(No_Cost_Too_Great(a))
for ans in Final:
    print(ans)