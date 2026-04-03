s=str(input(""))
S=s.lower()
L=[str(INPUT) for INPUT in S]
List=[]
for i in range (len(L)):
    if L[i].isalpha() or L[i].isdigit():
        List.append(L[i])
n=len(List)
if n%2==0:
    if all(List[i]==List[n-1-i] for i in range ((n//2))):
        print("True")
    else:
        print("False")
else:
    if all(List[i]==List[n-1-i] for i in range (((n-1)//2))):
        print("True")
    else:
        print("False")