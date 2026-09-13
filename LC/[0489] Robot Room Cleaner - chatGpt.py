"""
LeetCode 489: Robot Room Cleaner

Mental model
------------
The hidden room is an implicit graph:

* Every reachable open cell is a graph node.
* A successful robot.move() is an edge to a neighboring node.
* We assign our own coordinates, with the starting cell called (0, 0).
* DFS explores the graph, and a visited set prevents cycles.

The essential DFS contract is:

    dfs(row, col, direction) starts and finishes with the physical robot
    at (row, col), facing direction.

To satisfy that contract, after exploring a neighbor we must restore BOTH
the robot's position and its direction.
"""


# Robot's interface is supplied by LeetCode.
# We do not implement this class ourselves.
#
# class Robot:
#     def move(self) -> bool:
#         """Move forward if possible and report whether the move succeeded."""
#
#     def turnLeft(self) -> None:
#         """Turn 90 degrees left without changing cells."""
#
#     def turnRight(self) -> None:
#         """Turn 90 degrees right without changing cells."""
#
#     def clean(self) -> None:
#         """Clean the current cell."""


class Solution:
    def cleanRoom(self, robot):
        """Clean every open cell reachable from the robot's starting cell."""

        # Name the robot's unknown initial direction 0.
        # The remaining directions are listed clockwise from it:
        # 0 = initial/up, 1 = right, 2 = backward/down, 3 = left.
        # These are logical directions; they do not need to match compass north.
        directions = (
            (-1, 0),  # Direction 0: one logical row up.
            (0, 1),   # Direction 1: one logical column right.
            (1, 0),   # Direction 2: one logical row down.
            (0, -1),  # Direction 3: one logical column left.
        )

        # Store logical coordinates of open cells that DFS has discovered.
        # A local set is fresh for every call to cleanRoom().
        visited = set()

        def go_back():
            """Return across the edge just used and restore the old direction."""

            # Face the cell from which we entered the current cell.
            robot.turnRight()
            robot.turnRight()

            # Move one step back to the parent cell.
            # This succeeds because we just came through this same open edge.
            robot.move()

            # Face the original direction again.
            # Now both position and orientation have been restored.
            robot.turnRight()
            robot.turnRight()

        def dfs(row, col, direction):
            """
            Explore from (row, col).

            Precondition and postcondition:
            the robot is at (row, col), facing `direction`.
            """

            # Mark this cell immediately so a cycle cannot enter it again.
            visited.add((row, col))

            # This is the only DFS call for this coordinate, so clean it once.
            robot.clean()

            # Try all four directions, beginning with the current direction.
            for offset in range(4):
                # Turning clockwise `offset` times from the entry direction
                # gives the logical direction the robot currently faces.
                next_direction = (direction + offset) % 4

                # Compute the logical coordinate directly in front of the robot.
                row_change, col_change = directions[next_direction]
                next_row = row + row_change
                next_col = col + col_change
                next_cell = (next_row, next_col)

                # First avoid known cells; this saves an unnecessary physical move.
                # If the cell is unknown, move() tells us whether it is open.
                if next_cell not in visited and robot.move():
                    # move() succeeded, so logical and physical state both
                    # advance into the neighboring cell.
                    dfs(next_row, next_col, next_direction)

                    # The recursive call finishes at the neighbor in the same
                    # direction. Physically return to this parent and face the
                    # same direction as before the recursive exploration.
                    go_back()

                # Whether the target was blocked, visited, or fully explored,
                # rotate once so the next loop iteration tests the next side.
                robot.turnRight()

            # Four right turns make a full circle. Therefore, on return, the
            # robot is still at (row, col) and faces `direction`, satisfying
            # this function's contract.

        # Invent coordinate (0, 0) and direction 0 for the unknown starting state.
        # All other coordinates and directions are defined relative to this choice.
        dfs(0, 0, 0)


# Complexity
# ----------
# Let N be the number of reachable open cells.
# Time:  O(N), because each visited cell checks exactly four directions.
# Space: O(N), for the visited set and the recursive DFS call stack.
