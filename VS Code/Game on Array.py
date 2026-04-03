from collections import Counter
import sys
input = sys.stdin.readline
def ScoreBoard(arr):
    freq = Counter(arr)
    L = sorted(freq.items(), key=lambda x: x[1])
    Bob = Alice = 0
    chance = "Beta"
    while L:
        key, count = L.pop()  
        base = count * (key // 2)  
        Alice += base
        Bob += base
        if key % 2 == 1:  
            if chance == "Alpha":
                Alice += count
                chance = "Beta"
            else:
                Bob += count
                chance = "Alpha"
    return [Bob, Alice]
t = int(input())
out=[]
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    b,a = ScoreBoard(L)
    out.append(f"{b} {a}")
print("\n".join(out))