def solve(arr):
    evens = [x for x in arr if x % 2 == 0]
    if len(evens)>=2:
        return [evens[0], evens[1]]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[j]%arr[i])%2==0:
                return [arr[i],arr[j]]
    return [-1]
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(*solve(L))