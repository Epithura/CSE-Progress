from collections import deque
def Cake_Assignment(k,x):
    Chocola=x
    Vanilla=(2**(k+1))-x
    L=deque()
    larger=max(Chocola,Vanilla)
    while Chocola!=Vanilla:
        if Chocola==larger:
            Vanilla+=Vanilla
            Chocola-=(Vanilla//2)
            larger=max(Chocola,Vanilla)
            L.appendleft(2)
        else:
            Chocola+=Chocola
            Vanilla-=(Chocola//2)
            larger=max(Chocola,Vanilla)
            L.appendleft(1)
    print(len(L))
    print(*L)
t=int(input(""))
for i in range(t):
    k,x=map(int,input().split())
    Cake_Assignment(k,x)