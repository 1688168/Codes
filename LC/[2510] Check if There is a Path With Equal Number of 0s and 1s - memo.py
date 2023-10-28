#############
# 20231028
#############
class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        """
        - DFS with memo
        - right and down only
        """
        ans = False
        M = len(grid)
        N = len(grid[0])
        memo = set()

        def dfs(ii, jj, cnt):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False

            inc = (1 if grid[ii][jj] == 1 else -1)
            cnt += inc

            if (ii, jj, cnt) in memo:
                return False  # notice where we check the memo, we are checking after cnt is updated
            if ii == M-1 and jj == N-1:
                if cnt == 0:
                    return True
                else:
                    memo.add((ii, jj, cnt))
                    return False

            if dfs(ii+1, jj, cnt) or dfs(ii, jj+1, cnt):
                return True

            memo.add((ii, jj, cnt))
            return False

        ans = dfs(0, 0, 0)

        return ans

################################


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])

        # total number of 0's and 1's is odd. Balance can't be achieved
        if (M+N-1) % 2 == 1:
            return False

        memo = {}
        # @cache

        def dfs(ii, jj, c):
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False

            if grid[ii][jj] == 0:
                c -= 1
            else:
                c += 1

            if (ii, jj, c) in memo:
                return memo[(ii, jj, c)]

            if ii == M-1 and jj == N-1:
                return c == 0

            # unbalance went too far and cannot be fixed with remaining steps
            if M+N-ii-jj-2 < abs(c):
                return False

            dirs = [(1, 0), (0, 1)]
            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if dfs(nx, ny, c):
                    return True

            # memo[(ii, jj, c)] = dfs(ii+1, jj, c) or dfs(ii, jj+1, c)
            memo[(ii, jj, c)] = False
            return memo[(ii, jj, c)]

        return dfs(0, 0, 0)
