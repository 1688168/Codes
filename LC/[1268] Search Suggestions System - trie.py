"""
# Problem Statements:
1. Givne products and searchWord, 
on each char entered from searchWord, return 3 min lexical ordered products

# Solution 1: Trie
1. define Trie
2. build Trie from products
  - define self.children=[None]*26 # for lexical ordering, 26 TrieNodes

3. for each additional char into prefix
  - BFS the Child Branch from current until we have 3 matches
  
# solution 2: bisect
- sort the products
- por each accumulated_prefix, bisect_left the sorted product
- if next 3 (including current and less than N) elements share same prefix, output
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26 #for the sake of lexical ordering
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
            if len(matched) >= 3: # we only need top 3 results
                return

            if itr.is_word:
                matched.append(path)

            for ii in range(26): # traverse all children
                if itr.children[ii] is None: #ignore None child
                    continue

                dfs(itr.children[ii], path+chr(ord('a')+ii))
        # itr starts from root
        for ii, cc in enumerate(searchWord):
            prefix += cc

            # if itr is unable to decend, -> no more search results possible
            if itr.children[ord(cc)-ord('a')] is None:
                # all future search should return []

                for jj in range(ii, N): # the remaining searchWord all get [] search results
                    res.append([])
                break
            # itr keeps decending on each additional search word
            itr = itr.children[ord(cc)-ord('a')]
            matched = []
            dfs(itr, prefix)

            res.append(matched)

        return res
