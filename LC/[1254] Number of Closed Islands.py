class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        visited = set()

        def dfs(ii, jj):

            if ii < 0 or jj < 0 or ii >= M or jj >= N:
                return 0
            if grid[ii][jj] == 1:
                return 1
            if (ii, jj) in visited:
                return 1  # since we try all 4 directions, one of which will reach edge if not enclosed

            visited.add((ii, jj))
            # we will only return 1 if all 4 directions are 1
            # if we got zero meaning we are not enclosed by 1s
            return min(dfs(ii+1, jj), dfs(ii-1, jj), dfs(ii, jj+1), dfs(ii, jj-1))

        cnt = 0

        for ii in range(1, M-1):
            for jj in range(1, N-1):
                if grid[ii][jj] == 1:
                    continue
                if (ii, jj) in visited:
                    continue
                cnt += dfs(ii, jj)  # we only check 0s

        return cnt

############################


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = {}

        def dfs(ii, jj, kk):

            if ii < 0 or jj < 0 or ii >= M or jj >= N:
                return False
            if grid[ii][jj] == 1:
                return True
            if (ii, jj) in visited and visited[(ii, jj)] == 2:
                return False
            if (ii, jj) in visited and visited[(ii, jj)] == 0:
                return True
            visited[(ii, jj)] = kk

            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if not dfs(nx, ny, kk) and kk == 0:
                    return False

            return True

        # row1
        for jj in range(N):
            if grid[0][jj] == 0:
                dfs(0, jj, 2)

        for jj in range(N):
            if grid[M-1][jj] == 0:
                dfs(M-1, jj, 2)

        for ii in range(M):
            if grid[ii][0] == 0:
                dfs(ii, 0, 2)

        for ii in range(M):
            if grid[ii][N-1] == 0:
                dfs(ii, N-1, 2)

        cnt = 0

        for ii in range(1, M-1):
            for jj in range(1, N-1):
                if grid[ii][jj] == 1:
                    continue
                if (ii, jj) in visited:
                    continue
                if dfs(ii, jj, 0):
                    cnt += 1  # we only check 0s

        return cnt
