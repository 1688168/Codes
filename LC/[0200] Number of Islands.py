##########
# 20231008
##########
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        M = len(grid)
        N = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(ii, jj):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return
            vv = grid[ii][jj]
            if vv == '2' or vv == "0":
                return
            grid[ii][jj] = '2'
            for di, dj in dirs:
                ni, nj = ii+di, jj+dj
                dfs(ni, nj)

        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == '1':
                    cnt += 1
                    dfs(ii, jj)
        return cnt


##########
# 20230916
##########
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - traverse all grid: Time: O(M*N)
        - for each '1' encountered: dfs and mark visited
        """
        M = len(grid)
        N = len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        count = 0

        def dfs(ii, jj):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return
            if (ii, jj) in visited:
                return
            visited.add((ii, jj))
            curr = grid[ii][jj]
            if curr == '0':
                return
            for dx, dy in dirs:
                dfs(ii+dx, jj+dy)

        for ii in range(M):
            for jj in range(N):
                curr = grid[ii][jj]
                if curr == '1' and (ii, jj) not in visited:
                    count += 1
                    dfs(ii, jj)

        return count

##################################


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])

        def isValid(x, y):
            if x < 0 or y < 0 or x >= M or y >= N:
                return False  # out of bound
            if grid[x][y] == '2' or grid[x][y] == '0':
                return False  # visited or water

            return True

        cnt = 0

        def dfs(xx, yy):
            if not isValid(xx, yy):
                return

            grid[xx][yy] = '2'

            for dx, dy in dirs:
                nx, ny = xx+dx, yy+dy
                if not isValid(nx, ny):
                    continue
                dfs(nx, ny)

        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj] == '1':
                    cnt += 1
                    dfs(ii, jj)

        return cnt
