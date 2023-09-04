from collections import defaultdict


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        # define equality
        def is_equal(a, b):
            return abs(a-b) < 1e-5

        g = defaultdict(set)

        # build the relation in g
        for (n1, n2), f in zip(equations, values):
            if n1 == n2:
                if not is_equal(f, 1):
                    return True
                continue

            g[n1].add((n2, f))
            g[n2].add((n1, 1/f))

        # set first node with value = 1
        node2val = {}

        def dfs(curr):
            for nb, f in g[curr]:
                if nb in node2val:
                    if not is_equal(node2val[curr]/node2val[nb], f):
                        return True
                else:
                    node2val[nb] = node2val[curr]/f
                    if dfs(nb):
                        return True

            return False

        for n in g:  # check each nodes
            if n not in node2val:
                node2val[n] = 1
            if dfs(n):
                return True

        return False
