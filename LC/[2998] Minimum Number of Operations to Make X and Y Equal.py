class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        mx = x
        mn = y
        dq = collections.deque([x])

        lvl = 0
        visited = set()
        while (sz := len(dq)) > 0:

            for _ in range(sz):
                curr = dq.popleft()
                if curr == mn:
                    return lvl
                if curr in visited:
                    continue
                visited.add(curr)

                if curr+1 <= int(1e4):
                    dq.append(curr+1)
                if curr-1 >= 1:
                    dq.append(curr-1)

                if curr % 11 == 0 and curr//11 >= 1:
                    dq.append(curr//11)
                if curr % 5 == 0 and curr//5 >= 1:
                    dq.append(curr//5)
            lvl += 1

        return lvl
