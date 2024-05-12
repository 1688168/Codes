# https://www.youtube.com/results?search_query=leetcode+2297
"""
monotonic stack
[1944]
[2282]
"""
###############
# 20240512
###############
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        """
        # Analysis
        + single list with cost associated with
        + N=10^5
        + ii < kk < jj
        + constrain 1: nums[jj] is nums[ii] next greater_equal
        + constrain 2: nums[jj] is nums[ii] next smaller

        # strategy:
        + Maintain monotonic stack
        -- Constrain 1:
        - maintain prev_greater (anything after is smaller or equal than current)
        -- Constrain 2:
        - matintain prev_smaller_equal (anything after is greater than current)

        let dp[ii]: the min cost jumping to ii
            dp[ii] = dp[jj]+cost[ii] where jj is prev_smaller_equal or prev_greater
        """
        N=len(nums) #take size
        dp=[math.inf]*N # declare DP
        dp[0]=0

        # monotonic stack
        stk_greater=[]
        stk_smaller_equal=[]


        for ii, nn in enumerate(nums): # try all elements
            # constrain 1, jump higher use case:
            while stk_greater and nums[stk_greater[-1]] <= nn: #those jj who can jump higher is smaller or equal
                dp[ii]=min(dp[ii], dp[stk_greater[-1]]+costs[ii])
                stk_greater.pop()
            
            stk_greater.append(ii)


            while stk_smaller_equal and nums[stk_smaller_equal[-1]] > nn: #you can jump higher when equal or smaller
                dp[ii]=min(dp[ii], dp[stk_smaller_equal[-1]]+costs[ii])
                stk_smaller_equal.pop()
            
            stk_smaller_equal.append(ii)

        
        return dp[-1]
        

###############
# 20240407
###############


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        """
        + nums[ii]:
        + cost[ii]
             xx  
            xxx
        x   xxxx
        xx xxxxx
        xxxxxxxx
        xxxxxxxx
        i   j

        => min cost
        dp[ii]: min cost to jump to ii
        dp[ii]= min(dp[jj])+cost[ii]
        N=pow(10, 5)
        """
        N = len(nums)
        dp = [math.inf]*N
        dp[0] = 0
        stk_prev_greater = []  # anything in between can jump higher
        stk_prev_smaller = []  # anything in between can jump lower
        for ii, nn in enumerate(nums):
            while stk_prev_greater and nn >= nums[stk_prev_greater[-1]]:
                dp[ii] = min(dp[ii], dp[stk_prev_greater[-1]]+costs[ii])
                stk_prev_greater.pop()

            while stk_prev_smaller and nn < nums[stk_prev_smaller[-1]]:
                dp[ii] = min(dp[ii], dp[stk_prev_smaller[-1]]+costs[ii])
                stk_prev_smaller.pop()

            stk_prev_greater.append(ii)
            stk_prev_smaller.append(ii)

        return dp[-1]

###############
# 20240115
###############


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        """
        nums:
        costs:
        dp[ii]= min(dp[jj]) + cost[ii] where jj < ii
        # jump higher 
        * for all jj < ii that is smaller than ii ()
        """
        N = len(nums)

        stk0 = []
        stk1 = []
        dp = [math.inf]*N
        dp[0] = 0
        for ii, nn in enumerate(nums):
            # considering jump higher
            # if next item is greater than current item, anything before current item that is smaller than or equal to current item is irrelevant
            # so we pop anything in the stack that is smaller than or equal to current
            # jump higher, k in between (jj, ii) is strictly smaller than jj (okay to be equal to ii)
            while stk0 and nn >= nums[stk0[-1]]:
                dp[ii] = min(dp[ii], dp[stk0.pop()]+costs[ii])

            # considering jump lower
            # if next item is smaller than current itme, anything before current item that is samller than current item is irrelevant.
            # so we pop anything in the stack that is smaller than current item
            # jump lower, k in between (jj, ii) is smaller than or equal to jj
            while stk1 and nn < nums[stk1[-1]]:
                dp[ii] = min(dp[ii], dp[stk1.pop()]+costs[ii])

            stk0.append(ii)
            stk1.append(ii)

        return dp[-1]


####################################
class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        N = len(nums)
        dp = [math.inf]*N  # dp[ii] min cost to reach ii from statt
        dp[0] = 0
        stk_desc = []
        stk_asc = []
        for ii, vv in enumerate(nums):
            # what's the prev valid jump?
            # Type I: prev ii which nums[ii] <= nums[jj] and all kk in between are < nums[ii]
            # Type II:
            # type I jump to higher or equal
            while stk_desc and vv >= nums[stk_desc[-1]]:
                dp[ii] = min(dp[ii], costs[ii]+dp[stk_desc.pop()])

            while stk_asc and vv < nums[stk_asc[-1]]:  # jump lower
                dp[ii] = min(dp[ii], costs[ii]+dp[stk_asc.pop()])

            stk_desc.append(ii)
            stk_asc.append(ii)

        return dp[-1]
