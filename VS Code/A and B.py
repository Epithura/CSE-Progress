def AorB(L):
    if len(L)%2:
        pos=len(L)//2
        steps=0
        k=1
        for i in range(pos):
            steps+=L[pos]-L[i]-k
            k+=1
        k=1
        for i in range(pos+1,len(L)):
            steps+=L[i]-L[pos]-k
            k+=1
        return steps
    else:
        pos1=len(L)//2
        pos2=len(L)//2-1
        steps1=0
        k=1
        for i in range(pos1):
            steps1+=L[pos1]-L[i]-k
            k+=1
        k=1
        for i in range(pos1+1,len(L)):
            steps1+=L[i]-L[pos1]-k
            k+=1
        steps2=0
        k=1
        for i in range(pos2):
            steps2+=L[pos2]-L[i]-k
            k+=1
        k=1
        for i in range(pos2+1,len(L)):
            steps2+=L[i]-L[pos2]-k
            k+=1
        return min(steps1,steps2)
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    s=str(input(""))
    A=[]
    B=[]
    for i in range(len(s)):
        if s[i]=="a":
            A.append(i+1)
        else:
            B.append(i+1)
    print(min(AorB(A),AorB(B)))