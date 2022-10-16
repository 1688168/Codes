class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        """
        1, 3, 2, 4, 1

        """
        costs.sort()
        ttl=0
        for ii in range(len(costs)):
            ttl += costs[ii]
            if ttl == coins: break
            if ttl > coins:
                ii -= 1
                break

        return ii+1
