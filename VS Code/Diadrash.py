import sys
def interactive_solution():
    data = sys.stdin.readline().strip().split()
    if not data:
        return
    t = int(data[0])
    for _ in range(t):
        while True:
            parts = sys.stdin.readline().strip().split()
            if parts:
                break
        n = int(parts[0]); q = int(parts[1])
        ranges = [None] * q
        for i in range(q):
            li, ri = map(int, sys.stdin.readline().strip().split())
            ranges[i] = (li, ri)
        queries_done = 0
        query_limit = max(300, (n // 2) + 2)

        def query(l, r):
            nonlocal queries_done
            if not (1 <= l <= r <= n):
                print(f"# Invalid query attempted: {l} {r}", file=sys.stderr)
                sys.stdout.flush()
                sys.exit(1)
            queries_done += 1
            if queries_done > query_limit:
                print(f"# Query limit exceeded ({queries_done} > {query_limit})", file=sys.stderr)
                sys.stdout.flush()
                sys.exit(1)
            print(f"? {l} {r}", flush=True)
            resp_line = sys.stdin.readline().strip()
            if resp_line == "":
                print("# No response from judge", file=sys.stderr)
                sys.stdout.flush()
                sys.exit(1)
            try:
                resp = int(resp_line)
            except:
                print("# Non-integer response from judge:", resp_line, file=sys.stderr)
                sys.stdout.flush()
                sys.exit(1)
            return resp
        def answer(x):
            print(f"! {x}", flush=True)
        L, R = 1, n
        while L < R:
            mid = (L + R) // 2
            mex = query(L, mid)
            if mex > 0:
                R = mid
            else:
                L = mid + 1
        k = L
        mex_left = query(1, k)
        mex_right = query(k, n)
        if mex_right >= mex_left:
            target_mex = mex_right
            lo, hi = k, n
            best_r = n
            while lo <= hi:
                mid = (lo + hi) // 2
                mex = query(k, mid)
                if mex == target_mex:
                    best_r = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            Lopt, Ropt = k, best_r
        else:
            target_mex = mex_left
            lo, hi = 1, k
            best_l = 1
            while lo <= hi:
                mid = (lo + hi) // 2
                mex = query(mid, k)
                if mex == target_mex:
                    best_l = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            Lopt, Ropt = best_l, k
        best_idx = -1
        best_overlap = -1
        for idx, (li, ri) in enumerate(ranges):
            if li <= k <= ri:
                overlap = max(0, min(ri, Ropt) - max(li, Lopt) + 1)
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_idx = idx
        if best_idx == -1:
            for idx, (li, ri) in enumerate(ranges):
                overlap = max(0, min(ri, Ropt) - max(li, Lopt) + 1)
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_idx = idx
        answer(target_mex)
if __name__ == "__main__":
    interactive_solution()
