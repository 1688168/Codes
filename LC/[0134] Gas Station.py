##############
# 20231217
##############
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # to complete the circle, we need to ensure ttl gas > ttl cost

        if sum(gas) < sum(cost):
            return -1

        # now we guarantee we have a unique answer
        ttl = 0
        ans = 0
        N = len(gas)
        # here we need to find the last negative gas-cost and the next one is the answer
        # as we need all postive remaining to pay for the future costs and relying on unique answer constrain
        for ii in range(N):
            ttl += gas[ii]-cost[ii]
            if ttl < 0:
                ttl = 0
                ans = ii+1

        return ans

###########################


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        1. it is guaranteed to be unique solution if existing
        2. if solution exist, ttl gas must be >= ttl cost
        """
        ttl_gas = sum(gas)
        ttl_cost = sum(cost)
        if ttl_gas < ttl_cost:
            return -1
        N = len(gas)
        total = 0
        ans = 0
        for ii in range(N):  # since the answer is guaranteed to be quinue,
            # if one works, we cannot have another ii after current one that also work
            total += (gas[ii]-cost[ii])
            if total < 0:
                total = 0
                ans = ii+1

        return ans
