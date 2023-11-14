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
        ll = 0
        ans = -1

        while ll < rr:  # 32
            mm = (ll+rr) >> 1  # mm is the guessed distance
            cnt = 0

            # we need to count number of pairs with distance < mm
            # N -- we fix the first number and binary search the next (NlogN)
            jj = 0
            for ii, vv in enumerate(nums):

                while jj < N and nums[jj]-vv <= mm:
                    jj += 1

                cnt += jj-ii-1
            if cnt < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm
        return ll


##############################
