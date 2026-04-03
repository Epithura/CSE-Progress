def Acons(B):
    n=len(B)
    A=[1]*len(B)
    j=2
    for i in range(0,n-1):
        if i+1+B[i]-B[i+1]<0:
            A[i+1]=j
            j+=1
        else:
            A[i+1]=A[i+1+B[i]-B[i+1]]
    return A
Final=[]
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Final.append(Acons(L))
for ans in Final:
    print(*ans)