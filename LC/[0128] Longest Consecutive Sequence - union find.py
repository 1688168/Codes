from collections import defaultdict
class Solution:
    def __init__(self):
        self.child2father={}

    def longestConsecutive(self, nums: List[int]) -> int:

        def findFather(x):
            if self.child2father[x] != x:
                self.child2father[x]=findFather(self.child2father[x])
            return self.child2father[x]

        def union(x, y):
            x=self.child2father[x]
            y=self.child2father[y]
            if x <= y:
                self.child2father[y]=x
            else:
                self.child2father[x]=y

        N=len(nums)
        if N==0: return 0

        for ii in range(len(nums)):
            x=nums[ii]
            self.child2father[x]=x


            if (x-1) in self.child2father and findFather(x-1) != findFather(x):
                union(x-1, x)
            if (x+1) in self.child2father and findFather(x) != findFather(x+1):
                union(x, x+1)


        """
        : x's parent is y, and later y's parent is w. we need to updatex's real ancestor is w here
        : x -> y -> w <- z
        """
        for x in nums:
            self.child2father[x]=findFather(x)

        """
        : collect all family together in a list so we know the size
        """
        ancestor2members=defaultdict(set)
        mxl=0
        for x in nums:
            ancestor2members[findFather(x)].add(x)
            mxl=max(mxl, len(ancestor2members[findFather(x)]))

        return mxl
