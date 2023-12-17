class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = [0]*(limit+1)

        for w in people:  # bucket sort
            p[w] += 1

        cnt = 0
        x = limit
        y = 1
        while x > 0:

            while x > 0 and p[x] == 0:
                x -= 1
            if x == 0:
                break

            cnt += 1
            p[x] -= 1
            while x+y <= limit and p[y] == 0:
                y += 1
            if x+y <= limit and p[y] > 0:
                p[y] -= 1

        return cnt
