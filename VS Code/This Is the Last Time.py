import heapq
def find_max_profit(n, k, casinos):
    coins=k
    old_coins=-1
    PL=[(casinos[i][2],(casinos[i][0],casinos[i][1])) for i in range(n)]
    heapq.heapify(PL)
    while PL:
        a=heapq.heappop(PL)
        if a[1][0]<=coins<=a[1][1] and coins<a[0]:
            coins=a[0]
    return coins
t = int(input())
Final=[]
for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for _ in range(n)]
    Final.append(find_max_profit(n, k, casinos))
for ans in Final:
    print(ans)