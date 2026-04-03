def preprocess(a):
    n = len(a)
    bad = [0] * n   
    for i in range(n-2):
        if a[i] > a[i+2]:
            bad[i] = 1
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + bad[i]
    return prefix
def query(prefix, l, r):
    l -= 1
    r -= 1
    if r - l + 1 < 3:
        return "YES"   
    if prefix[r-1] - prefix[l] > 0:
        return "NO"
    return "YES"
t=int(input(""))
for i in range(t):
    n,q=map(int,input().split())
    L=list(map(int,input().split()))
    Prep=preprocess(L)
    for j in range(q):
        l,r=map(int,input().split())
        print(query(Prep,l,r))