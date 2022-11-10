############
# 20221108
############
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)

        mxl=0
        for nn in nums:
            if nn-1 in nset: continue

            npp=nn
            cnt=0
            while npp in nset:
                cnt +=1
                npp+=1
            mxl=max(mxl, cnt)


        return mxl



#################################################
"""
: find consequence sequence from an unordered array in O(N)
: * comparison based sort won't work => bucket sort. (out of memory)
: * find an element that doesn't have smaller neighbor.
: + once identify an end node, find how far we can link based on this starting point and capture the length
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)

        mxc=0
        if len(nums)==0: return 0

        for n in nset:
            # identify the left end node
            if (n-1) not in nset:
                cnt=1
                n=n+1
                while (n) in nset:
                    n+=1
                    cnt += 1

                mxc=max(mxc, cnt)


        return mxc
