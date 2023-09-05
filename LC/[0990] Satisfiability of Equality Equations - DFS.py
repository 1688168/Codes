from collections import defaultdict


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        g = defaultdict(set)

        def dfs(src, des):
            if src == des:
                return True
            if src in visited:
                return False
            visited.add(src)
            for child in g[src]:
                if dfs(child, des):
                    return True

            return False

        for exp in equations:
            if exp[1] != '=':
                continue
            a, b = exp[0], exp[3]
            g[a].add(b)
            g[b].add(a)

        # print(" g: ", g)

        for exp in equations:
            if exp[1] == '=':
                continue
            a, b = exp[0], exp[3]
            visited = set()
            if dfs(a, b):
                return False

        return True
