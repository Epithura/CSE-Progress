t=int(input())
N=10**12
for i in range(t):
    x,y,k=map(int,input().split())
    if y==1:
        print(-1)
    else:
        for j in range(x):
            k=k+(k-1)//(y-1)
        if k>N:
            print(-1)
        else:
            print(k)
