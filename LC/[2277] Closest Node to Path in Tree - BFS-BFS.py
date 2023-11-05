"""
1. path from start to end
2. BFS from target_node
"""


class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # step-0 build graph
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        res = []
        # BFS to determine the path

        def get_path_bfs(st, ed):
            dq = collections.deque([(st, [st])])
            visited = set()
            while (sz := len(dq)) > 0:
                for _ in range(sz):
                    curr, path = dq.popleft()
                    if curr == ed:
                        return path
                    visited.add(curr)
                    for child in g[curr]:
                        if child not in visited:
                            dq.append((child, path+[child]))
            return []

        for a, b, n in query:
            path_set = set(get_path_bfs(a, b))
            found = False
            dq = collections.deque([n])
            visited = set()
            while (sz := len(dq)) > 0:
                for _ in range(sz):
                    curr = dq.popleft()
                    if curr in path_set:
                        res.append(curr)
                        found = True
                        break

                    visited.add(curr)
                    for child in g[curr]:
                        if child not in visited:
                            dq.append(child)

                if found:
                    break

        return res
