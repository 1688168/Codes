class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))

        word_set = set()
        res = []

        def dfs(s):
            if (N := len(s)) == 0:
                return True

            if s in memo:
                return False
            for sz in range(1, N+1):
                if s[:sz] in word_set and dfs(s[sz:]):
                    return True

            memo.add(s)
            return False

        for w in words:
            memo = set()
            if dfs(w):
                res.append(w)
            word_set.add(w)
        return res
