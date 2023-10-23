class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        # 1 prep
        m, n = len(grid), len(grid[0])
        row_mins, col_mins = [1]*m, [1]*n

        # 2 sorting
        aux = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        aux.sort()

        # 3. resetting
        for i in range(m*n):
            _, r, c = aux[i]
            grid[r][c] = max(row_mins[r], col_mins[c])
            row_mins[r] = grid[r][c] + 1
            col_mins[c] = grid[r][c] + 1

        # 4 return the res
        return grid
