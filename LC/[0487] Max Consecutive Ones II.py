class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxl=0
        mxl_flipped=0
        mxl_unflipped=0

        for nn in nums:
            if nn==0:
                mxl_flipped = mxl_unflipped+1
                mxl_unflipped = 0
            else:
                mxl_flipped +=1
                mxl_unflipped +=1
            
            mxl=max(mxl, mxl_flipped, mxl_unflipped)
        
        return mxl
        