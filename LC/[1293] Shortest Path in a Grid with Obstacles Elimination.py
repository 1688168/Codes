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
        
        M=len(grid)
        N=len(grid[0])
        if M==1 and N==1: return 0
        dirs=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        while (sz:=len(dq)) > 0: #take sz for each level
            for _ in range(sz):# for each level
                x, y, z = dq.popleft() #all nodes on same level, level starts from 0
            
                if x==M-1 and y==N-1: #arrived
                    return steps
                if grid[x][y]==1:#if obstacle, consume one k
                    if kk+1 > k: continue
                    kk+=1
               
                visited.add((x, y, kk))
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >=M or ny < 0 or ny >= N or (nx, ny, kk) in visited: continue
                    dq.append((nx, ny, kk))


            steps += 1
            

        return -1
