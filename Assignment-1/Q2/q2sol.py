from collections import deque

class SlidingWindowMax:
    def __init__(self, k):
        self.k = k
        self.dq = deque()      # stores indices
        self.stream = []       # stores all values (optional, for value lookup)

    def add(self, value):
        idx = len(self.stream)   # current index
        self.stream.append(value)

        # 1. Remove smaller values from the back
        while self.dq and self.stream[self.dq[-1]] <= value:
            self.dq.pop()

        # 2. Add new index
        self.dq.append(idx)

        # 3. Remove expired indices from the front
        if self.dq[0] <= idx - self.k:
            self.dq.popleft()

        # 4. Current maximum
        return self.stream[self.dq[0]]

# Usage
k = 3
window = SlidingWindowMax(k)
latencies = [5, 2, 8, 6, 1, 9, 3]
for lat in latencies:
    max_val = window.add(lat)
    print(f"Window {window.stream[-window.k:] if len(window.stream)>=window.k else window.stream} -> max = {max_val}")
