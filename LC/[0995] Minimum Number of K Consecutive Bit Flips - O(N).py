#######
# 20260126
#######
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N=len(nums)
        events=[0]*(N+1)
        count=0
        flip = 0
        for ii, vv in enumerate(nums):
            flip += events[ii] # num of flips before reaching current ii
            # the current value and num of flip determines if we should flit the curren bit
            # 1+0 or 0+1 -> no need to flip, everything else, we need to flip

            if(vv + flip%2)==1: continue
            flip += 1 # we need to flip
            count+=1
            if ii+k-1 >= N: return -1
            events[ii+k] -= 1

        return count
        

##############
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # the extra 1 is for ii+k+1 the ending index to substract
        diff = [0]*(N+1)

        flips = 0
        cnt = 0
        for ii, nn in enumerate(nums):
            flips += diff[ii]  # required flip per earlier operations
            if (nums[ii]+flips) % 2 == 1:
                continue  # after required flipping, if 1, continue
            if ii+k-1 >= N:
                return -1  # false condition
            flips += 1
            diff[ii+k] -= 1
            cnt += 1

        return cnt
