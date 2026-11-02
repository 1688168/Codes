class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N=len(s)
        ll = 0
        charToCount = Counter()
        mxl=0
        for rr in range(N):
            cc=s[rr]
            charToCount[cc] += 1
                
            while len(charToCount) > 2 and ll<=rr: # we need to shrink the window
                leaving_ch = s[ll]
                charToCount[leaving_ch] -= 1
                if charToCount[leaving_ch] == 0: del charToCount[leaving_ch]
                ll+=1

            mxl = max(mxl, rr-ll+1)

        return mxl


            