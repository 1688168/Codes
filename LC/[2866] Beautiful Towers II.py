class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        """
        left_peak[ii] = ttl height for all building ending @ ii conforming to the rules
        right_peak[ii] = ttl height for all building starting @ ii to the end conforming to the rules

        peak[ii] = left_peak[ii]+right_peak-maxHeight (remember maxHeight is counted twice)

        * how do we find the left peak?
        * application of monotonic stack

  ii    0 1 2 3 4 5 6 7 8
        1 3 5 7 9 4 3 2 1
  ii=6

  stk  [0,1, 5]
  so when we pop 4, we need to substract (5-1)*height[5] 
                               add       (6-1)*peak[6]
        """
        N = len(maxHeights)
        left = [0]*N
        right = [0]*N

        def helper(arr):
            stk = []
            ttl = 0
            for ii in range(N):
                if ii == 0:
                    ttl += maxHeights[ii]
                    stk.append(ii)
                    arr[ii] = ttl
                    continue

                while len(stk) > 0 and maxHeights[ii] < maxHeights[stk[-1]]:
                    p2 = stk[-1]
                    stk.pop()
                    p1 = -1 if len(stk) == 0 else stk[-1]
                    ttl -= (maxHeights[p2] * (p2-p1))
                    ttl += (maxHeights[ii] * (p2-p1))
                ttl += maxHeights[ii]
                stk.append(ii)
                arr[ii] = ttl

        helper(left)

        maxHeights.reverse()
        helper(right)
        right.reverse()
        maxHeights.reverse()

        mx = 0
        for ii in range(N):
            mx = max(mx, left[ii]+right[ii]-maxHeights[ii])

        return mx
