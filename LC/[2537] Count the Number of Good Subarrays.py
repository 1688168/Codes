class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        """
        x x x x x
        i
            j
        * if a number shows m times:
        -> pairs=m*(m-1)/2
        """
        N = len(nums)
        jj=0

        ttl=0
        num2cnt={}

        def diff(num2cnt, nn, val):
            old_cnt=num2cnt.get(nn, 0)
            old_pairs=old_cnt*(old_cnt-1)//2
            new_cnt=old_cnt+val
            new_pairs=new_cnt*(new_cnt-1)//2

            return new_pairs-old_pairs

        ans=0
        for ii in range(N): #for each new sliding window start
            while jj < N and ttl < k:
                ttl += diff(num2cnt, nums[jj], 1)
                num2cnt[nums[jj]] =num2cnt.get(nums[jj],0)+1
                jj+=1
            
            if ttl >= k:
                ans += (N-jj+1)

            # move left window border
            ttl += diff(num2cnt, nums[ii], -1)
            num2cnt[nums[ii]] -= 1


        return ans

