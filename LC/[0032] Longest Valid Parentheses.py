class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        )( ( ) ) ( )
                  i
                ^
                this is pop
        ^ this will stay in the stack as no matching parenthesis
        the longest valid parenthesis ending @ ii is => ans=max(ii-(stk[-1] if stk else -1), ans)       
        """
        stk = []  # parenthesis 50% is about stack, the other 50% is about greedy
        N = len(s)
        ans = 0
        for ii in range(N):
            if s[ii] == "(":
                stk.append(ii)
            else:
                if stk and s[stk[-1]] == "(":
                    stk.pop()
                    ans = max(ii-(stk[-1] if stk else -1), ans)
                else:
                    stk.append(ii)
        return ans
