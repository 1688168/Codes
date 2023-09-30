class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        x x x a a x x x
              ^
        """
        ll, rr = 1, len(nums)
        ans = -1

        def count(mm):
            cnt = 0
            for n in nums:
                if n <= mm:
                    cnt += 1
            return cnt

        while ll <= rr:
            mm = ll + (rr-ll)//2

            if count(mm) <= mm:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
