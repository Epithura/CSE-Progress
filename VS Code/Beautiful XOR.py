def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))
def binary_to_decimal(b):
    decimal = 0
    for digit in b:
        decimal = decimal * 2 + int(digit)
    return decimal
def AtoB(a,b):
    if a==b:
        return 0
    sa=decimal_to_binary(a)
    sb=decimal_to_binary(b)
    if len(sa)<len(sb):
        return -1
    L=[]
    for char in sa:
        if char!="1":
            L.append(1)
        else:
            L.append(0)
    N1=binary_to_decimal(''.join(str(x) for x in L))
    L=[1]*(len(sa)-len(sb))
    for char in sb:
        if char=="0":
            L.append(1)
        else:
            L.append(0)
    N2=binary_to_decimal(''.join(str(x) for x in L))
    return (N1,N2)
t=int(input(""))
for i in range(t):
    a,b=map(int,input().split())
    Ans=AtoB(a,b)
    if type(Ans)!=int:
        print(2)
        print(*[Ans[0],Ans[1]])
    else:
        print(Ans)
