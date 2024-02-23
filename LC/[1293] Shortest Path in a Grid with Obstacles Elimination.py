from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        shortest path -> BFS
        Obstacles: additional variable we need to recordld
        
        # Can we try DP -> if we only go right and down (never go backward) -> might
        
        """
        visited=set()#(ii, jj, kk) where ii, jj are the grid coordinates and kk is the # of obstacles used
        steps=0
        dq=deque([(0,0,0)])
        kk=0
        arrived=False
        M=len(grid)
        N=len(grid[0])
        dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        while (sz:=len(dq)) > 0: #take sz for each level
            for _ in range(sz):# for each level
                x, y, z = dq.popleft() #all nodes on same level, level starts from 0
                if (x, y, z) in visited: continue
                if x==M-1 and y==N-1: #arrived
                    arrived=True
                    break
                if grid[x][y]==1:#if obstacle, consume one k
                    kk+=1
                if kk+1 > k: continue # if we used more than what we can, we cannot move forward
                visited.add((x, y, kk))
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    dq.append((nx, ny, kk))


            steps += 1
            if arrived: break

        return steps
