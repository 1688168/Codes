class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        def overlap(a, b):
            return a[0] <= b[1] and b[0] <= a[1]

        # Union every pair of overlapping intervals
        for i in range(n):
            for j in range(i + 1, n):
                if overlap(intervals[i], intervals[j]):
                    union(i, j)

        groups = {}

        # Group intervals by connected component
        for i, (s, e) in enumerate(intervals):
            root = find(i)
            if root not in groups:
                groups[root] = [s, e]
            else:
                groups[root][0] = min(groups[root][0], s)
                groups[root][1] = max(groups[root][1], e)

        return sorted(groups.values())