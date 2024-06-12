class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        * how do you know this is knapsack problem?
        1. given a list or resource
        2. given a target value
        3. num of ways to select
        * nums[ii]: positive integers
        * k: 
        """
        N=len(nums)
        M=int(1e9)+7
        ttl=sum(nums)
        cnt=0

        def dfs(st, acc):
            nonlocal cnt
          
            if st >=N: return 
            tke=acc+nums[st]
            rest=ttl-tke
            if tke >=k and rest >= k: cnt += 1
          
            dfs(st+1, acc+nums[st])
            dfs(st+1, acc)
        
        dfs(0, 0)
        return cnt%M
        