class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        * no 3 posts with same colors
        => num of ways
        # Analysis:
        * N=50, k=10^5
        * Bruteforce by searching: k branches: k^N
        * Try DP: 
          current state is depending on previous two posts
  
        """
        N=n

        if N==1: return k     
        same=k
        diff=k*(k-1)

        if N==2: return same+diff

        for ii in range(3, N+1):
            same_tmp=same
            diff_tmp = diff
            same = diff_tmp
            diff = same_tmp*(k-1)+diff_tmp*(k-1) #because the last two need to be diff so (k-1) options
        
        return same+diff

        