class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])

        @cache
        def dfs(ii, jj, z, o):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False

            if grid[ii][jj] == 0:
                z += 1
            else:
                o += 1
            if ii == M-1 and jj == N-1:
                if z == o:
                    return True
            dirs = [(1, 0), (0, 1)]
            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if dfs(nx, ny, z, o):
                    return True

            return False

        return dfs(0, 0, 0, 0)
