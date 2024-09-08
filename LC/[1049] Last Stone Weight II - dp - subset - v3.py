class Solution:
    def lastStoneWeightII(self, A):
        dp = {0}
        for a in A:
            dp = {a + x for x in dp} | {abs(a - x) for x in dp}
        return min(dp)
        