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
