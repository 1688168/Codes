from collections import deque


class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        # direction, row change, column change, reverse direction
        directions = [
            ('U', -1, 0, 'D'),
            ('D', 1, 0, 'U'),
            ('L', 0, -1, 'R'),
            ('R', 0, 1, 'L'),
        ]

        reachable = {(0, 0)}
        target = (0, 0) if master.isTarget() else None

        # Frame: (row, col, next direction index, move back to parent)
        stack = [(0, 0, 0, None)]

        while stack:
            r, c, i, back = stack[-1]

            if i == 4:
                stack.pop()
                if back is not None:
                    master.move(back)
                continue

            # Resume with the next direction after exploring this one.
            stack[-1] = (r, c, i + 1, back)
            direction, dr, dc, reverse = directions[i]
            nr, nc = r + dr, c + dc

            if (nr, nc) in reachable:
                continue
            if not master.canMove(direction):
                continue

            master.move(direction)
            reachable.add((nr, nc))

            if master.isTarget():
                target = (nr, nc)

            stack.append((nr, nc, 0, reverse))

        if target is None:
            return -1

        # BFS over the discovered grid.
        queue = deque([(0, 0, 0)])
        reachable.remove((0, 0))  # Also use this set as BFS's unvisited set.

        while queue:
            r, c, distance = queue.popleft()

            if (r, c) == target:
                return distance

            for _, dr, dc, _ in directions:
                neighbor = (r + dr, c + dc)
                if neighbor in reachable:
                    reachable.remove(neighbor)
                    queue.append((*neighbor, distance + 1))

        return -1