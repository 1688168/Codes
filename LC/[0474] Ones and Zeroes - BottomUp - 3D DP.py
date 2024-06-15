################
# 20240615
################
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        * single array with limitations m, n
        -> size of largest subset
        * subset -> take or skip
        """
        s2cnt=[] # (zero_cnt, one_cnt )
        for ss in strs:
            zero=0
            one=0
            for cc in ss:
                if cc=='0': zero +=1
                if cc=='1': one += 1
            
            s2cnt.append((zero, one))
        
        N=len(strs)
        dp=[[[0]*(n+1) for _ in range(m+1)] for _ in range(N)]

        for ii in range(N): #ii is the idx of nums
            zz, oo = s2cnt[ii]
            for jj in range(m+1): # jj is number of zero
                for kk in range(n+1): # kk is number of ones
                    if ii==0:
                        if jj >= zz and kk >= oo: dp[ii][jj][kk]=1
                        continue
                    #skip
                    dp[ii][jj][kk] = max(dp[ii][jj][kk], dp[ii-1][jj][kk])

                    #take               
                    if jj-zz >=0 and kk-oo >=0:
                        dp[ii][jj][kk] = max(dp[ii][jj][kk], dp[ii-1][jj-zz][kk-oo]+1)
        return dp[-1][-1][-1]
###############################
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N=len(strs)
        rcs=[]
        for ss in strs: #transforming the given resource to required measurements
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
                    if ii==0 and jj >= zz and kk >= oo: #special handing ii=0 to avoid (ii-1) idx out of bound error
                        # for ii=0, we have at least zz zero and oo ones. anything before zz, oo is zero
                        dp[ii][jj][kk]=1
                        continue
                   
                    if jj < zz or kk < oo: # if we cannot fitting in current num, make the dp copy from previous status
                        dp[ii][jj][kk] = dp[ii-1][jj][kk]
                    else:
                        # consider (current, tke, nte) scenarir
                        dp[ii][jj][kk] = max(dp[ii][jj][kk], 1+dp[ii-1][jj-zz][kk-oo], dp[ii-1][jj][kk])
                        #                                                              ^^^^^^^^^^^^^^^^^^^^
                        #                                                              not taking current
        
        #print(dp)
        return dp[-1][-1][-1]

