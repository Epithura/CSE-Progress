def Rabbits(s):
    unit=[]
    j=1
    while j<len(s)/2:
        U=[0,1]*j
        if s[:2*j]==U:
            j+=1
            unit=U
        else:
            break
    if unit and unit.count(0)%2==0:
        for i in range(0,len(unit)//4):
            unit[4*i]="R"
            unit[2*i+2]="L"
    elif unit and unit.count(0)%2!=0:
            unit[4*i]="L"
            unit[2*i+2]="R"
    i=0
    while i<len(s):
        if s[i]==0:
            if i>0 and s[i-1]==0:
                s[i]="L"
                s[i-1]="R"
            elif i>1 and s[i-2]==0:
                s[i]="L"
                s[i-2]="R"
            elif i<len(s)-1 and s[i+1]==0:
                s[i]="R"
                s[i+1]="L"
            elif i<len(s)-2 and s[i+2]==0:
                s[i]="R"
                s[i+2]="L"
            elif i==0:
                s[i]="L"
            elif i==len(s)-1:
                s[i]="R"
        i+=1
    print(s)
    if (0 in s):
        return "NO"
    return "YES"
t = int(input())
Final = []
for _ in range(t):
    n = int(input())
    s_input = input()
    digits = [int(d) for d in s_input]
    Final.append(Rabbits(digits))
for ans in Final:
    print(ans)
