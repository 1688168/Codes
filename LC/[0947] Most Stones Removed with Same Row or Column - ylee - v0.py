class DSU:
    def __init__(self):
        self.parents = dict()
        self.node2size = dict()

    def union(self, aa, bb):
        pa = self.find(aa)
        pb = self.find(bb)

        if pa == pb:
            return

        # Union by size: attach smaller component to larger
        if self.node2size[pa] < self.node2size[pb]:
            pa, pb = pb, pa

        self.parents[pb] = pa
        self.node2size[pa] += self.node2size[pb]

    def find(self, xx):
        # Lazy initialization for new nodes
        if xx not in self.parents:
            self.parents[xx] = xx
            self.node2size[xx] = 1

        # Path compression
        if xx != self.parents[xx]:
            self.parents[xx] = self.find(self.parents[xx])

        return self.parents[xx]


class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        N = len(stones)
        dsu = DSU()

        def is_connected(aa, bb):
            return (stones[aa][0] == stones[bb][0] or
                    stones[aa][1] == stones[bb][1])

        # Compare every pair of stones
        for ii in range(N):
            for jj in range(ii + 1, N):
                if is_connected(ii, jj):
                    dsu.union(ii, jj)

        # find() also initializes isolated stones that were never unioned.
        # Each isolated stone counts as its own connected component.
        components = len({dsu.find(x) for x in range(N)})

        # Each component of size k allows removing k-1 stones.
        return N - components