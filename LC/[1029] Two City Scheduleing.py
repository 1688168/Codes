class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])

        ttl = 0
        n = len(costs)//2
        for ii in range(n):
            a, b = costs[ii]
            c, d = costs[ii+n]
            ttl += (a+d)

        return ttl


########################
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        => O(n^2)
        => min costs
        0. brute force. C(n, n//2)
        1. binary search: 32, n ?
        2. dynamic programming: ?? no idea
        3. Greedy: sort (nlogn)
        """
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
