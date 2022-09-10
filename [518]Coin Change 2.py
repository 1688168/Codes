# You are given an integer array coins representing coins of different 
# denominations and an integer amount representing a total amount of money. 
# 
#  Return the number of combinations that make up that amount. If that amount 
# of money cannot be made up by any combination of the coins, return 0. 
# 
#  You may assume that you have an infinite number of each kind of coin. 
# 
#  The answer is guaranteed to fit into a signed 32-bit integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#  
# 
#  Example 2: 
# 
#  
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#  
# 
#  Example 3: 
# 
#  
# Input: amount = 10, coins = [10]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= coins.length <= 300 
#  1 <= coins[i] <= 5000 
#  All the values of coins are unique. 
#  0 <= amount <= 5000 
#  
# 
#  Related Topics Array Dynamic Programming 👍 6133 👎 110


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        : counting problem
        : DFS -> repeating computation
        : DP
        : let dp[ii][jj] = num of combination to reach jj amount with first ii coin types
        : ii: 0~len(coins) => m
        : jj: 0~amount     => n
        : time: mn
        : space: mn
        """
        dp = [0] * (amount + 1)

        dp[0] = 1  # 1 way to achieve 0 with 0 coins

        for ii in range(len(coins)):
            for jj in range(1, amount + 1):
                if jj >= coins[ii]:
                    dp[jj] = dp[jj] + dp[jj - coins[ii]]

        return dp[amount]

#         M=len(coins)+1 #0 coins, 1, 2, ...M
#         N=amount
#         print(" m: ", M, " n: ", N)
#         dp=[[0]*(N+1) for _ in range(M)] #including amount

#         for ii in range(M):
#             dp[ii][0]=1

#         for ii in range(1, N+1):
#             dp[0][ii]=0
#             dp[1][ii]=(1 if ii%coins[0]==0 else 0)


#         while ii in range(2, M):
#             while jj in range(1, N+1):
#                 if jj >= coins[ii-1]:
#                     dp[ii][jj]=dp[ii][jj-coins[ii-1]]+dp[ii-1][jj]
#                 else:
#                     dp[ii][jj]=dp[ii-1][jj]

#         print(dp)
#         return dp[M-1][N]


# leetcode submit region end(Prohibit modification and deletion)
