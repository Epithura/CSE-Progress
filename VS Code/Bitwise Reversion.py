def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary
def bitwise_and_binary(B1, B2):
    return ''.join(str(b1 & b2) for b1, b2 in zip(B1, B2))
def if_BitwiseAND(x,y,z):
    Bx=decimal_to_binary(x)
    By=decimal_to_binary(y)
    Bz=decimal_to_binary(z)
    max_len = max(len(Bx), len(By), len(Bz))
    Bx = Bx.zfill(max_len)
    By = By.zfill(max_len)
    Bz = Bz.zfill(max_len)
    L=[Bx,By,Bz]
    a=[0]*max_len
    b=a[:]
    c=a[:]
    for i in range(max_len):
        if Bx[i]=="1":
            a[i]=1
            b[i]=1
        if By[i]=="1":
            b[i]=1
            c[i]=1
        if Bz[i]=="1":
            c[i]=1
            a[i]=1
    if bitwise_and_binary(a,b)==Bx and bitwise_and_binary(b,c)==By and bitwise_and_binary(a,c)==Bz:
        return "YES"
    return "NO"
t=int(input(""))
for i in range(t):
    x,y,z=map(int,input().split())
    print(if_BitwiseAND(x,y,z))