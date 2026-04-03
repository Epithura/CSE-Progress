def mod_insertion_sort(arr,k):
    L=[]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            L.append(j+1)
        

        arr[j + 1] = key
    Q=[]
    for q in range(len(L)):
        Q.append([k,L[q]+1])
    return Q
t=int(input(""))
X=[]
Y=[]
for i in range(t):
    n=int(input(""))
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    X.append(A)
    Y.append(B)
for i in range(t):
    a=mod_insertion_sort(X[i],1)
    b=mod_insertion_sort(Y[i],2)
    Q=[]
    for j in range(len(X[i])):
        if X[i][j]>Y[i][j]:
            Q.append([3,j+1])
    print(len(a)+len(b)+len(Q))
    for pair in a:
        print(*pair)
    for pair in b:
        print(*pair)
    for pair in Q:
        print(*pair)