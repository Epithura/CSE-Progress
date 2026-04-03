from math import log
def Renako_Amaori(a,b): #a-Ajisai,b-Mai;Ajisai-odd,Mai-even
    if (a.count(1)+b.count(1))%2==0:
        return "Tie"
    i=1
    j=1
    while j<=len(a):
        if a[j-1]!=b[j-1]:
            i=j
        j+=1
    if i%2==0:
        return "Mai"
    return "Ajisai"
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    alpha=max(a)
    beta=max(b)
    Q=max(alpha,beta)
    if Q==0:
        print("Tie")
    else:
        bits=Q.bit_length()
        A=[]
        B=[]
        for x in a:
            A.append((x>>(bits-1))&1)
        for x in b:
            B.append((x>>(bits-1))&1)
        Conc=Renako_Amaori(A,B)
        while Conc=="Tie" and bits>1:
            bits-=1
            A=[]
            B=[]
            for x in a:
                A.append((x>>(bits-1))&1)
            for x in b:
                B.append((x>>(bits-1))&1)
            Conc=Renako_Amaori(A,B)
        print(Conc)