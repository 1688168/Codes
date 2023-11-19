class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        ll = min([b-a for a, b in zip(nums[:-1], nums[1:])])
        rr = nums[-1]-nums[0]
        ans = rr

        def count(mm):
            ii = 0
            jj = 0
            cnt = 0
            # while ii<N:
            #     while jj<N and nums[jj]-nums[ii] <= mm:
            #         jj+=1
            #     cnt += (jj-ii-1)

            #     ii+=1

            # return cnt
            for ii, vv in enumerate(nums):

                while jj < N and nums[jj]-vv <= mm:
                    jj += 1

                cnt += jj-ii-1
            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
