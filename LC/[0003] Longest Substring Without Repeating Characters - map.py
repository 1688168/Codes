class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll=rr=0
        char2idx={}
        N=len(s)

        mxl=0
        for rr in range(N):
            rchar=s[rr]
            if rchar in char2idx:
                ll=max(ll, char2idx[s[rr]]+1)

            char2idx[rchar]=rr

            mxl=max(mxl, rr-ll+1)


        return mxl


            
