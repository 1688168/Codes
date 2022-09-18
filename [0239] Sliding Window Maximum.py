# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 11896 👎 384


# leetcode submit region begin(Prohibit modification and deletion)?""""""""""""""""""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Given a window size k for an nums array.  moving the window from left to right and output the max num in the
        window
        * if we scan the array on each move: O(n*k)
        * leverage deque
        :param nums:
        :param k:
        :return:
        """
        mxq=deque()
        N=len(nums)
        res=[]

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


            if (ii-k+1) >= 0: # we have the window of size k
                res.append(nums[mxq[0]])
                if len(mxq)>0 and mxq[0] <= (ii-k+1):
                    mxq.popleft()

        return res




        
# leetcode submit region end(Prohibit modification and deletion)
