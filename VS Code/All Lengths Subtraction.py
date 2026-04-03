t=int(input(""))
for i in range(t):
    n=int(input(""))
    Arr=list(map(int,input().split()))
    pos=Arr.index(max(Arr))
    A1=Arr[:pos+1]
    A2=Arr[pos:]
    Q=A1[:]
    P=A2[:]
    A1.sort()
    A2.sort(reverse=True)
    if Q==A1 and P==A2:
        print("YES")
    else:
        print("NO")