from math import gcd
n=int(input(""))
L=list(map(int,input().split()))
prefix=[L[0]]
suffix=[L[-1]]
M=0
for i in range(1,n):
    prefix.append(gcd(prefix[-1],L[i]))
    suffix.append(gcd(suffix[-1],L[-i-1]))
for i in range(1,n):
    M+=min(prefix[i],suffix[-1-i])
print(M)