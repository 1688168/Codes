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

##########
# 20221029
##########
class Solution:
    def longestPalindrome(self, s: str) -> str:

        N=len(s)
        mxl=0
        mxs=""

        for ii in range(N):
            #anchor on each char
            # case 1: center
            if ii > 0:
                jj=ii-1
                kk=ii+1
                while jj >=0 and kk <N and s[jj]==s[kk]:
                    if kk-jj+1 > mxl:
                        mxl=kk-jj+1
                        mxs=s[jj:kk+1]
                    jj-=1
                    kk+=1
            else:
                mxl=1
                mxs=s[0]

            # case 2: pair
            jj=ii+1
            kk=ii
            while jj < N and kk >=0 and s[kk]==s[jj]:
                if jj-kk+1 > mxl:
                    mxl=jj-kk+1
                    mxs=s[kk:jj+1]

                kk-=1
                jj+=1

        return mxs
