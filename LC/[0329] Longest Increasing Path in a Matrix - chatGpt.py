from functools import cache
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        @cache
        def dfs(row: int, col: int) -> int:
            longest = 1

            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc

                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and matrix[next_row][next_col] > matrix[row][col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(next_row, next_col),
                    )

            return longest

        return max(
            dfs(row, col)
            for row in range(rows)
            for col in range(cols)
        )