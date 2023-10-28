
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        res = []

        def dfs(s, path):
            if (N := len(s)) == 0:
                res.append(" ".join(path))
                return

            for sz in range(1, N+1):
                if s[:sz] in words:
                    dfs(s[sz:], path+[s[:sz]])

            return

        path = []
        dfs(s, path)

        return res
