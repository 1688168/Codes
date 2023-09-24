class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, w):
        if w is None or len(w) == 0:
            return
        itr = self.root
        for c in w:
            idx = ord(c)-ord('a')
            if itr.children[idx] is None:
                itr.children[idx] = TrieNode()
            itr = itr.children[idx]
        itr.is_word = True


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        1. build trie
        2. dfs to find words on trie
        """
        trie = Trie()
        for p in products:  # build trie, space O(N), reduced duplicated path
            trie.add(p)

        res = []

        prefix = ""
        N = len(searchWord)
        itr = trie.root

        def dfs(itr, path):
            if len(matched) >= 3:
                return

            if itr.is_word:
                matched.append(path)

            for ii in range(26):
                if itr.children[ii] is None:
                    continue

                dfs(itr.children[ii], path+chr(ord('a')+ii))

        for ii, cc in enumerate(searchWord):
            prefix += cc
            if itr.children[ord(cc)-ord('a')] is None:
                # all future search should return []

                for jj in range(ii, N):
                    res.append([])
                break

            itr = itr.children[ord(cc)-ord('a')]
            matched = []
            dfs(itr, prefix)

            res.append(matched)

        return res
