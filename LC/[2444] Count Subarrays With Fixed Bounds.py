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
