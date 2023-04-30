"""
20.5%
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Case I: if 1 is existing in nums
        N=len(nums)
        NumOfOnes = len([1 for _ in nums if _==1]) # space O(N)

        if NumOfOnes > 0:
            return N-NumOfOnes

        # case II: no 1 existing -> find the smallest subarray that we can produce a 1
        mnl=math.inf

        for ll in range(2, N+1): # O(N^2)
            for ii in range(N):
                if math.gcd(*nums[ii:ii+ll])==1:                    
                    return ll-1 + N - 1 
        
        return -1


"""
10.71%
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Case I: if 1 is existing in nums
        N=len(nums)
        NumOfOnes = len([1 for _ in nums if _==1])

        if NumOfOnes > 0:
            return N-NumOfOnes

        # case II: no 1 existing -> find the smallest subarray that we can produce a 1
        mnl=math.inf

        for ii in range(N):
            g=nums[ii]
            for jj in range(ii+1, N):
                if (g:=math.gcd(g, nums[jj])) == 1:
                    mnl = min(mnl, jj-ii+1)
        return mnl -1 + N - 1 if mnl != math.inf else -1

"""
10.11%
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        # Case I: if 1 is existing in nums
        N=len(nums)
        NumOfOnes = len([1 for _ in nums if _==1]) # space O(N)

        if NumOfOnes > 0:
            return N-NumOfOnes

        # case II: no 1 existing -> find the smallest subarray that we can produce a 1
        mnl=math.inf

        for ii in range(N): # O(N^2)
            for jj in range(ii+1, N):
                #if (g:=math.gcd(g, nums[jj])) == 1:
                if math.gcd(*nums[ii:jj+1])==1:
                    mnl = min(mnl, jj-ii+1)
        return mnl -1 + N - 1 if mnl != math.inf else -1