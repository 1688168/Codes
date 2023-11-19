class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0


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
            itr.count += 1
        itr.is_word = True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        - a word can be constructed by two other words -> length is longer
        - 
        """
        words.sort(key=lambda x: len(x))

        trie = Trie()
        res = []

        def dfs(st):

            if st >= N:
                return True
            if st in memo:
                return False
            itr = trie.root
            for ii in range(st, N):
                if w[ii] in itr.children:
                    itr = itr.children[w[ii]]
                    if itr.is_word and dfs(ii+1):
                        return True
                else:
                    break

            memo.add(st)

            return False

        for w in words:
            memo = set()
            N = len(w)
            # print(" checking w: ", w)
            if dfs(0):
                res.append(w)
            trie.add(w)

        return res
