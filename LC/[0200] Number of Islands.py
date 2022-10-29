class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[(1,0), (-1,0), (0, 1), (0, -1)]

        M=len(grid)
        if M==0: return 0
        N=len(grid[0])

        def isValid(x, y):
            if x < 0 or y < 0 or x >= M or y >= N:
                return False # out of bound
            if grid[x][y] == '2' or grid[x][y]=='0': return False #visited or water

            return True

        cnt=0

        def dfs(xx, yy):
            if not isValid(xx, yy):
                return

            grid[xx][yy]='2'

            for dx, dy in dirs:
                nx, ny=xx+dx, yy+dy
                if not isValid(nx, ny): continue
                dfs(nx, ny)


        for ii in range(M):
            for jj in range(N):
                if grid[ii][jj]=='1':
                    cnt += 1
                    dfs(ii, jj)

        return cnt
