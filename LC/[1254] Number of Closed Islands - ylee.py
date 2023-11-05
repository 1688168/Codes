class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        visited = set()

        def dfs(ii, jj):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False, 0
            if grid[ii][jj] == 1:
                return True, 0
            if (ii, jj) in visited:
                return True, 0
            visited.add((ii, jj))

            v1, c1 = dfs(ii+1, jj)
            v2, c2 = dfs(ii-1, jj)
            v3, c3 = dfs(ii, jj+1)
            v4, c4 = dfs(ii, jj-1)
            if v1 and v2 and v3 and v4:
                return True, 1
            return False, 0

        cnt = 0
        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == 0:
                    is_valid, nn = dfs(ii, jj)
                    if is_valid:
                        cnt += nn

        return cnt
