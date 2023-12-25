class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = [0]*(limit+1)  # each weight is a bucket

        for w in people:  # bucket sort
            p[w] += 1

        cnt = 0
        x = limit
        while x > 0:  # visit each weight
            jj = p[x]

            while jj > 0:  # for each x, is there another y that can fit in same boat?
                cnt += 1
                p[x] -= 1

                y = limit-x
                # looking for partner weight
                while y > 0 and p[y] == 0:
                    y -= 1  # all weights are greater than 0
                if y > 0:
                    # if we can fit in another ppl, remove it so it won't be counted again
                    p[y] -= 1
                if x == y:
                    jj -= 1
                jj -= 1
            x -= 1

        return cnt
