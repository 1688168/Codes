##############
# 20240113
##############
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        """
        nums:

        """
        N = len(nums)
        ll, rr = 0, N-1
        cnt = 0
        while ll < rr:
            if nums[ll] == nums[rr]:
                ll += 1
                rr -= 1
                continue
            if nums[ll] < nums[rr]:
                nums[ll+1] += nums[ll]
                ll += 1
            else:
                nums[rr-1] += nums[rr]
                rr -= 1
            cnt += 1

        return cnt


##############
# 20230926
##############
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        N = len(nums)
        ll, rr = 0, N-1

        while ll <= rr:
            if nums[ll] == nums[rr]:
                ll += 1
                rr -= 1
                continue

            if nums[ll] > nums[rr]:
                nums[rr-1] += nums[rr]
                rr -= 1
                cnt += 1
                continue

            if nums[ll] < nums[rr]:
                nums[ll+1] += nums[ll]
                cnt += 1
                ll += 1
                continue

        return cnt


############################


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        cnt = 0
        ll, rr = 0, N-1
        left = nums[ll]
        right = nums[rr]

        while ll < rr:
            # print(" left: ", left, " right: ", right, " ll: ", ll, " rr: ", rr, " cnt: ", cnt)
            if left == right:
                ll += 1
                rr -= 1
                left += nums[ll]
                right += nums[rr]
                continue

            """
            L L L L R R R R
            """

            if left > right:
                cnt += 1
                rr -= 1
                right += nums[rr]

                continue

            if left < right:
                cnt += 1
                ll += 1
                left += nums[ll]

                continue

        return cnt
