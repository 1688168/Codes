class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        if t is None or s==t: return 1
        
        # @cache
        def helper(ss, tt):
            if len(tt)<=0 or ss==tt: return 1 #target is null or ss and tt are the same
            if len(ss) <= len(tt): return 0 # you cannot compose target that is longer than you

            if (ss, tt) in dp: return dp[(ss, tt)]

            dp[(ss, tt)] = helper(ss[:-1], tt) #none take
            if ss[-1]==tt[-1]: dp[(ss, tt)] += helper(ss[:-1], tt[:-1]) # you can take if last char is equal
            return dp[(ss, tt)] 

        return helper(s, t)