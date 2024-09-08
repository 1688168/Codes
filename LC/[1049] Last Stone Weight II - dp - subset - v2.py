class Solution:
    def lastStoneWeightII(self, A):
        dp = {0} #set of achievable subset sum.  0 is achievable by do-nothing
        sumA = sum(A)

        # DP will contain all subsets of possible sums
        for a in A:#for each stone
            dp |= {a + i for i in dp} # dp union with each existing achievable weight + new weight

        # from all the possible subset_sum, which one is closest to zero?    
        return min(abs(sumA - i - i) for i in dp)
        