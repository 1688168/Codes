#############
# 20231203
#############
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        word_set = set(wordDict)
        dp = [False]*(N+1)
        dp[0] = True

        for ii in range(1, N+1):  # ii is the length
            for jj in reversed(range(ii)):
                if dp[jj] and s[jj:ii] in word_set:
                    dp[ii] = True
                if dp[ii]:
                    break

        return dp[-1]
#############
# 20231028
#############


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time: O(N^3): NXN array size, and string comparison in set lookup
        dp word break

        dp[ii] = True/False if s[:ii] can be broken into dictionary
               = dp[jj] and s[jj:ii+1] in word_set
        """
        N = len(s)
        words = set(wordDict)
        dp = [False]*(N+1)
        dp[0] = True  # for empty string, we can choose nothing from dict
        for ii in range(1, N+1):
            for jj in range(ii):
                dp[ii] = (dp[jj] and s[jj:ii] in words)
                if dp[ii]:
                    break

        return dp[N]


##################################
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Time: O(N^3): NXN array size, and string comparison in set lookup
        dp word break

        dp[ii] = True/False if s[:ii] can be broken into dictionary
               = dp[jj] and s[jj:ii+1] in word_set
        """
        N = len(s)
        dp = [False]*(N+1)  # length of s 0~N
        dp[0] = True
        word_set = set(wordDict)
        for ii in range(1, N+1):  # for each length
            for jj in range(ii):
                dp[ii] = dp[jj] and (s[jj:ii] in word_set)
                if dp[ii]:
                    break

        return dp[N]
