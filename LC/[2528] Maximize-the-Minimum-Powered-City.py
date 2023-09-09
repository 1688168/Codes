class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # calculate the consolidated city maxPower
        N = len(stations)
        nums = [0]*N
        nums[0] = sum(stations[:r+1])
        for ii in range(1, N):
            nums[ii] = nums[ii-1] + (stations[ii+r] if (ii+r) < N else 0) - \
                (stations[ii-r-1] if (ii-r-1) >= 0 else 0)

        # print(" consolidated station: ", nums)

        # define binary helper function

        def isokay(mm, r, k, nums):
            N = len(nums)
            new_stations_out_of_range = [0] * (N+2*r+1)
            added_stations = 0
            # print(" mm: ", mm, " ------ ")
            for ii in range(N):
                added_stations -= new_stations_out_of_range[ii]
                short = mm-nums[ii]-added_stations
                # print(" ii: ================= ", ii )
                # print(" short: ", short, " kk: ", k, " nums[ii]: ", nums[ii], " added: ", added_stations, " removing: ", new_stations_out_of_range[ii])

                # print(" oor: ", new_stations_out_of_range[ii] )
                if short <= 0:
                    continue

                if short > k:
                    return False
                k -= short
                """
                r=1
                0 1 2 3 4 5
                i ^
                      ^
                """
                added_stations += short
                new_stations_out_of_range[ii+2*r+1] += short

            return True

        # now binary search the max(min-powered city)
        ll, rr, ans = 0, pow(10, 32), -1

        while ll <= rr:
            mm = ll+(rr-ll)//2
            # make a copy to avoid nums being modified in helper
            if isokay(mm, r, k, nums[:]):
                ans = mm
                ll = mm+1
            else:
                rr = mm-1

        return int(ans)


##################################################
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
