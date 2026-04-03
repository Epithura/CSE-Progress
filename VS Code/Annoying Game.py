from collections import deque
def Annoying_Game(arr,b,k):
    def Kadane(arr):
        B=float("-inf")
        C=0
        start=end=0
        Temp=0
        for i, x in enumerate(arr):
            C+=x
            if C>B:
                B=C
                start=Temp
                end=i
            if C<0:
                C=0
                Temp=i+1
        return B,start,end
    if k%2==0:
        A=Kadane(arr)
        return A[0]
    else:
        P=[0]
        S=deque([0])
        for i in range(1,len(arr)):
            P.append(max(P[-1]+arr[i-1],0))
            S.appendleft(max(S[0]+arr[-i],0))
        L=[]
        for i in range(len(arr)):
            L.append(arr[i]+b[i]+max(0,P[i])+max(0,S[i]))
        return max(L)
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    b=list(map(int,input().split()))
    Final.append(Annoying_Game(arr,b,k))
for ans in Final:
    print(ans)