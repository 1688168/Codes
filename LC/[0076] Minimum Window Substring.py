from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m < n: return ""

        ll, rr = 0, 0
        matched=0
        char2cnt=Counter(t)

        mnl=float('inf')
        mns=""
        
        """
        ADOBECODEBANC
        ^^^^^^
        l    r
        ABC

        """

        for rr in range(m):
            c=s[rr]

            char2cnt[c] = char2cnt.get(c, 0) -1

            if char2cnt[c]>=0: matched += 1
            #print("mnl: ", mnl, " mns: ", mns)
            while ll< m and matched == n:
                if rr-ll+1 < mnl:
                    mnl=rr-ll+1
                    mns=s[ll:rr+1]
                prev=s[ll]

                char2cnt[prev] +=1
                if char2cnt[prev] > 0: matched -= 1

                ll+=1

        return mns
