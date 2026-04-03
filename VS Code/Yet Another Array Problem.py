import math
def minx(arr):
    primes=[2 ,3 ,5 ,7 ,11 ,13 ,17 ,19 ,23 ,29 ,31 ,37 ,41 ,43 ,47 ,53]
    x=54
    for i in range(len(arr)):
        for j in range(16):
            if math.gcd(arr[i],primes[j])==1:
                if primes[j]<x:
                    x=primes[j]
                break
    return x
q=int(input(""))
for i in range(q):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(minx(L))
