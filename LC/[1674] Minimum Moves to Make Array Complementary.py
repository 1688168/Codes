
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        N=len(nums) # this is an event number

        # collect all events: define all space or use map
        events=defaultdict(int)
        for ii in range(N//2): #only need to process half for pairs
            aa = min(nums[ii], nums[N-ii-1]) # (1, 2, 3, 4)
            bb = max(nums[ii], nums[N-ii-1])

            events[2] += 2
            events[aa+1] -= 1
            events[aa+bb] -= 1
            events[aa+bb+1] += 1
            events[bb+limit+1] += 1
        
        ret = float('inf')
        yy = 0
        for kk, vv in sorted(events.items()):
            yy += vv
            ret = min(ret, yy)
        
        return ret






"""
1. what's the X we can choose from limit to be the number -> traverse all x
2. min operations

* we know X can be any number < 10^5 -> try all of them and count required moves to output the min
> given an x, and a pair (a, b) where a < b. what's the required number of flip of this pair?
-> we are aiming: a+b=x
-> what are the turning points?

      2                1      0          1                     2
(2) --- (a+1) ---  (a+b-1) --- (a+b) --- (b+ a+1) --- (b+limit) --- (2*limits)

      2                1      0          1                     2
(2) --- (a+1) ---  (a+b-1) --- (a+b) --- (b+ a+1) --- (b+limit) --- (2*limits)

      2                1      0          1                     2
(2) --- (a+1) ---  (a+b-1) --- (a+b) --- (b+ a+1) --- (b+limit) --- (2*limits)

...
we will have n/2 interval functions. -> we need to add all of them together -> interval addition -> diff array (sweepline)
                
         
* we can partiion a+b to different interval and each interval requires diff number of flip given an x
* given an x, we know number of required flips we need for a pair interval., for all pairs -> we need to add all those intervals

"""
        
