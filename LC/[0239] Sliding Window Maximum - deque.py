from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        mxq = deque()
        N = len(nums)
        res = []

        """
        1, 2, 3,   4, 5; k=3
           ^ 
                   ^
           ii-k+1  ii
        the window is (ii-k+1, ii)            
        """

        for ii in range(N):

            while len(mxq) > 0 and nums[ii] >= nums[mxq[-1]]:
                mxq.pop()

            mxq.append(ii)

            if (ii-k+1) >= 0:  # we have the window of size k
                res.append(nums[mxq[0]])
                if len(mxq) > 0 and mxq[0] <= (ii-k+1):
                    mxq.popleft()

        return res


# leetcode submit region end(Prohibit modification and deletion)
