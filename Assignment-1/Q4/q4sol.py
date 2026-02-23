class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)   # 4*n is safe for segment tree
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, l, r):
        if l == r:
            self.tree[node] = data[l]
        else:
            mid = (l + r) // 2
            self._build(data, node*2, l, mid)
            self._build(data, node*2+1, mid+1, r)
            self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])

    def update(self, pos, value):
        self._update(1, 0, self.n - 1, pos, value)

    def _update(self, node, l, r, pos, value):
        if l == r:
            self.tree[node] = value
        else:
            mid = (l + r) // 2
            if pos <= mid:
                self._update(node*2, l, mid, pos, value)
            else:
                self._update(node*2+1, mid+1, r, pos, value)
            self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])

    def query_max(self, L, R):
        return self._query(1, 0, self.n - 1, L, R)

    def _query(self, node, l, r, L, R):
        if L > r or R < l:
            return float('-inf')
        if L <= l and r <= R:
            return self.tree[node]
        mid = (l + r) // 2
        left_max = self._query(node*2, l, mid, L, R)
        right_max = self._query(node*2+1, mid+1, r, L, R)
        return max(left_max, right_max)
