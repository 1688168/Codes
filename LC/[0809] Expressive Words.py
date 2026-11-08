class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        s_dict = Counter(s)
        count = 0

        def is_stretchy(ww):
            ii=0
            jj=0

            """
            * s: heeellooo
            * w: hello
            """
            while ii < len(s) and jj < len(ww):
                if s[ii] != ww[jj]: return False
                # how many in S
                # how many in w
                s_count=1
                while ii < len(s)-1 and s[ii] == s[ii+1]:
                    ii += 1
                    s_count += 1
                
                w_count=1
                while jj < len(ww)-1 and ww[jj] ==ww[jj+1]:
                    jj += 1
                    w_count += 1
                
                if w_count > s_count: return False
                if s_count != w_count and s_count < 3: return False
                ii += 1
                jj += 1 
                
                
            return ii == len(s) and jj == len(ww)

        for ww in words:
            if is_stretchy(ww): count+=1

        return count
        