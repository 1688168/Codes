# 20230823
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # for each element as the right end of the sub-array, how many subarrays satisfy the fixed bound?
        ans=0
        boundary=minKi=maxKi=-1
        for ii, vv in enumerate(nums):
            if vv > maxK or vv < minK: 
                boundary=ii
                continue

            if vv == minK: minKi=ii
            if vv == maxK: maxKi=ii

            ans += max(0, min(minKi, maxKi)-boundary)

        
        return ans


#####################
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        : => border x x x minK x x maxk x x  ii << the min fixed-bond subarray ending @ ii
        : => how many more can above expand?
        : => border is an index with value where value < minK or value > maxK
        """

        border_idx=-1
        mnki = -1
        mxki = -1

        N=len(nums)

        cnt=0
        for ii in range(N):
            if nums[ii]==minK:
                mnki=ii

            if nums[ii]==maxK:
                mxki=ii


            if nums[ii] < minK or nums[ii] > maxK:
                border_idx=ii

            cnt += max(0, min(mnki, mxki)-border_idx)


        return cnt
