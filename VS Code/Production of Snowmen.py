def Count(a, b):
    n=len(a)
    cnt=0
    for shift in range(n):
        Rise=False
        for i in range(n):
            if a[(i+shift)%n]>=b[i]:
                Rise=True
                break
        if Rise:
            cnt+=1
    return cnt
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=list(map(int,input().split()))
    print(n*(n-Count(A,B))*(n-Count(B,C)))