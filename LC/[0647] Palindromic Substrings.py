class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        cnt=0
        for ii in range(N): # for each starting point
            # odd case
            cnt += 1
            jj=ii-1
            kk=ii+1
            while jj>=0 and kk < N and s[jj]==s[kk]:
                cnt +=1
                jj-=1
                kk+=1

            jj=ii
            kk=ii+1
            while jj >=0 and kk < N and s[jj]==s[kk]:
                cnt +=1
                jj-=1
                kk+=1

        return cnt

        
