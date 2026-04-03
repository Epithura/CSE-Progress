from itertools import groupby
t=int(input())
for _ in range(t):
    St=input().strip()
    count=0
    if St and St[0]=='u':
        count+=1
        St='s'+St[1:]
    if St and St[-1]=='u':
        count+=1
        St=St[:-1]+'s'
    L=[len(list(g)) for k,g in groupby(St) if k=='u']
    count+=sum(x//2 for x in L)
    print(count)