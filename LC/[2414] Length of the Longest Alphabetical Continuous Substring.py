class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        st, ed, N = 0, 1, len(s)

        mxl=1
        for ed in range(1, N):
            if ord(s[ed])-ord(s[ed-1]) != 1:
                st=ed
            mxl=max(mxl, ed-st+1)


        return mxl
