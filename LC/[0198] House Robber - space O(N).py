####################
##### 20240518 #####
####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums=[0]+nums
        N=len(nums)

        dp=[0]*N

        for ii in range(1, N):
            dp[ii]=max(dp[ii-1], dp[ii-2]+nums[ii])
        
        return dp[-1]
####################
##### 20231225 #####
####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        """
        dp[ii]: max profit if we rob upto ii
        """
        for ii in range(N):
            if ii == 0:
                dp[ii] = nums[ii]
                continue
            if ii == 1:
                dp[ii] = max(nums[ii], dp[ii-1])
                continue

            dp[ii] = max(nums[ii]+dp[ii-2], dp[ii-1])

        return dp[-1]

####################
##### 20231008 #####
####################


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)

        dp = [0] * N  # dp[ii] = max profit ending @ ii

        for ii in range(N):
            if ii == 0:
                dp[ii] = nums[ii]
                continue

            dp[ii] = max(nums[ii] + (dp[ii-2] if ii >= 2 else 0), dp[ii-1])

        return dp[-1]


#####################
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        : dp[ii] = max(num[ii] + dp[ii-2], dp[ii-1])
        """
        N = len(nums)
        dp = [0] * N

        dp[0] = nums[0]

        for ii in range(1, N):
            dp[ii] = max(nums[ii] + (dp[ii-2] if ii-2 >= 0 else 0),
                         dp[ii-1] if ii-1 >= 0 else 0)

        return dp[N-1]

####################
##### 20221030 #####
####################


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        """
        : dp[ii]: max amt the robber can get if rob up to iith house
        """

        for ii in range(N):
            if ii == 0:
                dp[ii] = nums[ii]
            else:
                dp[ii] = max(nums[ii] + (dp[ii-2] if ii >= 2 else 0), dp[ii-1])

        return dp[-1]
