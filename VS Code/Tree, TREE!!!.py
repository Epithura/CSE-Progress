from collections import defaultdict

def kawaii_tree(n, k, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    subtree = [0] * (n + 1)
    good = [0] * (n + 1)
    ans = [0] * (n + 1)

    # ----- Iterative DFS1 -----
    stack = [(1, -1, 0)]  # (node, parent, state)
    order = []             # store order for postprocessing
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            stack.append((u, p, 1))
            for v in adj[u]:
                if v != p:
                    stack.append((v, u, 0))
        else:
            size = 1
            for v in adj[u]:
                if v != p:
                    size += subtree[v]
            subtree[u] = size
            good[u] = 1 if size - 1 >= k - 1 else 0
            order.append(u)

    ans[1] = sum(good[1:])

    # ----- Iterative DFS2 (rerooting) -----
    stack = [(1, -1)]
    while stack:
        u, p = stack.pop()
        for v in adj[u]:
            if v == p:
                continue
            old_su, old_sv = subtree[u], subtree[v]
            old_gu, old_gv = good[u], good[v]
            old_ansu = ans[u]

            subtree[u] = n - old_sv
            subtree[v] = n
            good[u] = 1 if subtree[u] - 1 >= k - 1 else 0
            good[v] = 1 if subtree[v] - 1 >= k - 1 else 0
            ans[v] = ans[u] - old_gu - old_gv + good[u] + good[v]

            stack.append((v, u))

            # restore values (for correctness when returning to siblings)
            subtree[u], subtree[v] = old_su, old_sv
            good[u], good[v] = old_gu, old_gv
            ans[u] = old_ansu

    return sum(ans[1:])
t = int(input())
Final = []
for i in range(t):
    n, k = map(int, input().split())
    edges = []
    for j in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    Final.append(kawaii_tree(n, k, edges))
for ans in Final:
    print(ans)