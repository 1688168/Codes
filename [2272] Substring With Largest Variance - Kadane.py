class Solution:

    def largestVariance(self, s: str) -> int:
        # char instance count is like converting char array to 1,0 array
        # ababab => 101010
        # count of a => subarray sum of 1
        # the diff of two chars is like make a=1, b=-1
        # => max subarray sum anchoring on a -1 to maximize the variance

        # all given chars
        ctr = Counter(s) # O(N)

        mxv = 0
        # construct all potential pairs of the given chars
        #chrs = [k for k in ctr.keys()]
        # chrs.sort()
        pairs = []
        for x in ctr.keys():

            for y in ctr.keys():
                if x == y: continue
                pairs.append((x, y))

        # pp(pairs)
        dp1 = [0] * len(s)
        # dp2=[0]* len(s)
        dp = 0

        for x, y in pairs:  # traverse each pair
            nums = [0] * len(s)  # make up the 1,0 -1 array
            for ii in range(len(s)):
                if s[ii] == x: nums[ii] = 1
                if s[ii] == y: nums[ii] = -1
            # dp1 is subarray sum ending @ ii
            dp1[0] = nums[0] # setup for Kadane's algorithm for max subarray sum
            for ii in range(1, len(s)):
                dp1[ii] = max(dp1[ii - 1] + nums[ii], nums[ii])

            # pp(dp1)
            lmv = float('-inf')

            # dp is max subarray sum from right, reduced to single var
            dp = nums[-1]
            if nums[-1] == -1: # reversed kadane's algorithm
                lmv = max(lmv, dp1[-1] + dp - nums[-1])

            for ii in reversed(range(len(s) - 1)): #going reversed
                dp = max(dp + nums[ii], nums[ii])

                if nums[ii] == -1:#centering on -1 for max variance
                    lmv = max(lmv, dp1[ii] + dp - nums[ii])

            mxv = max(lmv, mxv)

        return mxv
