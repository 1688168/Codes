class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # pre-processing resources
        N=len(strs)
        rcs=[]
        for ss in strs:
            zz=0
            oo=0
            for cc in ss:
                if cc=='0': zz+=1
                if cc=='1': oo+=1
            rcs.append((zz, oo))


        dp=[[0]*(n+1) for _ in range(m+1)]

        # initialize dp on prev resource
        # when @ resource[-1], number of subset is all zero so no need to initialize

        for kk in range(N): # for each resource, how can we get to here from previous resource
            zz, oo = rcs[kk]
            for ii in reversed(range(zz, m+1)):     # use reversed order to avoid copy the dp for prev status
                for jj in reversed(range(oo, n+1)): # use reversed order to avoid copy the dp for prev status
                    dp[ii][jj] = max(dp[ii][jj], 1+dp[ii-zz][jj-oo])

        return dp[-1][-1]

###############
