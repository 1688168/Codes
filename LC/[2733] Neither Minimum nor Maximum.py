class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        ans=-1
        mxSoFar=-1
        mnSoFar=float('inf')
        N=len(nums)
        if N <= 2: return ans

        for n in nums:
            mxSoFar = max(mxSoFar, n)
            mnSoFar = min(mnSoFar, n)

            if n != mxSoFar and n != mnSoFar: return n

        for n in nums:
            if n != mxSoFar and n != mnSoFar: return n

        return ans