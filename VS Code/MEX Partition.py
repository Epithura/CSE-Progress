def mex(arr):
    s=set(arr)
    n=len(arr)
    for i in range(n+1):
        if i not in s:
            return i
def Score(arr):
    if 0 in set(arr):
        return mex(arr)
    else:
        return 0
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(Score(L))
    