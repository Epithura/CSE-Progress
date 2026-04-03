import heapq
def Slay(n, m, a, b, c):
    swords = list(a)
    heapq.heapify(swords)
    pos = sorted((b[i], c[i]) for i in range(m) if c[i] > 0)
    zero = sorted(b[i] for i in range(m) if c[i] == 0)
    ans = 0
    weak_swords=[]
    for life, reward in pos:
        while swords and swords[0] < life:
            Weaks=heapq.heappop(swords)
            weak_swords.append(Weaks)
        if not swords:
            continue
        s = heapq.heappop(swords)
        ans += 1
        if reward > 0:
            heapq.heappush(swords, max(s, reward))
    while weak_swords:
        W=weak_swords.pop()
        heapq.heappush(swords,W)
    for life in zero:
        while swords and swords[0] < life:
            heapq.heappop(swords)
        if not swords:
            continue
        heapq.heappop(swords)
        ans += 1
    return ans
t=int(input(""))
Final=[]
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    Final.append(Slay(n,m,a,b,c))
for ans in Final:
    print(ans)