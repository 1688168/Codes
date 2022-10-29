class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M=len(heights)
        if M==0: return []
        N=len(heights[0])
        atlantic=[[0]*N for _ in range(M)]
        pacific=[[0]*N for _ in range(M)]

        dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(xx, yy, visited):
            visited[xx][yy]=1

            for dx, dy in dirs:
                nx, ny=xx+dx, yy+dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
                if visited[nx][ny]==1: continue
                if heights[nx][ny] < heights[xx][yy]: continue

                dfs(nx, ny, visited)

        # DFS Pacific
        for ii in range(N):
            dfs(0, ii, pacific)

        for ii in range(1, M):
            dfs(ii, 0, pacific)

        # DFS Atlantic
        for ii in range(M-1):
            dfs(ii, N-1, atlantic)

        for ii in range(N):
            dfs(M-1, ii, atlantic)

        res=[]
        for ii in range(M):
            for jj in range(N):
                if atlantic[ii][jj]==1 and pacific[ii][jj]==1:
                    res.append((ii, jj))
        return res

        
