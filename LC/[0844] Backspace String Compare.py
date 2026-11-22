class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk_s=[]
        stk_t=[]
        for c in s:
            if c=='#':
                if stk_s: stk_s.pop()
            else:
                stk_s.append(c)
        
        for c in t:
            if c=='#':
                if stk_t: stk_t.pop()
            else:
                stk_t.append(c)

        return "".join(stk_s) == "".join(stk_t)
        

        