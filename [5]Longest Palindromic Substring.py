class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxl=0
        mxs=""
        N=len(s)

        if len(s)==1:
            return s

        for ii in range(N):
            l1=1
            jj, kk = ii, ii

            while jj >=0 and kk < N and s[jj]==s[kk]:
                ll=kk-jj+1
                if ll > mxl:
                    mxl=ll
                    mxs=s[jj:kk+1]
                jj-=1
                kk+=1


            jj, kk=ii-1, ii
            while jj >=0 and kk < N and s[jj]==s[kk]:

                ll=kk-jj+1
                if ll > mxl:
                    mxl=ll
                    mxs=s[jj:kk+1]
                jj-=1
                kk+=1


        return mxs
        
