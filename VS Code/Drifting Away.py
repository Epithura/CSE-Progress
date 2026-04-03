def Drifting_Away(s):
    Loops=["><",">*","*<","**"]
    for i in range(len(s)-1):
        if s[i]+s[i+1] in Loops:
            return -1
    a=0
    b=0
    for i in range(len(s)):
        if s[i]=="<":
            a+=1
        elif s[i]==">":
            b+=1
        else:
            a+=1
            b+=1
    return max(a,b)
t=int(input(""))
for i in range(t):
    s=str(input(""))
    print(Drifting_Away(s))