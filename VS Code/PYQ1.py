L=[]
L1=[]
L2=[]
LDash=[]
x=int(input(""))
if x%2==0:
    for i in range(x):
        a=input("")
        L.append(a)
    for j in range(0,int(x/2)):
        L1.append(L[j])
        L2.append(L[int(x/2) + j])
    for k in range(0,int(x/2)):
        LDash.append(L1[k])
        LDash.append(L2[k])
    print(LDash)
else:
    print("INVALID LENGTH OF LIST")