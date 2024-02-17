#######
# 20240217
#######

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        two pointers and see the distance of pointer same as the unique count?
        if less, shift the window until the window can continue to grow bigger
        -> return the window size
        """
        ll=rr=0
        N=len(s)
        char2cnt=collections.defaultdict(int)
        """
        abcabcbb
        """
        if s=="": return 0
        for rr in range(N):
            dist=rr-ll+1
            char2cnt[s[rr]] += 1
            if dist > len(char2cnt): # has duplicate
                char2cnt[s[ll]] -=1
                if char2cnt[s[ll]] == 0: del char2cnt[s[ll]]
                ll+=1
        
        return rr-ll+1
        


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
