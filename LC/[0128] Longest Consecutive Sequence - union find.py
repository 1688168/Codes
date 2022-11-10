########
# 20221108
########
from collections import defaultdict
class Solution:

    def __init__(self):
        self.c2f={} #child 2 father

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        all numbers in consecutive sequence will share the same smallest number
        -> union/find
        * union all n in nums in same group that shares the same smallest number
        * the largest group  (group size) is the length of the longest consecutive seq.
        """
        def findFather(x):

            if x in self.c2f and x!= self.c2f[x]:
                self.c2f[x]=findFather(self.c2f[x])
            else:
                self.c2f[x]=x

            return self.c2f[x]

        def union(x, y):
            fx=self.c2f[x]
            fy=self.c2f[y]

            if fx<=fy:
                self.c2f[y]=fx
            else:
                self.c2f[x]=fy

        for n in nums: #initialize the c2f to self
            self.c2f[n]=n

            # is n-1 existing? -> union
            if n-1 in self.c2f:
                union(n-1, n)

            # is n+1 existing? -> union
            if n+1 in self.c2f:
                union(n+1, n)

        # normalize the unions.
        for n in nums:
            self.c2f[n]=findFather(n)

        # realign the ancestors
        f2children=defaultdict(set)
        mxl=0
        # group the ancestors
        for n in nums:
            #ancestor=findFather()
            f2children[findFather(n)].add(n)
            mxl=max(mxl, len(f2children[findFather(n)]))

        # return the largest size

        return mxl
##########################################
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
