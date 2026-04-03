def AS(a, n, k):
    appended = []
    used = set(a)

    start = None
    for i in range(1, n+1):
        if i not in used:
            start = i
            break

    tail_safe = start

    if start is None and len(a) >= 2 and a[-1] == a[-2]:

        for i in range(1, n+1):
            if i != a[-1]:
                tail_safe = i
                break

    elif start is None:

        tail_safe = a[-3] if len(a) >= 3 else a[-1]
    current = tail_safe
    for _ in range(k):
        if current==a[-1]:
            current+=1
            if current>n:
                current=1
        appended.append(current)
        current += 1
        if current > n:
            current = 1
        if len(appended) >= 2 and appended[-1] == appended[-2]:
            current += 1
            if current > n:
                current = 1

    return appended


t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    Final.append(AS(a,n,k))
for ans in Final:
    print(*ans)