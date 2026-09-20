from collections import deque


class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = [
            ('U', -1, 0, 'D'),
            ('D', 1, 0, 'U'),
            ('L', 0, -1, 'R'),
            ('R', 0, 1, 'L'),
        ]

        reachable = {(0, 0)}
        target = None

        def dfs(r, c):
            nonlocal target

            if master.isTarget():
                target = (r, c)

            for direction, dr, dc, reverse in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in reachable:
                    continue
                if not master.canMove(direction):
                    continue

                reachable.add((nr, nc))

                master.move(direction)
                dfs(nr, nc)
                master.move(reverse)  # Backtrack physically.

        dfs(0, 0)

        if target is None:
            return -1

        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}

        while queue:
            r, c, distance = queue.popleft()

            if (r, c) == target:
                return distance

            for _, dr, dc, _ in directions:
                neighbor = (r + dr, c + dc)

                if neighbor in reachable and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((*neighbor, distance + 1))

        return -1