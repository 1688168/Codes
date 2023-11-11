############
# 20231111
############
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        cnt ending at ii = (1 if presum[ii]== k else 0) + presum_k[curr_sum-k]

        if presum[jj]=curr_sum-k where jj < ii (ii is current sum)
        curr_sum - presum[jj] = curr_sum-curr_sum+k = k  
        """
        N = len(nums)

        cnt = 0
        presum_cnt = defaultdict(int)
        curr_sum = 0
        for ii, vv in enumerate(nums):
            curr_sum += vv
            cnt += ((1 if curr_sum == k else 0) +
                    presum_cnt.get(curr_sum-k, 0))
            presum_cnt[curr_sum] += 1

        return cnt


#########################
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        : first of all, you have to realize that the fucking sliding window strategy won't work here as num[ii] could be negative
        : you cannot assume increasing sum of array range will increase "sum"
        : the heuristic is: num of subarrays ending @ ii that sum to k is equal to
        : 1 if sum(0:ii)==k else 0 + num of presum(jj) equal to (curr_sum-k) where jj < ii (current index)
        : remember:
                    presum(ii)-presum[jj]=sum(jj+1:ii)
        :           if presum[jj]==curr_sum-k
                       presum(ii)==curr_sum
                    => presum(ii)-presum[jj]= curr_sum - (curr_sum-k)= k
        """
        # in one loop, accuA, check cnt, append new accuNum
        cnt = 0
        presum_cnt = {}
        curr_sum = 0
        for n in nums:
            curr_sum += n
            cnt += ((1 if curr_sum == k else 0) +
                    presum_cnt.get(curr_sum-k, 0))
            presum_cnt[curr_sum] = presum_cnt.get(curr_sum, 0) + 1
        return cnt
