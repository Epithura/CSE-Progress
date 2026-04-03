t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a % 2 == 0:
        if b % 2 == 0:
            print(a*b//2 + 2)
        else:
            print(-1)
    else:
        if b % 2 == 0:
            if (b//2) % 2 == 0:
                print(a*b//2 + 2)
            else:
                print(-1)
        else:
            print(a*b + 1)
