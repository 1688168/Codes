class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        1. sort: nlogn
        2. Binary Search: while loop
        3. outter loop: N
        4. bisect_right: logN
        => 32NlogN
        """
        nums.sort()
        N = len(nums)
        rr = nums[-1]-nums[0]
        ll = math.inf
        ans = -1
        for ii in range(1, N):
            ll = min(ll, nums[ii]-nums[ii-1])

        while ll <= rr:  # 32
            mm = ll+(rr-ll)//2  # mm is the guessed distance
            cnt = 0

            # we need to count number of pairs with distance < mm
            # N -- we fix the first number and binary search the next (NlogN)
            for ii, vv in enumerate(nums):
                """
                a 1 2 3 4 5 (since we bisect_right the whole array )
                        ^                
                b   2 3 4 5 6 ...

                b-a=mm (b is bigger as we are fixing a looking for b)
                b=a+mm
                where to insert a+k?
                """
                idx = bisect.bisect_right(nums, vv+mm)  # logN
                cnt += (idx-ii-1)
            if cnt >= k:
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans


##############################
