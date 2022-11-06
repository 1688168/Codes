class Solution:
    def threeSumClosest(self, nums: List[int],
                        target: int) -> int:
        """
        1. sort the input array
        2. traverse the sorted array to fix the 1st int
        3. try all combination of two sum to capture whoever is closest to target
        4.
        """
        # take the dimentions
        N=len(nums)
        nums.sort()

        diff=float('inf')
        mns=float('inf')
        for ii in range(N):#anchor first element
            ll=ii+1
            rr=N-1
            while ll < rr:
                _3sum=nums[ii]+nums[ll]+nums[rr]

                if _3sum-target==0:
                    return target
                if abs(_3sum-target) < diff:
                    diff=abs(_3sum-target)
                    mns=_3sum

                if _3sum > target:
                    rr-=1
                else:
                    ll+=1
        return mns





        
