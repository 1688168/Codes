class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        # Naive solution
        - for each staring (s1[ii] == s2[0])
        - two pointer
        - greedy 

        # Time:
        - N1 + S*N1*N2
        """
        N1=len(s1)
        N2=len(s2)

        mnl = math.inf
        ret=""

        for ii in range(N1):
            if s1[ii]==s2[0]: # found a start
                st=ii
                ed=ii+1
                # we want to find all chars in S2 from s1[ii:]
                jj=1 #we are already @ a start: s1[ii]==s2[0]
                while jj<N2 and ed < N1:
                    if s1[ed] == s2[jj]: jj+=1
                    ed+=1

                if jj >= N2 and (ll:=ed-st+1) < mnl:
                    mnl=ll
                    ret = s1[st:ed]
                      
        return ret
        