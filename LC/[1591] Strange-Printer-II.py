from collections import defaultdict


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        """
        1. find color range
        - color2Range={colorID: (left, right, top, bottom)}
        2. find color order
        - build graph, top color as parent, others as children
        3. check cycle
        """
        color2Range = {}
        M = len(targetGrid)
        N = len(targetGrid[0])

        # define range
        for ii in range(M):
            for jj in range(N):
                color = targetGrid[ii][jj]
                if color not in color2Range:
                    color2Range[color] = (N, 0, M, 0)
                color2Range[color] = (min(color2Range[color][0], jj),
                                      max(color2Range[color][1], jj),
                                      min(color2Range[color][2], ii),
                                      max(color2Range[color][3], ii)
                                      )

        # define color order via building graph
        g = defaultdict(set)
        for ii in range(M):
            for jj in range(N):

                for color in range(1, 61):
                    if color not in color2Range:
                        continue
                    if jj < color2Range[color][0] or  \
                       jj > color2Range[color][1] or  \
                       ii < color2Range[color][2] or  \
                       ii > color2Range[color][3]:
                        continue

                    if color != targetGrid[ii][jj]:
                        g[targetGrid[ii][jj]].add(color)

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

        for color in range(1, 61):
            if color not in color2Range:
                continue
            if has_cycle_dfs(color):
                return False

        return True
