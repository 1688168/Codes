class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        * can replace k for longest repeating string
        * rr-ll+1-max(cnt) <= k
        """
        ll, rr, N = 0, 0, len(s)

        char2cnt = {}
        mxl=0
        for rr in range(N):
            c=s[rr]
            char2cnt[c]=char2cnt.get(c, 0) + 1
            while rr-ll+1 - max(char2cnt.values()) > k:               
                char2cnt[s[ll]] -= 1
                ll += 1
            mxl=max(mxl, rr-ll+1)

        return mxl
