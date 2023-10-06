##########
# 20231005
##########
from collections import defaultdict


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        """
        - build a weighted graph
        - start from each node with starting value 1 to check if any contradiction
        """
        g = defaultdict(set)

        def is_equal(a, b):
            return abs(a-b) < 1e-5

        for (a, b), v in zip(equations, values):
            if a == b and not is_equal(v, 1):
                return True
            g[a].add((b, v))
            g[b].add((a, 1/v))

        checked = {}

        def has_contradiction(a):
            """
            a/b=v 
            b=a/v
            """

            for b, v in g[a]:
                if b in checked:
                    if not is_equal(checked[b], checked[a]/v):
                        return True
                else:
                    checked[b] = checked[a]/v
                    if has_contradiction(b):
                        return True

            return False

        for a in g:
            if a not in checked:
                checked[a] = 1
            if has_contradiction(a):
                return True

        return False


########################################


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
