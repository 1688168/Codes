class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        : fix ii, shrink jj, kk range to find the min diff
        : ii, jj, kk
        : N*N=> O(N^2)
        """
        nums.sort()
        N=len(nums)
        mnd=float('inf')
        mns=float('inf')

        for ii in range(N):
            ll, rr = ii+1, N-1
            while ll < rr:
                a3sum=nums[ii]+nums[ll]+nums[rr]
                diff = abs(a3sum-target)
                if diff == 0:
                    return a3sum

                if diff < mnd:
                    mnd=diff
                    mns=a3sum

                if a3sum > target:
                    rr-=1
                else:
                    ll+=1



        return mns
