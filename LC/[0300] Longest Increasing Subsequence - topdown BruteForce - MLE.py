class Solution:
    def lengthOfLIS(self, nums):  # time exceeded
        """
        :20210925: brutal force solution
        :param nums:
        :return:
        : Time: O(N^2).  T(N)=T(n-1)+T(n-1)
        """
        @cache
        def hp(st=0, prev=-1):
            if st >= len(nums):
                return 0

            tke = 0
            if prev == -1 or nums[st] > nums[prev]:
                tke = 1 + hp(st+1, st)

            ntk = hp(st+1, prev)

            return max(tke, ntk)

        return hp()
