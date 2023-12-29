###############
# 20231229
###############
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        - shortest: BFS
        - N: 10^4 --> O(N)?
        => "length" of the unsorted subarray

        ** bruteforce: 
        1. all subarray: O(N^2) -- A
        2. is sorted: O(N)  -- B
        --> A*B
        ** ideas0:
        * the beginning index of the violation subarray
        -> first index smaller than max_so_far from the left

        * the ending index of the violation subarray
        -> first index greater than min_so_far from the right

        =>  end_index-begin_index+1

        ** ideas1:
        x x x x x x x
        * find first ii who's next smaller is not @ N
        * find last ii who's prev greater is not @ -1
        * the distance is the answer

        - the beginning index is the first ii who's next smaller is not @ N
        - the ending index is the last ii who's prev greater is not @ -1

        ** next smaller/prev smaller/greater -> two monotonic stack
        1. build next_smaller
        2. build prev_greater

        """
        N = len(nums)

        # build next_smaller
        next_smaller = [N]*N
        stk = []
        for ii, nn in enumerate(nums):
            while stk and nums[stk[-1]] > nn:
                next_smaller[stk[-1]] = ii
                stk.pop()

            stk.append(ii)

        # build prev_greater
        prev_greater = [-1]*N
        stk = []
        for ii, nn in enumerate(nums):
            while stk and nums[stk[-1]] <= nn:
                stk.pop()

            if stk:
                prev_greater[ii] = stk[-1]

            stk.append(ii)

        # starting index: first idx that has next smaller not @ N
        for st in range(N):
            if next_smaller[st] != N:
                break

        # ending index: first idx that has prev_greater not @ -1
        for ed in reversed(range(N)):
            if prev_greater[ed] != -1:
                break

        if st == N-1:
            return 0

        return ed-st+1


##############################
##############################
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        prev_greater = [-1]*N
        next_smaller = [N]*N

        stk = []
        for ii, vv in enumerate(nums):
            while stk and nums[stk[-1]] > vv:
                next_smaller[stk[-1]] = ii
                stk.pop()

            stk.append(ii)
        stk = []
        for ii in reversed(range(N)):
            while stk and nums[stk[-1]] < nums[ii]:
                prev_greater[stk[-1]] = ii
                stk.pop()
            stk.append(ii)

        ll, rr = 0, N-1
        # no one on your right is smaller than you
        while ll < N and next_smaller[ll] == N:
            ll += 1
        # no one on your left is greater than you
        while rr >= 0 and prev_greater[rr] == -1:
            rr -= 1

        return 0 if rr <= ll else rr-ll+1
