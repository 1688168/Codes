# You are given an integer array nums. You are initially positioned at the 
# array's first index, and each element in the array represents your maximum jump 
# length at that position. 
# 
#  Return true if you can reach the last index, or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum 
# jump length is 0, which makes it impossible to reach the last index.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Dynamic Programming Greedy 👍 12868 👎 679


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        : feasibility
        : state: dp[ii] = dp[ii-nums[ii]]+nums[ii]
        : dp[N-1]
        """
        N = len(nums)
        dp = [False] * N

        dp[0] = True

        for ii in range(1, N):
            # dp[ii]=any([True if dp[jj] and jj+nums[jj] >= ii else False for jj in reversed(range(ii))])
            for jj in reversed(range(ii)):
                if dp[jj] and jj + nums[jj] >= ii:
                    dp[ii] = True
                    break

        return dp[N - 1]

# leetcode submit region end(Prohibit modification and deletion)
