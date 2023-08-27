class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N=len(nums)
        pre_sum=[0]*N 
        for ii, vv in enumerate(nums):
            if ii==0:
                pre_sum[ii]=nums[ii]
            else:
                pre_sum[ii]=nums[ii]+pre_sum[ii-1]
        
        ll=0
        ans = 0
        for ii, vv in enumerate(nums): #for each element as subarray end
            length=ii-ll+1
            _sum=pre_sum[ii] - (pre_sum[ll-1] if ll > 0 else 0)
            score=length*_sum
            
            while ll <= ii and score >= k:
                ll += 1
                length=ii-ll+1
                _sum=pre_sum[ii] - (pre_sum[ll-1] if ll > 0 else 0)
                score=length*_sum
            
            if score < k:
                ans += ii-ll+1

        return ans

