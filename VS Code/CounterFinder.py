# efficient_counterexample_finder.py
from collections import deque
from itertools import combinations, product

def has_three_consecutive(mask, n):
    for r in range(n):
        for c in range(n-2):
            if (r,c) in mask and (r,c+1) in mask and (r,c+2) in mask:
                return True
    for c in range(n):
        for r in range(n-2):
            if (r,c) in mask and (r+1,c) in mask and (r+2,c) in mask:
                return True
    return False

def is_connected(mask, n):
    if not mask:
        return False
    start = next(iter(mask))
    q = deque([start])
    seen = {start}
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        r,c = q.popleft()
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and (nr,nc) in mask and (nr,nc) not in seen:
                seen.add((nr,nc))
                q.append((nr,nc))
    return len(seen) == len(mask)

def user_rule_initial(blacks):
    # blacks: iterable of (r,c)
    blacks = list(blacks)
    if not blacks or len(blacks) == 1:
        return True
    for i in range(len(blacks)):
        for j in range(i+1, len(blacks)):
            a = abs(blacks[i][0] - blacks[j][0])
            b = abs(blacks[i][1] - blacks[j][1])
            if not (a == b or a == b - 1 or a == b + 1):
                return False
    return True

def find_counterexample(max_n=5):
    # search n = 2..max_n
    for n in range(2, max_n+1):
        coords = [(r,c) for r in range(n) for c in range(n)]
        # iterate initial sets up to some small size (1..min(5,n*n))
        max_initial_size = min(6, n*n)
        for k in range(1, max_initial_size+1):
            for comb in combinations(coords, k):
                initial = set(comb)
                # skip trivial already invalid (initial already contains 3-in-row)
                if has_three_consecutive(initial, n):
                    continue
                # if initial already connected and valid, skip (not a counterexample)
                if initial and is_connected(initial, n):
                    continue
                # If user's rule already accepts this initial, it's not a counterexample (we want cases where user's rule says NO).
                if user_rule_initial(initial):
                    continue

                # BFS over supersets by adding only orthogonally adjacent cells (pruning search)
                q = deque([frozenset(initial)])
                seen = {frozenset(initial)}
                found_valid = False
                while q:
                    cur = set(q.popleft())
                    # check if cur is a valid final config
                    if cur and is_connected(cur, n) and not has_three_consecutive(cur, n):
                        # A valid completion exists, but user_rule_initial(initial) was False => counterexample
                        return {
                            'n': n,
                            'initial': initial,
                            'completion': cur
                        }
                    # generate possible cells to add: neighbors of current black component
                    neighbors = set()
                    for (r,c) in cur:
                        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc = r+dr, c+dc
                            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in cur:
                                neighbors.add((nr,nc))
                    # also consider adding any existing isolated black's neighbors (to connect components)
                    # try adding one neighbor at a time (monotone)
                    for cell in neighbors:
                        nxt = frozenset(cur | {cell})
                        if nxt in seen: continue
                        if has_three_consecutive(nxt, n):
                            continue
                        seen.add(nxt)
                        q.append(nxt)
    return None

if __name__ == "__main__":
    res = find_counterexample(max_n=5)
    if not res:
        print("No counterexample found for n up to 5 with search heuristics.")
    else:
        n = res['n']
        init = res['initial']
        comp = res['completion']
        print("Found counterexample on {}x{} grid".format(n,n))
        print("Initial black coordinates (0-based):", sorted(init))
        print("A valid completion (one possible) coordinates:", sorted(comp))
        # print grids
        def print_grid(mask):
            g = [['.' for _ in range(n)] for __ in range(n)]
            for (r,c) in mask:
                g[r][c] = '#'
            print("\n".join("".join(row) for row in g))
        print("\nInitial grid:")
        print_grid(init)
        print("\nCompleted grid:")
        print_grid(comp)
