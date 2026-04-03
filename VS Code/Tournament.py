x = int(input())
results = []
for i in range(x):
    m, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if k>1 or max(arr) == arr[j - 1]:
        results.append("Yes")
    else:
        results.append("No")
for res in results:
    print(res)
