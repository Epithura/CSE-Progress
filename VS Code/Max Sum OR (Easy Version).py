import math
"""
def MaximiseORbit(n):
    A=[]
    if n==0:
        return [0]
    if math.log2(n+1)==math.floor(math.log2(n+1)):
        for i in range(n+1):
            A.append(i)
        return A
    else:
        for i in range(2**(math.floor(math.log2(n))+1)-n-1,n+1):
            A.append(i)
    return A+MaximiseORbit(2**(math.floor(math.log2(n))+1)-n-2)
"""
def MaximiseORbitGen(n):
    if n == 0:
        yield 0
        return
    if math.log2(n+1) == math.floor(math.log2(n+1)):
        for i in range(n+1):
            yield i
        return
    else:
        start = 2**(math.floor(math.log2(n))+1) - n - 1
        for i in range(start, n+1):
            yield i
    # recursive call: yield from next part
    next_n = 2**(math.floor(math.log2(n))+1) - n - 2
    yield from MaximiseORbitGen(next_n)
def SumORBit(n):
    sum=0
    if n==0:
        return 0
    else:
        sum+=2*(n+1-2**(math.floor(math.log2(n))))*(2**(math.floor(math.log2(n))+1)-1)
    if math.log2(n+1)!=math.floor(math.log2(n+1)):
        return sum+SumORBit(2**(math.floor(math.log2(n))+1)-n-2)
    else:
        return sum
t=int(input(""))
for i in range(t):
    l,r=map(int,input().split())
    print(SumORBit(r))
    arr=list(MaximiseORbitGen(r))
    arr.reverse()
    print(*arr)