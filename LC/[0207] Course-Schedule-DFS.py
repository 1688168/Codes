from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        check if has cycle
        """
        g = defaultdict(set)
        for a, b in prerequisites:
            g[b].add(a)

        visited = {}

        def has_cycle_dfs(curr):
            """
            return True if has cycle
                False otherwise
            :param curr:
            :return:
            """
            if curr in visited and visited[curr] == 1:
                return False
            if curr in visited and visited[curr] == 2:
                return True  # has cycle

            visited[curr] = 2
            for child in g[curr]:
                if has_cycle_dfs(child):
                    return True
            visited[curr] = 1

            return False

        for ii in range(numCourses):
            if has_cycle_dfs(ii):
                return False

        return True
