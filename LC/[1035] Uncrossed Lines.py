class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        this is asking LCS
        N=500
        """
        nums1 = [0]+nums1
        nums2 = [0]+nums2
        N1 = len(nums1)
        N2 = len(nums2)
        dp = [[0]*N2 for _ in range(N1)]

        for ii in range(1, N1):
            for jj in range(1, N2):
                if nums1[ii] == nums2[jj]:
                    dp[ii][jj] = 1+dp[ii-1][jj-1]
                else:
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])

        return dp[-1][-1]
