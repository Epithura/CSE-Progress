t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    I=L.index(max(L))
    Cost=0
    for i in range(I,len(L)-1):
        Cost+=max(L[i],L[i+1])
    for i in range(I):
        Cost+=max(L[i-1],L[i])
    print(Cost)