from collections import defaultdict
def catch_herobrine(n, edges):
    tree = defaultdict(list)
    for u, v in edges:
        u -= 1  
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
    removed = [False]*n
    ops = []
    def component_nodes(u, parent):
        nodes = [u]
        for v in tree[u]:
            if v != parent and not removed[v]:
                nodes.extend(component_nodes(v, u))
        return nodes
    def decompose(u):
        nodes = component_nodes(u, -1)
        if len(nodes) == 1:
            ops.append((1, nodes[0]+1))
            removed[nodes[0]] = True
            return
        elif len(nodes) == 2:
            for node in nodes:
                ops.append((1, node+1))
                removed[node] = True
            return
        size = [0]*n
        def dfs_size(u, parent):
            size[u] = 1
            for v in tree[u]:
                if v != parent and not removed[v]:
                    dfs_size(v, u)
                    size[u] += size[v]

        def find_centroid(u, parent, total_size):
            for v in tree[u]:
                if v != parent and not removed[v] and size[v] > total_size // 2:
                    return find_centroid(v, u, total_size)
            return u
        dfs_size(u, -1)
        c = find_centroid(u, -1, size[u])
        ops.append((1, c+1))
        if any(not removed[v] for v in tree[c]):
            ops.append((2, c+1))
        removed[c] = True
        for v in tree[c]:
            if not removed[v]:
                decompose(v)
    decompose(0)
    return ops
t = int(input())
for _ in range(t):
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    ops = catch_herobrine(n, edges)
    print(len(ops))
    for t_i, x_i in ops:
        print(t_i, x_i)