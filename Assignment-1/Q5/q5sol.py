def min_assignment_cost(cost):
    """
    cost: N x N matrix, cost[i][j] = cost of worker i doing task j.
    Returns minimum total assignment cost.
    """
    n = len(cost)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        k = mask.bit_count()          # number of assigned tasks = next worker index
        if k == n:
            continue
        for j in range(n):
            if not (mask >> j) & 1:   # task j is free
                new_mask = mask | (1 << j)
                dp[new_mask] = min(dp[new_mask], dp[mask] + cost[k][j])

    return dp[(1 << n) - 1]
