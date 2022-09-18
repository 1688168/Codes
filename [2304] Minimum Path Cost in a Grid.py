from functools import lru_cache
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        """
        * last row move cost can be ignored
        * distinct integers
        * min cost of a pth reaching last row
        """

        M=len(grid)
        N=len(grid[0])

        # check edge cases:


        @lru_cache(None)
        def dfs(rn, jj): #row num
            # base cases
            if rn==M-1:
                return grid[rn][jj]

            if rn==0:
                return min([grid[rn][ii]+moveCost[grid[rn][ii]][jj]+dfs(rn+1 , jj) for ii in range(N) for jj in range(N)])
            else:
                return min([grid[rn][jj]+moveCost[grid[rn][jj]][ii]+dfs(rn+1,  ii) for ii in range(N)])

        return dfs(0, 0)
