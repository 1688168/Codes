class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        N=len(nums)
        ans = 0
        nums.sort()
        def two_sum_less(idx, target):
            ttl=0

            for ii in range(idx, N-1):
                #print(" -- jj: ", ii)
                #find first jj that nums[ii]+nums[jj] < target
                ntg=target-nums[ii]
                ll, rr, ans = ii+1, N-1, -1
                if nums[ll]>=ntg: break  # understand how to optimize binary search
                while ll <= rr:
                    mm=ll+(rr-ll)//2
                    if nums[mm]<ntg:
                        ans=mm
                        ll=mm+1
                    else:
                        rr=mm-1

                #print(" ans: ", ans)
                if ans != -1:
                    ttl += (ans-ii)
                    #print(" added: ", ans-ii)

            return ttl

        for ii in range(N-2):
            #print("---- ii: ", ii)
            ans += two_sum_less(ii+1, target-nums[ii])

        return ans
