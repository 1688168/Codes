class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        => greedy
        1. put everybody on A
        2. move those can reduce most cost to B
        3. return ttl costs
        """
        N = len(costs)
        M = N//2
        costs.sort(key=lambda x: (x[1]-x[0]))
        acc = 0
        # print(" costs: ", costs)
        for ii in range(N):
            if ii < M:
                acc += costs[ii][1]
            else:
                acc += costs[ii][0]

        return acc
