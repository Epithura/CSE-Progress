t=int(input(""))
Final=[]
for i in range(t):
    x=(input(""))
    L=[int(digits) for digits in x]
    y=min(L)
    Final.append(y)
for ans in Final:
    print(ans)