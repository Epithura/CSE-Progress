L=[]
x=int(input("Enter Degree of Polynomial"))
for i in range(x+1):
    c=input("")
    L.append(c)
def Derivative(D):
    ODegree=D.keys()
    OValue=D.values()
    DerivativeDegree=len(ODegree)-2
    n=DerivativeDegree
    D1={}
    for i in range(n):
        D1[i]=(i+1)*OValue[n-i]
    return D1
