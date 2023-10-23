class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        0. build graph
        1. dfs the find path
        2. bfs find the shortest distance
        """
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        def dfs(a, b, path):
            # print(f"====> a=[{a}], b=[{b}]")
            if a == b:
                path.append(a)
                for n in path:
                    path_nodes.add(n)
                return True
            if a in visited:
                return False
            visited.add(a)

            for c in g[a]:
                if dfs(c, b, path+[a]):
                    return True
            visited.remove(a)

            return False

        def bfs(n,  path_nodes):
            dq = collections.deque([n])

            while (sz := len(dq)) > 0:
                found = False
                for _ in range(sz):
                    curr = dq.popleft()
                    if curr in path_nodes:
                        res.append(curr)
                        found = True
                        break
                    for c in g[curr]:
                        dq.append(c)
                if found:
                    break

        res = []
        for a, b, n in query:
            path_nodes = set()
            path = []
            visited = set()

            dfs(a, b, path)

            bfs(n, path_nodes)

        return res
