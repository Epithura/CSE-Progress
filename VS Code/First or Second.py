t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    A=0          
    B=a[0]       
    for i in range(1,n):
        x=a[i]
        A_new=max(B,A-x)
        B_new=B+abs(x)
        A,B=A_new,B_new
    print(A)