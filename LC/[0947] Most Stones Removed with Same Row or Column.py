class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()

        for x, y in stones:
            row_id = ("row", x)
            col_id = ("col", y)
            dsu.union(row_id, col_id)

        roots = set()
        for x, y in stones:
            roots.add(dsu.find(("row", x)))

        return len(stones) - len(roots)

# ## Strategy
# * Treat each row and each column as DSU nodes:
#   row node = ('row', x), column node = ('col', y)
# * A stone at (x, y) connects row x and column y, so union(('row', x), ('col', y)).
# * If another stone shares the same row or column, it will connect through the same row/col node.
# * Therefore, each connected component represents one group of stones.
# * In each group, we can remove all stones except one.
# * Answer = total stones - number of connected components.