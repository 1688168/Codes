class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        * n: posts
        * k: colors
        * no 3 consecutive posts with same color
        => num of ways to paint
        * N=50
        * K=10^5
        """
        N=n
        def dfs(prev, prev_prev, st):
            if st>=N: return 1

            cnt=0
            for kk in range(1, k+1):
                if kk != prev or kk != prev_prev:
                    cnt += dfs(kk, prev, st+1)
        
            return cnt


        return dfs(None, None, 0)
        