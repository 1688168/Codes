###############
# 20231028
###############
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """
        1 3 4 3 1
            x       
          x x x
          x x x
        x x x x x

        min(elements)*k > threshold

        - same as question: 84
        """

        N = len(nums)
        nums = [0]+nums+[0]
        stk = []

        # for each stk[-1] as the min of the subarray
        for ii, nn in enumerate(nums):
            while stk and nn < nums[stk[-1]]:  # nn is the smaller
                curr_ii = stk.pop()
                curr_h = nums[curr_ii]
                next_h = nn
                if stk:  # after first pop, stk[-1] is the previous smaller or equal
                    prev_h = nums[stk[-1]]
                    mnh = curr_h*(ii-stk[-1]-1)
                    if mnh > threshold:
                        return ii-stk[-1]-1

            stk.append(ii)

        return -1

##########################################


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
