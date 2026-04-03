def visit(p,N):
    if N==0:
        return 1
    elif N<0:
        return 0
    else:
        y=p*visit(p,N-1)+(1-p)*visit(p,N-2)
        return y
p=float(input(""))
if p<0 or p>1:
    print("INVALID INPUT")
else:
    n=input("")
    if n.isdigit():  
       print(visit(p,int(n)))  
    else:
        print("INVALID INPUT")



    