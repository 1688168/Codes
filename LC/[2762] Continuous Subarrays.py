from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans=0
        dq_max=deque() # maintain max in the sliding window
        dq_min=deque() # maintain min in the sliding window

        # sliding window boundary
        ll, rr, N = 0, 0, len(nums)

        # for each window right-end rr, calc the qualified continuous array
        for rr in range(N):
            # maintain window max/min
            while len(dq_max) > 0 and nums[rr] > nums[dq_max[-1]]: dq_max.pop()
            dq_max.append(rr)
            
            while len(dq_min) > 0 and nums[rr] < nums[dq_min[-1]]: dq_min.pop()
            dq_min.append(rr)

            # adjust sliding window to be qualifed continuous array
            while len(dq_max) > 0 and len(dq_min) > 0 and (nums[dq_max[0]]-nums[dq_min[0]]) > 2:
                while len(dq_max)> 0 and ll >= dq_max[0]: dq_max.popleft()
                while len(dq_min)> 0 and ll >= dq_min[0]: dq_min.popleft()
                ll+=1
            
            ans += (rr-ll+1)

        return ans