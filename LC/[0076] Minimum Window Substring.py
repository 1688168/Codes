from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        """
        ans=""

        #check edge case
        m=len(s)
        n=len(t)
        if m < n: return ""
        char2cnt=Counter(t)
        #origChars=set(list(t))
        st, ed=0,0
        mnl=m+1
        matched=0

        """
        s a a t t t t s s s s
        s t s
        i
                      j
        """
        for ed in range(m):
            #print("ed: ", ed, " st: ", st)
            curr=s[ed]
            if curr in char2cnt:
                char2cnt[curr]=char2cnt.get(curr, 0)-1
                if char2cnt[curr]>=0:
                    #del char2cnt[curr]
                    matched+=1
            #print("matched: ", matched, " st: ", st, " ed: ", ed, " ans: ", ans)
            # if matched==n: #s covers t
            #     mnl=ed-st+1
            #     ans=s[st:ed+1]
            while st<= ed and matched==n: #we found a window, can we shrink
                #print(" inner st: ", st)
                if ed-st+1 < mnl:
                    mnl=ed-st+1
                    ans=s[st:ed+1]
                prev=s[st]
                st+=1
                if prev in char2cnt:
                    char2cnt[prev]=char2cnt.get(prev, 0)+1
                    if char2cnt[prev] > 0:
                        matched -=1


        return ans
