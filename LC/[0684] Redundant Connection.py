class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            if pa < pb:
                parent[pb] = pa
            else:
                parent[pa] = pb

            return True

        for a, b in edges:
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b

            if not union(a, b):
                return [a, b]

        return []