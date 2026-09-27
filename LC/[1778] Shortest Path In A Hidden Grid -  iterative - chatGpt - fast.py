from collections import deque

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = [
            ('U', 0, -1, 'D'),
            ('D', 0, 1, 'U'),
            ('L', -1, 0, 'R'),
            ('R', 1, 0, 'L')
        ]

        start = (0, 0)

        if master.isTarget(): # return immediately if start is target
            return 0

        reachable = {start}
        target = None

        # Frame: [position, next direction index, return direction]
        stack = [[start, 0, None]]

        while stack:
            code, ii, return_dir = stack[-1]

            if ii == 4: # after tried all 4 direction
                stack.pop() # pop current frame
                if return_dir is not None: # None is Origin
                    master.move(return_dir) # here we moved back to previous cell
                continue #pop current frame (returning to previous frame)

            stack[-1][1] += 1 # update next direction index for current cell

            xx, yy = code
            dd, dx, dy, rd = directions[ii]
            n_code = (xx + dx, yy + dy)

            if n_code in reachable:
                continue
            if not master.canMove(dd):
                continue

            master.move(dd)
            reachable.add(n_code)
            stack.append([n_code, 0, rd])

            if master.isTarget():
                target = n_code

        if target is None:
            return -1

        lvl = 0
        dq = deque([start])
        reachable.remove(start)

        while dq:
            for _ in range(len(dq)):
                code = dq.popleft()

                if code == target:
                    return lvl

                xx, yy = code

                for _, dx, dy, _ in directions:
                    n_code = (xx + dx, yy + dy)

                    if n_code in reachable:
                        reachable.remove(n_code)
                        dq.append(n_code)

            lvl += 1

        return -1