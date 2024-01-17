############
# 20240113
############
from bisect import bisect_right
M = int(1e9)+7


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        """
        - nums: 
        - k: reource
        - max(product of nums): n1*n2*...
        => how to max two number with fixed ttl sum?
        ex: 6
        1 5=5
        2 4=8
        3 3=9 <<<

        ex: 9
        1 8=8
        2 7=14
        3 6=18
        4 5=20 <<<

        observation: try to make all numbers equal
        sort nums: 
        n1, n2, n3, ..., np, ..
        ^^^^^^^^^^^^^^^^^^^
        find p s.t. we can make equal

        """
        N = len(nums)  # take size

        # sort the list in increasing order
        nums.sort()

        # find an index(ii) s.t. we can make nums[jj] all equal where jj in [0, ii]
        # diff[ii] is the value you need to have nums[jj]=nums[ii] for all jj <= ii
        diff = [0]*N #with diff, we can use bisect to find p s.t. we can make even upto p
        presum = nums[0]
        for ii in range(1, N):
            presum += nums[ii]
            diff[ii] = nums[ii]*(ii+1)-presum

        # find the ii that we can fill with k
        idx = bisect.bisect_right(diff, k)
        # print("idx: ", idx)
        idx -= 1  # this is where we can fill all even with k

        ttl = sum(nums[:idx+1])+k
        # print(" ttl: ", ttl)
        each = ttl//(idx+1)
        # print(" each: ", each)
        extra = ttl % (idx+1)
        # print(" extra: ", extra)

        # print(" extra: ", extra)

        res = 1
        # calc product with remaining
        for ii in range(extra):
            res = res*(each+1) % M

        # calc product up to idx
        for ii in range(extra, idx+1):
            res = res*each % M

        # calc the rest
        for ii in range(idx+1, N):
            res = res*nums[ii] % M

        return res

###########################################


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
        M = int(1e9)+7
        nums.sort()
        N = len(nums)
        presum = [0]*N
        for ii, vv in enumerate(nums):
            presum[ii] = (presum[ii-1] if ii > 0 else 0) + nums[ii]

        diff = [0]*N
        for ii, vv in enumerate(presum):
            diff[ii] = nums[ii]*(ii+1)-presum[ii]

        idx = bisect_right(diff, k)  # how far can we fill by k to make equal?
        """
         idx can never be zero.  consider the definition of diff, 
         there is no elements before nums[0] and we do not need to invest 
         anything from k to make anything prior than nums[0] equal to nums[0]
        """
        idx -= 1  # move to prev (the first smaller)

        ttl = presum[idx]+k
        each = ttl//(idx+1)
        extra = ttl % (idx+1)  # or ttl-each*(idx+1)

        ret = 1
        for ii in range(extra):
            ret = ret*(each+1) % M

        for ii in range(extra, idx+1):
            ret = ret*each % M

        for ii in range(idx+1, N):
            ret = ret * nums[ii] % M
        return ret
