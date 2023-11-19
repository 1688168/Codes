class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        if w is None or len(w) == 0:
            return

        itr = self.root
        for c in w:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]

        itr.is_word = True

    def is_word(self, w):
        if w is None or len(w) == 0:
            return False
        itr = self.root
        for c in w:
            if c not in itr.children:
                return False
            itr = itr.children[c]

        return itr.is_word


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))  # sort by word length
        t = Trie()

        def dfs(s):
            if (N := len(s)) == 0:
                return True
            if s in memo:
                return False

            for sz in range(1, N+1):
                if t.is_word(s[:sz]) and dfs(s[sz:]):
                    return True

            memo.add(s)
            return False

        res = []
        for w in words:
            memo = set()
            if dfs(w):
                res.append(w)
            t.add(w)

        return res
