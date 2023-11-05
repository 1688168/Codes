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
        while ll < N and next_smaller[ll] == N: #no one on your right is smaller than you
            ll += 1
        while rr >= 0 and prev_greater[rr] == -1: # no one on your left is greater than you
            rr -= 1

        return 0 if rr <= ll else rr-ll+1
