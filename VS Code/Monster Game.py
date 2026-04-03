from collections import defaultdict
import bisect
def floor_pos(arr,target):
    i=bisect.bisect_right(arr,target)
    if i==0:
        return -1
    return i
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A.sort()
    alpha=list(set(A))
    alpha.sort()
    D={}
    Dc=defaultdict(int)
    for i in range(len(A)):
        Dc[A[i]]+=1
    net=len(A)
    D[alpha[0]]=net
    for i in range(1,len(alpha)):
        D[alpha[i]]=D[alpha[i-1]]-Dc[alpha[i-1]]
    Pref=[0]*n
    Pref[0]=B[0]
    for i in range(1,n):
        Pref[i]=Pref[i-1]+B[i]
    Lam=[]
    for i in range(len(alpha)):
        Lam.append(alpha[i]*floor_pos(Pref,D[alpha[i]]))
    print(max(Lam))