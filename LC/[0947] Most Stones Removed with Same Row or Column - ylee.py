class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.BASE = 10001
        
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        # Union by size: make pa the root of the larger component.
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        # Attach smaller component root pb under larger component root pa.
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]

    def find(self, x):
        # Lazily initialize unseen node.
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

        # Path compression.
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
    
        return self.parent[x]
    
    def get_gid(self, x, y):
        # Unique stone ID. BASE must be greater than max possible y.
        return self.BASE * x + y


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()

        ROW_OFFSET = 1_000_000_000
        COL_OFFSET = 2_000_000_000

        for x, y in stones:
            stone_gid = dsu.get_gid(x, y)

            # Unique row-group node for row x.
            row_gid = -ROW_OFFSET - x

            # Unique column-group node for column y.
            col_gid = -COL_OFFSET - y

            # This stone belongs to its row group and column group.
            dsu.union(stone_gid, row_gid)
            dsu.union(stone_gid, col_gid)

        # Count connected components among actual stones only.
        roots = set()
        for x, y in stones:
            roots.add(dsu.find(dsu.get_gid(x, y)))

        return len(stones) - len(roots)