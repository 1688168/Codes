class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        N=len(nums) # k: 0~N
        mxScore=0

        # apply diff array strategy
        # 1. covnert each ii to events
        events=[0]*N
        for ii in range(N):
            if nums[ii] > ii:
                events[0] += 0 #self, no rotate
                events[(ii+1)%N] += 1 # rotate to the end
                events[(ii+1 + N-nums[ii])%N] -= 1
            else: # nums[ii] <= ii
                events[0] += 1 #rotate 0
                events[(ii-nums[ii]+1)%N] -= 1
                events[(ii+1)%N] += 1
        
        score = 0
        mxii = 0
        for kk in range(N):
            score += events[kk]
            if(score >mxScore):
                mxScore = score
                mxii=kk

        return mxii
    

# ii: 0 1 2 3 4 
# vv:       4
# ss: 0 0 0 0 1

# ii: 0 1 2 3 4 
# vv:     1 
# ss: 0 1 1 0 0