from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n)) # whenever you know the num of nodes, use array is. easier.
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        # Attach the smaller group to the larger group
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


class Solution:
    def distanceLimitedPathsExist(
        self,
        n: int,
        edgeList: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        edgeList.sort(key=lambda edge: edge[2])

        # Sort query indices so we can preserve the original answer order.
        query_order = sorted(
            range(len(queries)),
            key=lambda index: queries[index][2],
        )

        dsu = DSU(n)
        answers = [False] * len(queries)
        edge_index = 0

        for query_index in query_order:
            p, q, limit = queries[query_index]

            # Add every newly eligible edge.
            while (
                edge_index < len(edgeList)
                and edgeList[edge_index][2] < limit
            ):
                u, v, weight = edgeList[edge_index]
                dsu.union(u, v)
                edge_index += 1

            answers[query_index] = dsu.find(p) == dsu.find(q)

        return answers