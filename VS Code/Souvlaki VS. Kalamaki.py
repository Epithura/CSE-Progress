t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    L.sort()
    A=False
    for i in range(n-1):
        if i%2!=0:
            if not L[i]==L[i+1]:
                print("NO")
                A=True
                break
    if not A:
        print("YES")