class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        """
        nums: binary array
        k:
        """
        cnt = 0
        N = len(nums)
        for ii in range(N):
            """
            0 1 0
            """
            # print("ii: ", ii, " nums: ", nums)
            if nums[ii] == 1:
                continue
            if ii+k-1 >= N:
                return -1
            for jj in range(ii, ii+k):
                nums[jj] ^= 1

            cnt += 1

        return cnt
