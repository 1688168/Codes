class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # the extra 1 is for ii+k+1 the ending index to substract
        diff = [0]*(N+1)

        flips = 0
        cnt = 0
        for ii, nn in enumerate(nums):
            flips += diff[ii]  # required flip per earlier operations
            if (nums[ii]+flips) % 2 == 1:
                continue  # after required flipping, if 1, continue
            if ii+k-1 >= N:
                return -1  # false condition
            flips += 1
            diff[ii+k] -= 1
            cnt += 1

        return cnt
