class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])

        dq = collections.deque([[0, 0, 0]])
        memo = set()
        while dq:  # the exit condition for BFS - iteration
            ii, jj, cnt = dq.popleft()

            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                continue

            # update cnt at current cell
            cnt += (1 if grid[ii][jj] == 1 else -1)

            if (ii, jj, cnt) in memo:
                continue  # how to use memo in BFS, if visited, no need to add children

            if ii == M-1 and jj == N-1 and cnt == 0:
                return True

            dq.append((ii+1, jj, cnt))
            dq.append((ii, jj+1, cnt))
            memo.add((ii, jj, cnt))

        return False
