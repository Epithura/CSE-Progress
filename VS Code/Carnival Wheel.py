from collections import defaultdict
def Carnival_Wheel(l,a,b):
    ptr=a
    D=defaultdict(int)
    while not D[ptr]:
        D[ptr]+=1
        ptr=(ptr+b)%l
    L=D.keys()
    return max(L)
t=int(input(""))
for i in range(t):
    l,a,b=map(int,input().split())
    print(Carnival_Wheel(l,a,b))