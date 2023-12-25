###########
# 20230225
###########

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp_rob_first = [0]*N
        dp_no_rob_first = [0]*N

        for ii in range(N):
            if ii == 0:
                dp_rob_first[ii] = nums[ii]
                dp_no_rob_first[ii] = 0
                continue
            if ii == 1:
                dp_rob_first[ii] = dp_rob_first[ii-1]
                dp_no_rob_first[ii] = nums[ii]
                continue
            if ii == N-1:
                dp_rob_first[ii] = dp_rob_first[ii-1]
                dp_no_rob_first[ii] = max(
                    nums[ii] + dp_no_rob_first[ii-2], dp_no_rob_first[ii-1])
                continue

            dp_rob_first[ii] = max(
                nums[ii] + dp_rob_first[ii-2], dp_rob_first[ii-1])
            dp_no_rob_first[ii] = max(
                nums[ii] + dp_no_rob_first[ii-2], dp_no_rob_first[ii-1])

        return max(dp_rob_first[-1], dp_no_rob_first[-1])

###########
# 20230813
###########


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. trying to find an optimized solution
        2. current states doesn't depend on future state and future state doesn't not change current local state
        3. current state is optimized 
        """

        N = len(nums)

        if N == 0:
            return 0
        if N == 1:
            return nums[0]

        # robbing the first, since we fixed first one, the 2nd one and the last are both fixed
        dp1 = [0]*N
        dp1[0] = nums[0]
        dp1[1] = dp1[0]
        dp2 = [0]*N  # not robbing the first

        for ii in range(1, N):
            if ii > 1 and ii < N-1:
                dp1[ii] = max(nums[ii] + dp1[ii-2], dp1[ii-1])
            if ii == N-1:
                dp1[ii] = dp1[ii-1]

            dp2[ii] = max(nums[ii] + (dp2[ii-2] if ii >= 2 else 0), dp2[ii-1])

        return max(dp1[-1], dp2[-1])


###########
# 20230531
###########
# this is just another thought process, but complexity is the same
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp1 = [0]*N  # rob first
        dp2 = [0]*N  # rob last

        for ii in range(N):
            if ii == 0:
                dp1[ii] = nums[ii]
                dp2[ii] = 0
            elif ii == N-1:
                dp1[ii] = dp1[ii-1]
                # we are robbing the last
                dp2[ii] = nums[ii] + (dp2[ii-2] if ii >= 2 else 0)
            else:
                dp1[ii] = max(dp1[ii-1], (dp1[ii-2]+nums[ii])
                              if ii-2 >= 0 else nums[ii])
                dp2[ii] = max(dp2[ii-1], (dp2[ii-2]+nums[ii])
                              if ii-2 >= 0 else nums[ii])

        return max(dp1[-1], dp2[-1])


###########
# 20221105
###########
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp1 = [0]*N  # not robbing the 1st house
        dp2 = [0]*N  # not robbing the last house

        for ii, vv in enumerate(nums):
            if ii == 0:
                dp1[ii] = 0  # not robbing the 1st house
                dp2[ii] = nums[ii]
            elif ii == N-1:
                dp1[ii] = max(
                    nums[ii]+(dp1[ii-2] if ii >= 2 else 0), dp1[ii-1])
                dp2[ii] = dp2[ii-1]  # not robbing the last house
            else:
                dp1[ii] = max(
                    nums[ii]+(dp1[ii-2] if ii >= 2 else 0), dp1[ii-1])
                dp2[ii] = max(
                    nums[ii]+(dp2[ii-2] if ii >= 2 else 0), dp2[ii-1])

        return max(dp1[-1], dp2[-1])

###########
# 20221031
###########


class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp1 = [0]*N  # not robbing the last
        dp2 = [0]*N  # not robbing the first

        for ii in range(N):
            if ii == 0:
                dp1[ii] = nums[ii]
            elif ii == N-1:
                dp1[ii] = dp1[ii-1]
            else:
                dp1[ii] = max((dp1[ii-2] if ii >= 2 else 0) +
                              nums[ii], dp1[ii-1])

        for ii in range(N):
            if ii == 0:
                dp2[ii] = 0
            else:
                dp2[ii] = max((dp2[ii-2] if ii >= 2 else 0) +
                              nums[ii], dp2[ii-1])

        return max(dp1[-1], dp2[-1])


################################################
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        : return max(not robbing 1st, not robbing last)
        : dp[ii] as max value with house ending @ ii
        : dp[ii] = max(nums[ii]+dp[ii-2], dp[ii-1])
        : not robbing 1st:
        """

        if len(nums) == 1:
            return nums[0]

        dp = [0]*len(nums)
        # not robbing 1st
        for ii in range(1, len(nums)):
            dp[ii] = max(nums[ii] + (dp[ii-2] if ii >= 2 else 0), dp[ii-1])

        dp1 = dp[-1]

        dp = [0]*len(nums)

        # not robbing last
        for ii in range(len(nums)-1):
            dp[ii] = max(nums[ii] + (dp[ii-2] if ii-2 >= 0 else 0),
                         dp[ii-1] if ii-1 >= 0 else 0)

        dp2 = dp[-2]

        return max(dp1, dp2)
