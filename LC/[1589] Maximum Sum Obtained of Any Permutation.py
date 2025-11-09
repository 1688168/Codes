class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N=len(nums)
        events = [0]*(N+1) #considering the ending is +1
        # 1. convert interval requests to events
        for (st, ed) in requests:
            events[st] += 1
            events[ed+1]-=1

        freq = [0]*N
        freq[0] = events[0]
        for ii in range(1, N):
            freq[ii] = freq[ii-1]+events[ii]
        
        freq.sort()
        nums.sort()

        M=pow(10, 9) + 7
        ttl=0
        for ii in range(N):
            ttl = (ttl + freq[ii]*nums[ii]%M)%M

        return ttl




"""
* requesting for a range -> range sum
* num of request is frequency on on an index
* the value of this index can produce -> freqXval
* we need to assing highest value to highest freq
* how to calc freq of request -> range request -> sweepline
"""
        
    