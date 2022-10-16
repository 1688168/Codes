from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        BFS
        """
        dirs=[(-2, -1), (-1, -2), (1, -2), (-1, 2)]


        x, y=abs(x), abs(y)
        dq=deque([(x,y)])
        #visited=set([(0,0)])
        visited=[[0]*601 for _ in range(601)]
        lvl=-1
        while (sz:=len(dq)) > 0:
            lvl+=1
            for _ in range(sz):
                (xx, yy)=dq.popleft()
                if xx + yy==0: return lvl

                for dx, dy in dirs:
                    nx, ny=abs(xx+dx), abs(yy+dy)
                    #if (nx, ny) in visited: continue
                    if visited[nx][ny] == 1: continue
                    visited[nx][ny]=1
                    dq.append((nx, ny))
        return -1
