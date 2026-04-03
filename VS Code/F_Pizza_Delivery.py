import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n, ax, ay, bx, by = map(int,input().split())

    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))

    pts = list(zip(xs,ys))
    pts.append((bx,by))

    pts.sort()

    cols = []
    i = 0
    m = len(pts)

    while i < m:
        x = pts[i][0]
        low = high = pts[i][1]

        while i < m and pts[i][0] == x:
            y = pts[i][1]
            low = min(low,y)
            high = max(high,y)
            i += 1

        cols.append((x,low,high))

    prev_x = ax
    prev_low = prev_high = ay
    dp_low = dp_high = 0

    for x,low,high in cols:

        dx = x - prev_x
        span = high - low

        new_low = min(
            dp_low + dx + abs(prev_low-high) + span,
            dp_high + dx + abs(prev_high-high) + span
        )

        new_high = min(
            dp_low + dx + abs(prev_low-low) + span,
            dp_high + dx + abs(prev_high-low) + span
        )

        prev_x = x
        prev_low = low
        prev_high = high
        dp_low = new_low
        dp_high = new_high

    print(min(
        dp_low + abs(prev_low-by),
        dp_high + abs(prev_high-by)
    ))