class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        1. naive: O(NK)
        2. sorted_list: O(nlogk)
        3. monotone queue: o(N)
        """
        dq = collections.deque()

        res = []
        for ii, nn in enumerate(nums):
            # dq maintain the largest in the front and maintained the sequence
            while dq and nums[dq[-1]] <= nn:
                dq.pop()

            dq.append(ii)

            # remove those that is expired
            while dq and dq[0] <= ii-k:
                dq.popleft()

            # output the max if in scope
            if ii >= k-1 and dq:
                res.append(nums[dq[0]])

        return res
