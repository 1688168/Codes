###########
# 20231203
###########
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def dfs(s):
            if (N := len(s)) == 0:
                return True

            for ii in range(1, N+1):
                if s[:ii] in word_set and dfs(s[ii:]):
                    return True
            return False

        return dfs(s)


###########
# 20231028
###########


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)

        @cache
        def dfs(s):

            if (N := len(s)) == 0 or s is None:
                return True

            for ii in range(1, N+1):
                if s[:ii] in words and dfs(s[ii:]):
                    return True

            return False

        return dfs(s)


###########
# 20230604
###########


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)

        @lru_cache(None)
        def dfs(s):
            if s is None or len(s) == 0:
                return True
            for ii in range(1, len(s)+1):
                if s[:ii] in wordSet and dfs(s[ii:]):
                    return True
            return False

        return dfs(s)


###################
class Solution:
    """
    Time: O(N^3)
    space: O(N)
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. recursive:
           search prefix in the list
           ex: leetcode
           => l in the wordDict?
           => le in the wordDict?
           ...
           => leet in the wordDict -> recursive on remaining part of the string see if we can complete
        """
        N = len(s)
        wordSet = set(wordDict)

        @lru_cache(None)
        def dfs(s):
            if s is None or len(s) == 0:
                return True
            for ii in range(1, N+1):
                cs = s[:ii]
                if cs in wordSet:
                    if dfs(s[ii:]):
                        return True
            return False

        return dfs(s)


############
