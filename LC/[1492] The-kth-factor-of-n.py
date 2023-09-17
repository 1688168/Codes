class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans=-1
        cnt=0
        for ii in range(1, n//2+1):
            if n%ii==0: cnt += 1
            if cnt == k: return ii
        
        if cnt+1==k: return n

        return ans
        