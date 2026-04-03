from math import gcd,lcm
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    a=list(map(int,input("").split()))
    b=list(map(int,input("").split()))
    count=0
    for i in range(1,n-1):
        left=gcd(a[i],a[i-1])
        right=gcd(a[i],a[i+1])
        if lcm(left,right)<a[i]:
            count+=1
    if gcd(a[0],a[1])!=a[0]:
        count+=1
    if gcd(a[n-1],a[n-2])!=a[n-1]:
        count+=1
    print(count)