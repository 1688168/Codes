#### use bitmap still no good
from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        BFS
        """
        dirs=[(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        dq=deque([(0,0)])

        #visited=set([(0,0)])
        visited=[[0]*602 for _ in range(602)]
        lvl=-1
        while (sz:=len(dq)) > 0:
            lvl+=1
            for _ in range(sz):
                (xx, yy)=dq.popleft()
                if (xx, yy)==(x, y): return lvl

                for dx, dy in dirs:
                    nx, ny=xx+dx, yy+dy
                    #if (nx, ny) in visited: continue
                    if visited[nx+300][ny+300] == 1: continue
                    visited[nx+300][ny+300]=1
                    dq.append((nx, ny))
        return -1
