class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """
        * min(subarray)*k >= threshold
        * if we know pre-smaller-equal and next-smaller-> we can calc area and see if area > threshold
        """

        nums = [0]+nums+[0]

        stk = []
        for ii, vv in enumerate(nums):
            while len(stk) > 0 and nums[ii] < nums[stk[-1]]:
                idx = stk.pop()
                width = ii-stk[-1]-1
                area = width*nums[idx]
                if area > threshold:
                    return width

            stk.append(ii)
        return -1
