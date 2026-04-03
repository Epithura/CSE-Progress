from collections import deque
def Odd_Process(arr):
    evens=[]
    odds=[]
    for i in range(len(arr)):
        if arr[i]%2:
            odds.append(arr[i])
        else:
            evens.append(arr[i])
    Final=[]
    evens.sort()
    odds.sort()
    Evens=deque(evens)
    Odds=deque(odds)
    if not Odds:
        Final=[0]*len(arr)
        return Final
    if not Evens:
        for i in range(len(arr)):
            if i%2:
                Final.append(0)
            else:
                Final.append(Odds[-1])
        return Final
    Final.append(Odds[-1])
    for i in range(len(Evens)):
        Final.append(Evens[-1-i]+Final[-1])
    max=Final[-1]
    while len(Odds)>2:
        Odds.popleft()
        Odds.popleft()
        Final.append(Final[-2])
    if len(Odds)==2:
        Final.append(0)
        return Final
    elif len(Final)<len(arr):
        Final.append(max)
    return Final
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(*Odd_Process(L))