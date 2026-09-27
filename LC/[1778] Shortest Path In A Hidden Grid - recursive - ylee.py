# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # setup required data structure for DFS to map the grid
        visited = set()
        directions = [ # each grid cell, we will need to try the 4 directions for DFS
            ['U', 0, -1, 'D'], # move dir, delta x, delta y, return dir
            ['D', 0, 1, 'U'], 
            ['L', -1, 0, 'R'],
            ['R', 1, 0, 'L']
        ]

        # helpers
        def encode(xx, yy):
            return str(xx)+"#"+str(yy)

        def decode(code):
            xx, yy = code.split("#")
            return (int(xx), int(yy))

        reachable = {encode(0, 0)}
        target = None

        def dfs(xx, yy): # dfs explorying the grid
            nonlocal target
            # at each cell (xx, yy), we will try all 4 directions to explore the grid and map the reachable cells

            if master.isTarget(): target = encode(xx, yy)
            for ii in range(4):
                dd, dx, dy, rd = directions[ii]
                nx, ny = xx+dx, yy+dy
                code = encode(nx, ny)
                if code in reachable: continue
                if not master.canMove(dd): continue
                # we will move the robot
                master.move(dd)
                # we will dfs the next cell
                reachable.add(code)
                dfs(nx, ny)
                # we need to move the robot back and try next direction
                master.move(rd)
        

        visited.add(encode(0, 0))

        dfs(0, 0)
        
        if target is None: return -1

        # now we have the grid mapped and know where the target is. we do a BFS to find the shortest distance
        lvl=0
        dq = deque([encode(0, 0)])

        while dq:
            sz = len(dq) # num of notes in current lvl (breath)
            for _ in range(sz):
                xx, yy = decode(dq.popleft())
                if encode(xx, yy) == target: return lvl
                for ii in range(4):
                    _, dx, dy, _ = directions[ii]
                    nx, ny = xx+dx, yy+dy
                    n_code = encode(nx, ny)
                    if n_code in visited: continue
                    visited.add(n_code)
                    if n_code in reachable: dq.append(encode(nx, ny))
            lvl += 1
        return -1
