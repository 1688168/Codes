from bisect import bisect_right
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        - How to maximize the product of nums 
          where size(nums) is not fixed
                sum(sums)+k is fixed
        => try to make the elements equal
        a1+a2+a3+...+an = S

        maximize a1*a2*a3*...*an => a1==a2==a3==s/n <<<<<
        
        s = 6
        (1,5)
        (2,4)
        (3,3) <<< max product

        a1+a2 = s
        a1*a2 = a1*(s-a1) = -a1^2 + S*a1 => a1=s/2 <<<< how to find the max value by calculus
              x
            x x 
          x x x
        x x x x
        ^^^^^
          p   p+1


        presum[p]+k/p <= nums[p+1]

        diff[ii]: what's the required K to make nums[:ii] all same height?
         >> diff[ii]=nums[ii]*ii-presum[ii]
         we are looking for diff[p] <= k
        """
        M=int(1e9)+7
        nums.sort()
        N=len(nums)
        presum=[0]*N
        for ii, vv in enumerate(nums):
            presum[ii] = (presum[ii-1] if ii > 0 else 0) + nums[ii]
            
        diff=[0]*N
        for ii, vv in enumerate(presum):
            diff[ii]=nums[ii]*(ii+1)-presum[ii]

        idx=bisect_right(diff, k) #how far can we fill by k to make equal?
        """
         idx can never be zero.  consider the definition of diff, 
         there is no elements before nums[0] and we do not need to invest 
         anything from k to make anything prior than nums[0] equal to nums[0]
        """
        idx-=1 #move to prev (the first smaller)

        ttl= presum[idx]+k
        each = ttl//(idx+1)
        extra = ttl % (idx+1) # or ttl-each*(idx+1)

        ret=1
        for ii in range(extra):
            ret=ret*(each+1)%M

        for ii in range(extra, idx+1):
            ret=ret*each%M
        
        for ii in range(idx+1, N):
            ret = ret * nums[ii] % M
        return ret