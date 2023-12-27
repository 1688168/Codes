###########
# 20231105
###########

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        dfs all nodes from the border and set to zero
        add all 1s form all rows, all cols
        """

        M = len(grid)
        N = len(grid[0])

        def dfs(ii, jj):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return
            if grid[ii][jj] == 0:
                return

            grid[ii][jj] = 0

            dfs(ii+1, jj)
            dfs(ii-1, jj)
            dfs(ii, jj+1)
            dfs(ii, jj-1)

        for ii in range(M):
            for jj in range(N):
                if ii == 0 or jj == 0 or ii == M-1 or jj == N-1:  # only dfs border cells
                    if grid[ii][jj] == 0:
                        continue
                    dfs(ii, jj)

        return sum([sum(grid[ii]) for ii in range(M)])


"""
# Strategy:
1. visit edge cells and dfs all 1 cells and reset all to zero
2. the remaining 1s are inner 1s so we can just sum all of them to get the ttl count

"""


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)
