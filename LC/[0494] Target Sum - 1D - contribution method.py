class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset=1000
        dp=[0]*(offset*2+5)
        dp[0+offset]=1 # skipping all is counted as one way to achieve 0
        for ii, nn in enumerate(nums):#for each resource, always take with options           

            dp_new = [0]*(offset*2+5) # reduce memory foot print

            for jj in range(-offset, offset+1): #what can new element move the current sum to?
                # take as positive
                if -offset <=jj+nn<=offset:
                    dp_new[jj+nn+offset] += (dp[jj+offset])
                # take as negative
                if -offset <=jj-nn<=offset:
                    dp_new[jj-nn+offset] += (dp[jj+offset])
            
            dp=dp_new
        
        return dp[target+offset]