class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n2freq={}
        for n in nums:
            n2freq[n]=n2freq.get(n,0)+1

        mxv=0
        mxn=None
        for kk, vv in n2freq.items():
            if vv > mxv:
                mxv=vv
                mxn=kk
                if vv > len(nums)//2: return kk
        
        return mxn