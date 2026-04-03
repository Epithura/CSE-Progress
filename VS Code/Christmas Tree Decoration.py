from collections import Counter
MOD=998244353
MAXN=2*10**5+5
fact=[1]*MAXN
invfact=[1]*MAXN
for i in range(1,MAXN):fact[i]=fact[i-1]*i%MOD
invfact[MAXN-1]=pow(fact[MAXN-1],MOD-2,MOD)
for i in range(MAXN-2,-1,-1):invfact[i]=invfact[i+1]*(i+1)%MOD
def Final(arr,k):
    freq=Counter(arr)
    keys=sorted(freq)
    zeros=freq.get(0,0)
    t=0
    i=0
    while i<len(keys):
        nxt=keys[i]
        if nxt<=t:
            i+=1
            continue
        gap=nxt-t
        cost=zeros*gap
        if k<cost:
            step=k//zeros
            t+=step
            k-=step*zeros
            break
        k-=cost
        t=nxt
        zeros+=freq[nxt]
        i+=1
    else:
        if zeros:
            step=k//zeros
            t+=step
            k-=step*zeros
    ok=True
    fA=[]
    for x in arr:
        v=x-t
        if v<=0:
            fA.append(0)
        elif v==1:
            fA.append(1)
        else:
            fA.append(v)
            ok=False
    return k,fA,ok
t=int(input())
for _ in range(t):
    n=int(input())
    L=list(map(int,input().split()))
    k=L[0]
    A=L[1:]
    kF,fA,ok=Final(A,k)
    if not ok:
        print(0)
        continue
    c0=fA.count(0)
    c1=len(fA)-c0
    print(fact[c0]*fact[c1+kF]%MOD*invfact[kF]%MOD)