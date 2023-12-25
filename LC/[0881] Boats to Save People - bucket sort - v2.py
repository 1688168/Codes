class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = [0]*(limit+1)

        for w in people:  # bucket sort
            p[w] += 1

        cnt = 0
        x = limit
        y = 1
        while x > 0:  # visit each x from right

            while x > 0 and p[x] == 0:  # find the first non-zero x
                x -= 1
            if x == 0:  # get out when we visited all weights
                break

            cnt += 1  # for each non-zero x, we need a boat
            p[x] -= 1  # set it to zero
            # is there another ppl from left can fit in the boat?
            while x+y <= limit and p[y] == 0:
                y += 1
            # remove the 1st non-zero y that fits in the boat.
            if x+y <= limit and p[y] > 0:
                p[y] -= 1

        return cnt
