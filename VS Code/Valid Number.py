def isNumber(s: str):
    i=0
    check=True
    if s[0]=="-" or s[0]=="+":
        i+=1
    if s[0]=="e" or s[0]=="E":
        return False
    if i<len(s) and s[i]==".":
        i+=1
        check=False
    if len(s)<=i:
        return False
    while i<len(s):
        if check and s[i]==".":
            i+=1
            check=False
        elif (s[i] in "eE") and i > 0 and s[i-1].isdigit() and i+1 < len(s) and (s[i+1].isdigit() or s[i+1] in "+-"):
            i += 2
        elif s[i].isdigit():
            i+=1
        else:
            return False
    return True
print(isNumber(input("")))