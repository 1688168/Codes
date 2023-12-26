##########
# 20231226
##########
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        for each ii: tke  -> condition, prev < nums[ii]
                     ntke 
                     LIS = max(tke, ntke)
        """
        N = len(nums)

        def hp(prev, ii):
            if ii >= N:
                return 0

            tke = 0
            if prev == -1 or nums[prev] < nums[ii]:
                tke = 1+hp(ii, ii+1)

            ntk = hp(prev, ii+1)
            return max(tke, ntk)

        return hp(-1, 0)


#####################
class Solution:
    def lengthOfLIS(self, nums):  # time exceeded
        """
        :20210925: brutal force solution
        :param nums:
        :return:
        : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
        """
        def hp(st=0, prev=-1):
            if st >= len(nums):
                return 0

            tke = 0
            if prev == -1 or nums[st] > nums[prev]:
                tke = 1 + hp(st+1, st)

            ntk = hp(st+1, prev)

            return max(tke, ntk)

        return hp()
