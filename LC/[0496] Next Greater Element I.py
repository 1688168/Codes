class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        nums1 <=nums2
        """

        # review edge cases
        # check inputs

        # build hash table of nums2 location
        # build lookup talbe for next greater

        v2idx={} # given a value in nums1, what's the index of same value into nums2
        for ii, vv in enumerate(nums2):
            v2idx[vv]=ii

        # build next greater lookup table
        N=len(nums2)
        next_greater=[-1]*N

        stack=[]
        for ii, vv in enumerate(nums2):
            while len(stack) > 0 and vv >nums2[stack[-1]]:
                next_greater[stack[-1]]=ii
                stack.pop()

            stack.append(ii)

        res=[]
        for ii, vv in enumerate(nums1):
            idx=v2idx.get(vv, -1)
            if idx==-1:
                res.append(-1)
            else:
                ans=next_greater[idx]
                if ans==-1:
                    res.append(-1)
                else:
                    res.append(nums2[ans])

        return res
        
