from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        shortest path -> BFS
        Obstacles: additional variable we need to recordld

        # Can we try DP -> if we only go right and down (never go backward) -> might

        """
        visited = set()  # (ii, jj, kk) where ii, jj are the grid coordinates and kk is the # of obstacles used so far
        steps = 0
        dq = deque([(0, 0, 0)])

        M = len(grid)
        N = len(grid[0])
        if M == 1 and N == 1:
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while (sz := len(dq)) > 0:  # take sz for each level
            for _ in range(sz):  # for each level
                # all nodes on same level, level starts from 0. zz is the initial state when etering a new grid
                xx, yy, zz = dq.popleft()
                if xx < 0 or xx >= M or yy < 0 or yy >= N or (xx, yy, zz) in visited:
                    continue
                if grid[xx][yy] == 1:  # if obstacle, consume one k
                    if zz >= k:
                        continue  # if the initial kk state is already k, we cannot proceed from here
                    zz += 1  # consume one k and proceeding
                if xx == M-1 and yy == N-1:  # arrived
                    return steps
                # recording the zz-1 as the initial state on this grid is visited
                visited.add((xx, yy, zz-1))
                for dx, dy in dirs:
                    nx, ny = xx+dx, yy+dy
                    dq.append((nx, ny, zz))

            steps += 1

        return -1
