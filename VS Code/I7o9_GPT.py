def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ops = []

        # We'll lock columns 0..k-1 after step k.
        for k in range(n):
            target_lo = k + 1          # we want this in a[k]
            target_hi = n + k + 1      # we want this in b[k]

            # --- bring target_lo into a[k] ---
            # find it:
            pos = -1
            row = 1
            for j in range(k, n):
                if a[j] == target_lo:
                    pos = j
                    row = 1
                    break
                if b[j] == target_lo:
                    pos = j
                    row = 2
                    break

            if row == 2:
                # vertical swap at pos
                ops.append((3, pos + 1))
                a[pos], b[pos] = b[pos], a[pos]

            # now it's in a[pos], bubble left to a[k]
            while pos > k:
                # swap a[pos-1] <-> a[pos]
                ops.append((1, pos))
                a[pos], a[pos-1] = a[pos-1], a[pos]
                pos -= 1

            # --- bring target_hi into b[k] ---
            # find it:
            pos = -1
            row = 1
            for j in range(k, n):
                if b[j] == target_hi:
                    pos = j
                    row = 2
                    break
                if a[j] == target_hi:
                    pos = j
                    row = 1
                    break

            if row == 2:
                # it's already in b[pos], bubble it left to b[k]
                while pos > k:
                    ops.append((2, pos))
                    b[pos], b[pos-1] = b[pos-1], b[pos]
                    pos -= 1
            else:
                # in a[pos], first bubble in a down to k+1
                while pos > k+1:
                    ops.append((1, pos))
                    a[pos], a[pos-1] = a[pos-1], a[pos]
                    pos -= 1
                # now at a[k+1], swap down to b[k+1]
                ops.append((3, k+2))
                a[k+1], b[k+1] = b[k+1], a[k+1]
                # bubble that from b[k+1] left to b[k]
                ops.append((2, k+1))
                b[k+1], b[k] = b[k], b[k+1]

            # now (a[k], b[k]) == (k+1, n+k+1) and column k is locked

        # done!
        print(len(ops))
        for t, i in ops:
            print(t, i)
