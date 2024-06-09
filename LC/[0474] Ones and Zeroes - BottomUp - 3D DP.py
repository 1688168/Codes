class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N=len(strs)
        rcs=[]
        for ss in strs:
            zz=0
            oo=0
            for cc in ss:
                if cc=='0': zz+=1
                if cc=='1': oo+=1
        
            rcs.append((zz, oo))
    
        # declare DP
        dp=[[[0]*(n+1) for _ in range(m+1)] for _ in range(N)]

        # initialize DP
        """
        this is counting num of ways to reach end. so zero is the expected default value. no additional action required
        """

        for ii in range(N): # for each string
            zz, oo= rcs[ii]            
            for jj in range(m+1): # jj is zero count
                for kk in range(n+1): # kk is one count
                    if ii==0 and jj >= zz and kk >= oo:
                        dp[ii][jj][kk]=1
                        continue
                    
                    if jj < zz or kk < oo:
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]
                    else:
                        dp[ii][jj][kk] = max(dp[ii][jj][kk], 1+dp[ii-1][jj-zz][kk-oo], dp[ii-1][jj][kk])
        
        #print(dp)
        return dp[-1][-1][-1]


# class Solution:
#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         # pre-processing resources
#         N=len(strs)
#         rcs=[]
#         for ss in strs:
#             zz=0
#             oo=0
#             for cc in ss:
#                 if cc=='0': zz+=1
#                 if cc=='1': oo+=1
#             rcs.append((zz, oo))


#         dp=[[0]*(n+1) for _ in range(m+1)]

#         # initialize dp on prev resource
#         # when @ resource[-1], number of subset is all zero so no need to initialize

#         for kk in range(N): # for each resource, how can we get to here from previous resource
#             zz, oo = rcs[kk]
#             for ii in reversed(range(zz, m+1)):     # use reversed order to avoid copy the dp for prev status
#                 for jj in reversed(range(oo, n+1)): # use reversed order to avoid copy the dp for prev status
#                     dp[ii][jj] = max(dp[ii][jj], 1+dp[ii-zz][jj-oo])
#             print(dp)

#         return dp[-1][-1]