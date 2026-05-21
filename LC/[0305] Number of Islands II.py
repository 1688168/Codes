class DSU:
    def __init__(self, m, n):
        self.parent = {}
        self.size = {}
        self.count = 0
        self.m = m
        self.n = n

    def get_gid(self, r, c):
        return r * self.n + c

    def is_existing(self, gid):
        return gid in self.parent

    def add(self, gid):
        self.parent[gid] = gid
        self.size[gid] = 1
        self.count += 1

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return

        # Union by size: attach smaller component under larger component.
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU(m, n)
        answer = []

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in positions:
            gid = dsu.get_gid(r, c)

            # Duplicate position: island count does not change.
            # positions could have duplicates, when problem didn't say all unique, it could have duplicates
            if dsu.is_existing(gid):
                answer.append(dsu.count)
                continue

            # New land starts as its own island.
            dsu.add(gid)

            # Merge with existing neighboring land cells.
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                ngid = dsu.get_gid(nr, nc)

                if not dsu.is_existing(ngid):
                    continue

                dsu.union(gid, ngid)

            answer.append(dsu.count)

        return answer