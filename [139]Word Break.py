# Given a string s and a dictionary of strings wordDict, return true if s can 
# be segmented into a space-separated sequence of one or more dictionary words. 
# 
#  Note that the same word in the dictionary may be reused multiple times in 
# the segmentation. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple 
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 300 
#  1 <= wordDict.length <= 1000 
#  1 <= wordDict[i].length <= 20 
#  s and wordDict[i] consist of only lowercase English letters. 
#  All the strings of wordDict are unique. 
#  
# 
#  Related Topics Hash Table String Dynamic Programming Trie Memoization 👍 1211
# 9 👎 518


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache
class Solution:
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
        wordSet=set(wordDict)
        @lru_cache(None)
        def dfs(s):
            if s is None or len(s)==0 : return True
            for ii in range(1, N+1):
                cs=s[:ii]
                if cs in wordSet:
                    if dfs(s[ii:]): return True
            return False

        return dfs(s)
        
# leetcode submit region end(Prohibit modification and deletion)
