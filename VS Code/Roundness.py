def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
INPUT=input("")
List=[char for char in INPUT]
if List[len(List)-1]=="!":
    List.remove("!")
    x=fact(int("".join(map(str, List))))
else:    
    x=int(INPUT)
a=x
def NZero(l):
    count=0
    for num in reversed(l):
        if num==0:
            count+=1
        else:
            break
    return count              
R=0
for i in range(2,x+1):
    L=[]
    while x>0:
        r=x%i
        L.insert(0,r)
        x=x//i
    R+=NZero(L)
    x=a
print(R)