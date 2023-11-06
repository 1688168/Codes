#########
# 20231105
#########
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        """
        (vv, (ii, jj))
        """
        M = len(grid)
        N = len(grid[0])
        grid_list = [(grid[ii][jj], ii, jj)
                     for jj in range(N) for ii in range(M)]

        grid_list.sort()

        row = [0]*M
        col = [0]*N
        for vv, ii, jj in grid_list:
            grid[ii][jj] = max(row[ii], col[jj])+1
            row[ii] = grid[ii][jj]
            col[jj] = grid[ii][jj]

        return grid


##########################
"""
1. start to update from the min cell (that's why we sort for all cells)
2. on each update, we update the max of min_rows, min_cols
3. update min_rows, min_cols be grid[r][c]+1
"""


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        # 1 prep
        m, n = len(grid), len(grid[0])
        row_mins, col_mins = [1]*m, [1]*n

        # 2 sorting
        # so we will start to ulpdate from the smallest cell
        aux = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        aux.sort()

        # 3. resetting
        for i in range(m*n):
            _, r, c = aux[i]
            # after assigning the min valid value for this cell
            grid[r][c] = max(row_mins[r], col_mins[c])
            row_mins[r] = grid[r][c] + 1  # the min valid row value is updated
            col_mins[c] = grid[r][c] + 1  # the min valid col value is updated

        # 4 return the res
        return grid
