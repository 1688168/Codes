#######
# 20230625
#######

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        a b c a b c b b
                      r
                  l 

        p w w k e w
                r
            l   
        """

        N = len(s)
        ll = 0
        char2idx = {}
        mxl = min(N, 1)
        for rr, cc in enumerate(s):
            if cc not in char2idx or char2idx[cc] < ll:
                mxl = max(mxl, rr-ll+1)
                char2idx[cc] = rr

            else:
                ll = max(ll, char2idx[cc]+1)
                char2idx[cc] = rr
            # print("ll: ", ll, " rr: ", rr, " mxl: ", mxl)

        return mxl


#############


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll = rr = 0
        char2idx = {}
        N = len(s)

        mxl = 0
        for rr in range(N):
            rchar = s[rr]
            if rchar in char2idx:
                ll = max(ll, char2idx[s[rr]]+1)

            char2idx[rchar] = rr

            mxl = max(mxl, rr-ll+1)

        return mxl
