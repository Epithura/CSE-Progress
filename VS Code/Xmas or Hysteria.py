t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if m==1 or m>n//2:
        print(-1)
        continue
    elves=[(a[i],i) for i in range(n)]
    elves.sort()
    ops=[]
    if m==0:
        for i in range(n-1):
            ops.append((elves[i][1]+1,elves[i+1][1]+1))
        print(len(ops))
        for x,y in ops:
            print(x,y)
        continue
    for i in range(m):
        ops.append((elves[n-1-i][1]+1,elves[i][1]+1))
    print(len(ops))
    for x,y in ops:
        print(x,y)
