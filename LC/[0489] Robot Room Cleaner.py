# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

"""
## Observations:
* we need to traverse all the grids of the room -> dfs or bfs
* we started somewhere in the room facing north -> we do not have absolute coordinate

## How is this diff than regular traversing 
* recursion/stack takes care of back-track automatically, in this problem, we need to go back to parent (prev) node by ourselvous
* we started (0,0direction (facing). a typical traversing we have no concept of which side we are facing and we typically started from tree root or some node of a graph.
* to model the robot and the location of the robot, we need 3 attributes (xx, yy, dd) 
"""

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        visited=set()
        
        def encode(xx, yy):
            return str(xx) + "#" + str(yy)

        def dfs(xx, yy, dd):
            """
            # on each dfs, we are entering a new
            """
            # base case
            #if encode(xx, yy) in visited: return # we likely can remove this.

            # first thing you do is clean
            robot.clean()

            # we need to try all directions
            for ii in range(4): # in each node, we need to try all directions
                ndd = (dd+ii)%4 # starting from the original direction
                nxx = xx + directions[ndd][0]
                nyy = yy + directions[ndd][1]

                if encode(nxx, nyy) in visited or not robot.move(): 
                    robot.turnRight()
                    continue

                # when we get here, our robot already moved to next cell                    
                visited.add(encode(nxx, nyy))
                dfs(nxx, nyy, ndd)
                robot.turnRight() # turn 180
                robot.turnRight()
                robot.move() # to back to previous node
                robot.turnRight()
                robot.turnRight() # turn back to original direction and ready for next turn

                robot.turnRight()
        
        visited.add(encode(0, 0)) # starting from any cell (0, 0, 0) as origin
        dfs(0, 0, 0) #the initial cell is facing north

        