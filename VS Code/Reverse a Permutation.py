def rev(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    i=0
    while i<len(L) and L[i]==n-i:
        i+=1
    if i==len(L):
        print(*L)
    else:
        pos=0
        while pos<len(L) and L[pos]!=n-i:
            pos+=1
        Left=i
        Right=pos
        rev(L,Left,Right)
        print(*L)