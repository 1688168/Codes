class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        offset = 5000
        dp=[-1]*(2*offset+1) #[-5000, 5000], "-1" indicate no left/right can make the diff
        dp[0+offset]=0
        N=len(rods)
        for ii, ll in enumerate(rods): # [0, N-1] - for each rod
            dp_old = copy.deepcopy(dp)
            for diff in range(-offset, offset+1, 1):
                if dp_old[diff+offset]==-1: continue
                # add to left
                if diff+ll<=offset:         
                    dp[diff+ll+offset] =  max(dp[diff+ll+offset], dp_old[diff+offset]+ll)

                # add to right
                if diff-ll >= -offset:
                    dp[diff-ll+offset] = max(dp[diff-ll+offset], dp_old[diff+offset]-ll)

        return dp[0+offset]