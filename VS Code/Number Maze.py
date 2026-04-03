def getPermutation(n,k):
        Fact=[1]
        Q=[i+1 for i in range(n)]
        for i in range(1,n):
            Fact.append(Fact[-1]*(i+1))
        L=[]
        C=0
        i=1
        while k>1:
            count=0
            while k>C+Fact[-i-1]:
                C+=Fact[-i-1]
                count+=1
            L.append(Q[count])
            Q.pop(count)
            k-=C
            C=0
            i+=1
        L.extend(Q)
        if k==0:
            L[-1],L[-2]=L[-2],L[-1]
        return ''.join(str(x) for x in L)
t=int(input(""))
for i in range(t):
    n,j,k=map(int,input().split())
    J=getPermutation(len(str(n)),j)
    K=getPermutation(len(str(n)),k)
    A=0
    for i in range(len(str(n))):
         if J[i]==K[i]:
              A+=1
    print(f"{A}A{len(str(n))-A}B")