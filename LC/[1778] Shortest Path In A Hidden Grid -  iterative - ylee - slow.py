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
        
        start = encode(0, 0)
        reachable = {start}
        target = start if master.isTarget() else None

        # implement DFS iteratively
        stack = [[encode(0, 0), 0, None]] # coordinate and direction idx
        while stack:
            code, ii, ord = stack[-1]
            xx, yy = decode(code)

            if ii == 4: # we finished all 4 directions exploration. we can return to previous cell
                stack.pop()
                if ord is not None:  
                    master.move(ord)
                continue

            dd, dx, dy, rd = directions[ii]
            nx, ny = xx+dx, yy+dy
            n_code=encode(nx, ny)
            
            stack[-1][1] += 1
            if n_code in reachable: 
                continue
            
            if not master.canMove(dd): 
                continue

            stack.append([n_code, 0, rd])
            reachable.add(n_code)
            master.move(dd)
            if master.isTarget():
                target = n_code


        if target is None: return -1

        # now we have the grid mapped and know where the target is. we do a BFS to find the shortest distance
        lvl=0
        dq = deque([encode(0, 0)])
        reachable.remove(encode(0, 0))
        while dq:
            sz = len(dq) # num of notes in current lvl (breath)
            for _ in range(sz):
                xx, yy = decode(dq.popleft())
                if encode(xx, yy) == target: return lvl
                for ii in range(4):
                    _, dx, dy, _ = directions[ii]
                    nx, ny = xx+dx, yy+dy
                    n_code = encode(nx, ny)
                    if n_code in reachable: 
                        dq.append(encode(nx, ny))
                        reachable.remove(n_code)
            lvl += 1
        return -1
