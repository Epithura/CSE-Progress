from collections import defaultdict
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    D=defaultdict(int)
    for j in range(n):
        D[L[j]]+=1
    L1=list(D.values())
    L1.sort(reverse=True)
    max_sum = 0
    for i, x in enumerate(L1):
        value = x * (i + 1)
        if value > max_sum:
            max_sum = value
    Final.append(max_sum)
for ans in Final:
    print(ans)