class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra = find(a)
            rb = find(b)

            if ra == rb:
                return False

            # attach smaller component under larger component
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

            return True

        for a, b in edges:
            if a not in parent:
                parent[a] = a
                size[a] = 1
            if b not in parent:
                parent[b] = b
                size[b] = 1

            if not union(a, b):
                return [a, b]

        return []