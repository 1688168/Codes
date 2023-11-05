class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        1. find index of the right most number that is less than max on it's left 
        2. find index of the left most number that is greater than min on it's right 
        3. the dist btn above two is the answer
        """
        # find the rigt most number that is less than the max on it's left
        N = len(nums)
        MXN = -math.inf
        rmni = 0
        for ii, vv in enumerate(nums):
            if vv < MXN:
                rmni = ii

            MXN = max(MXN, vv)

        MNN = math.inf
        lmni = N-1
        for ii in reversed(range(N)):
            vv = nums[ii]
            if vv > MNN:
                lmni = ii
            MNN = min(MNN, vv)

        return rmni-lmni+1 if rmni-lmni > 0 else 0
