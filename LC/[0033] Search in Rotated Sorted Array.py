###########
# 20231105
###########
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ans = -1
        N = len(nums)
        ll, rr = 0, N-1
        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] == target:
                return mm

            if nums[mm] < nums[0]:  # mm is on the right
                if target < nums[mm]:  # target is also on the right sec and less than nums[mm]
                    rr = mm-1
                else:  # target could be on the left or right
                    if target < nums[0]:  # target on the right and greater than nums[mm]
                        ll = mm+1
                    else:
                        rr = mm-1

            else:  # mm is on the left
                if target < nums[mm]:  # target could be on left or right
                    if target < nums[0]:  # target on the right
                        ll = mm+1
                    else:
                        rr = mm-1
                else:  # target on the left and less than nums[mm]
                    ll = mm+1
        return ans


###########
# 20231023
###########
"""
1. check n=nums[mm] in first half or 2nd half
2. based on one, we also need to check target is in first half or 2nd half

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ll, rr = 0, N-1

        while ll <= rr:
            mm = ll+(rr-ll)//2
            n = nums[mm]
            # determin n is in first half or 2nd half:
            if n < nums[0]:  # n is in 2nd half
                if n < target:  # target could be in first or 2nd half.
                    if target < nums[0]:  # target is on 2nd half
                        ll = mm+1
                    else:  # target is on first half
                        rr = mm-1
                elif n == target:
                    return mm
                else:  # N > target, target can only be in 2nd half to be smaller
                    rr = mm-1
            else:  # in first half or the array was not pivited
                if n < target:  # target canonly be on first half to be bigger
                    ll = mm+1
                elif n == target:
                    return mm
                else:  # n > target, target can be in first or 2nd half
                    if target < nums[0]:  # target on 2nd half
                        ll = mm+1
                    else:  # taget on first half
                        rr = mm-1

        return -1
###########
# 20230528
###########


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans, ll, rr = -1, 0, len(nums)-1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            curr = nums[mm]
            if curr >= nums[0]:  # on the left side
                if curr < target:
                    ll = mm+1
                elif curr > target and target >= nums[0]:
                    rr = mm-1
                elif curr > target and target < nums[0]:
                    ll = mm+1
                elif curr == target:
                    return mm

            else:  # on the right side
                if curr > target:
                    rr = mm-1
                elif curr < target and target < nums[0]:
                    ll = mm+1
                elif curr < target and target >= nums[0]:
                    rr = mm - 1
                elif curr == target:
                    return mm

        return ans


##############
# 20230122
##############
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        : nums: ints, ascending order, distinct        
        : rotated k
        : time: logn, searching -> binary search
        : landing in left or right
        """

        ll, rr, ans = 0, len(nums)-1, -1

        # edge cases
        # n=1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        if target < nums[0]:  # target on the right side
            while ll <= rr:
                mm = ll+(rr-ll)//2
                if nums[mm] < nums[0]:
                    if nums[mm] == target:
                        ans = mm
                        break
                    elif nums[mm] > target:
                        rr = mm-1
                    else:
                        ll = mm+1
                else:
                    ll = mm+1

        else:  # target on the left side

            while ll <= rr:
                mm = ll+(rr-ll)//2
                if nums[mm] < nums[0]:
                    rr = mm-1
                else:
                    if nums[mm] == target:
                        ans = mm
                        break
                    elif nums[mm] > target:
                        rr = mm-1
                    else:
                        ll = mm+1

        return ans


####################################
####################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

                  7
              6
           5
        4

                           2
                        1
                     0


        """

        N = len(nums)
        ll, rr = 0, N-1
        ans = -1
        while ll <= rr:
            mm = ll+(rr-ll)//2
            curr = nums[mm]

            if curr == target:  # found it
                return mm

            if curr < nums[0]:  # landed on the right
                if target < curr or target > nums[N-1]:
                    rr = mm-1
                else:
                    ll = mm+1

            else:  # landed on the left
                if curr < target or target < nums[0]:
                    ll = mm+1
                else:
                    rr = mm-1

        return ans

########################################################
########################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ll, rr, ans = 0, len(nums)-1, -1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] == target:
                return mm

            if nums[mm] >= nums[0]:  # on the left

                if nums[mm] < target or target < nums[0]:
                    ll = mm+1
                else:
                    rr = mm-1

            else:  # on the right

                if target < nums[mm] or target >= nums[0]:
                    rr = mm-1
                else:
                    ll = mm+1

        return ans
