##################
# 20261121 - chatGpt
##################
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def has_at_least_k(candidate: int) -> bool:
            count = 0
            for num in nums:
                if num >= candidate:
                    count += 1
                    if count == k:
                        return True
            return False

        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right + 1) // 2

            if has_at_least_k(mid):
                left = mid
            else:
                right = mid - 1

        return left

##################
# 20230930
##################
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ll, rr = int(-1e4), int(1e4)
        # left, right = -10_000, 10_000
        # float("-inf") and float("inf")
        
        ans = -1

        def count(mm):
            cnt = 0
            for n in nums:
                if n >= mm:
                    cnt += 1
            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if count(mm) >= k:
                ans = mm
                ll = mm+1
            else:
                rr = mm-1

        return ans


######################################
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        binary search
        guess t, s.t. count(num > t) >= k  --> make t bigger
                                           --> make t smaller
        """

        ans = -1
        ll, rr = pow(10, 4) * -1, pow(10, 4)

        def count(t):
            cnt = 0
            for ii in range(len(nums)):
                if nums[ii] >= t:
                    cnt += 1

            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if count(mm) >= k:
                ans = mm
                ll = mm+1
            else:
                rr = mm-1

        return ans


###############
