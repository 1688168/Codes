class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char2loc={}

        st, ed=0, 0
        N=len(s)
        
        mxl=0
        for ed in range(N):
            cc=s[ed]
            if cc in char2loc:
                prev_loc=char2loc[cc]

                for ii in range(st, prev_loc):
                    del char2loc[s[ii]]
                char2loc[cc]=ed
                st=prev_loc+1
            else:
                char2loc[cc]=ed

            mxl=max(mxl, ed-st+1)

        return mxl
