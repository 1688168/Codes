# this plython is TLE

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # calculate the consolidated city maxPower
        N = len(stations)
        acc = 0
        nums = stations[:]
        for ii in range(r+1):
            acc += stations[ii]

        for ii in range(N):

            if ii == 0:
                nums[ii] = acc
            else:
                adding = (0 if ii+r >= N else stations[ii+r])
                removing = (0 if ii-r-1 < 0 else stations[ii-r-1])
                acc += (adding-removing)
                nums[ii] = acc

        # print(" consolidated station: ", nums)

        # define binary helper function

        def isokay(mm, r, k, nums):
            N = len(nums)
            for ii in range(N):
                if nums[ii] >= mm:
                    continue
                short = mm-nums[ii]

                if short > k:
                    return False
                for jj in range(ii, min(N, ii+2*r+1)):
                    nums[jj] += short
                k -= short

            return True

        # now binary search the max(min-powered city)
        ll, rr, ans = 0, pow(10, 10), -1

        while ll <= rr:
            mm = ll+(rr-ll)//2
            # make a copy to avoid nums being modified in helper
            if isokay(mm, r, k, nums[:]):
                ans = mm
                ll = mm+1
            else:
                rr = mm-1

        return int(ans)
