class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = [0]*(limit+1)

        for w in people:  # bucket sort
            p[w] += 1

        cnt = 0
        x = limit
        while x > 0:
            jj = p[x]

            while jj > 0:
                cnt += 1
                p[x] -= 1

                y = limit-x
                # looking for partner weight
                while y > 0 and p[y] == 0:
                    y -= 1  # all weights are greater than 0
                if y > 0:
                    p[y] -= 1
                if x == y:
                    jj -= 1
                jj -= 1
            x -= 1

        return cnt
