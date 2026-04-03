t=int(input(""))
for _ in range(t):
    n=int(input(""))
    X=str(input(""))
    A=["a"]*n
    for i in range(1,n,2):
        A[i]="b"
    Bool=True
    j=n-1
    i=0
    while j+1>i:
        if A[i]==X[i+n-j-1]:
            i+=1
        elif A[j]==X[i+n-j-1]:
            j-=1
        elif X[i+n-j-1]=="?":
            if A[i]==A[j]:
                i+=1
            else:
                if X[i+n-j]==A[i] or X[i+n-j]=="?":
                    j-=1
                elif X[i+n-j]==A[j] or X[i+n-j]=="?":
                    i+=1
        else:
            Bool=False
            break
    print("YES" if Bool else "NO")