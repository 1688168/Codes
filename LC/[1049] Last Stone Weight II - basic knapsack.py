class Solution:
    """
    >> revised problem statement:
    * find subset of A into group X s.t.
    -> capacity = sum(A)//2
    -> sum(X) is the max of all the subsets
    """
    def lastStoneWeightII(self, A):
        total = sum(A)
        capacity=total//2

        """
        let dp[jj] = max(subset_sum) <= jj
        where jj=subset_sum
        """
        dp=[0]*(capacity+1) #[0, capacity]
        for ii, nn in enumerate(A): # for each item, go by source_from method
            for jj in range(capacity, nn-1, -1):#[0, capacity], go reversed way to avoid using additional dp_old
                if nn+dp[jj-nn] <= jj: 
                    dp[jj] = max(dp[jj], dp[jj-nn]+nn)

        return total - dp[-1]*2
                    
        