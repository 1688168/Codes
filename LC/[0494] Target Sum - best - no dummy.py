class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dp[ii][jj]: number of ways to reach target jj ending @ ii
        """
        N=len(nums)
        offset=1000
        dp=[[0] * (offset*2+1) for _ in range(N)]

        dp[0][nums[0]+offset]+=1 ## +0 and -0 both counted for jj=0
        dp[0][-nums[0]+offset]+=1


        for ii in range(1, N):
            for jj in range(-offset, offset+1):
                if 0 <= jj + offset - nums[ii] <= offset*2: dp[ii][jj+offset] += dp[ii-1][jj+offset-nums[ii]]               
                if 0 <= jj + offset + nums[ii] <= offset*2: dp[ii][jj+offset] += dp[ii-1][jj+offset+nums[ii]]

        return dp[-1][target+offset]


##############
# this is for testing
#############
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        dp[ii][jj]: number of ways to reach target jj ending @ ii
        """
        N=len(nums)
        offset=10
        dp=[[0] * (offset*2+1) for _ in range(N)]

        dp[0][nums[0]+offset]=1
        dp[0][-nums[0]+offset]=1


        for ii in range(1, N):
            for jj in range(-offset, offset+1):
                if 0 <= jj + offset - nums[ii] <= offset*2: dp[ii][jj+offset] += dp[ii-1][jj+offset-nums[ii]]               
                if 0 <= jj + offset + nums[ii] <= offset*2: dp[ii][jj+offset] += dp[ii-1][jj+offset+nums[ii]]

        print(dp)
        return dp[-1][target+offset]


##############
# this is for testing
#############
###############
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        nums = [0]+nums
        M = len(nums)
        offset = 10
        N = 22
        dp = [[0]*N for _ in range(M)]
        dp[0][offset] = 1

        for ii in range(1, M):
            for jj in range(-10, 11):

                # if we are adding new number
                if 0 <= jj+offset-nums[ii] <= 21:
                    dp[ii][jj+offset] += dp[ii-1][jj+offset-nums[ii]]

                # if we are substracting new number
                if 0 <= jj+offset+nums[ii] <= 21:
                    dp[ii][jj+offset] += dp[ii-1][jj+offset+nums[ii]]
        print(dp)
        return dp[-1][target+offset]