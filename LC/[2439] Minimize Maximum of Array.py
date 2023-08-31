class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        1. array size 10^5 -> nlogn time 
        2. sort, binary search, greedy
        * we cannot sort as the order matters
        """

        N = len(nums)

        ll, rr = nums[0], max(nums)
        ans = -1
        while ll <= rr:
            # print(" ll: ", ll, " rr: ", rr, " ans: ", ans)
            mm = ll+(rr-ll)//2
            # can mm be the min max value?
            buffer = 0
            flag = True
            for ii in range(N):
                buffer += (mm-nums[ii])
                # print("mm: ", mm, "ii: ", ii, " buffer: ", buffer)
                if buffer < 0:
                    flag = False
                    break

            if flag:
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans
