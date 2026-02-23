def find_bridges(n, graph):
    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []

    def dfs(u, parent):
        nonlocal time
        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:
            if v == parent:
                continue
            if disc[v] == -1:          # tree edge
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:                       # back edge
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges
