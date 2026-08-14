class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # we will traverse the matrix and dfs for the longest increasing path
        
        memo = dict()
        m=len(matrix)
        n=len(matrix[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(ii, jj):
            if (ii, jj) in memo: return memo[(ii, jj)]
            ans =1
            for dx, dy in directions:
                nx, ny = ii+dx, jj+dy
                if nx < 0 or nx >= m or ny < 0 or ny >=n: continue
                if matrix[nx][ny] <= matrix[ii][jj]: continue
                ans = max(ans, 1+dfs(nx, ny))

            memo[(ii, jj)] = ans
            return ans
        
        res=0
        for ii in range(m):
            for jj in range(n):
                res = max(res, dfs(ii, jj))

        return res
        


        