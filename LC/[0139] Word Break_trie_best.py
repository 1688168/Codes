##########
# 20231028
##########
from collections import deque
from functools import lru_cache


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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        - S="LEETCODE"
        - build trie from wordDict: Time: O(N), space: O(N)
        - for ii in each char in s - check if is_word via trie: O(N) dfs
        - only lowercase letters
        """
        ans = False
        t = Trie()
        N = len(s)
        for w in wordDict:
            t.add(w)

        memo = set()

        def dfs(st):
            if st >= N:
                return True
            if st in memo:
                return False
            itr = t.root  # each time check is in dictionary, we start from root of the trie
            for ii in range(st, N):  # from st to x, can we find a word in dict?

                if (cc := s[ii]) in itr.children:
                    itr = itr.children[cc]
                else:
                    break
                if itr.is_word and dfs(ii+1):
                    return True

            memo.add(st)
            return False

        return dfs(0)


##########
# 20230915
##########


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def is_word(self, w):
        if w is None or len(w) == 0:
            return False

        itr = self.root
        for c in w:
            if c not in itr.children or itr.count == 0:
                return False
            itr = itr.children[c]

        return itr.is_word

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

    def remove(self, w):
        if w is None or len(w) == 0:
            return
        itr = self.root

        for c in w:
            if c not in itr.children:
                raise Exception(f"removing not existing word: {w}")
            itr.count -= 1
            itr = itr.children[c]

        itr.is_word = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        1. build trie for dict words
        2. can we find dfs that is a word for s[:ii] and dfs(ii+1)
        """
        N = len(s)
        trie = Trie()
        for w in wordDict:
            trie.add(w)

        @lru_cache(None)
        def dfs(st):
            if st >= N:
                return True

            itr = trie.root
            for ii in range(st, N):
                if (c := s[ii]) in itr.children:
                    itr = itr.children[c]
                    if itr.is_word and dfs(ii+1):
                        return True
                else:
                    break
            return False

        return dfs(0)


########################


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def pt(self):
        """
        level order print
        """
        dq = deque([self.root])

        lvl = 0
        while (sz := len(dq)) > 0:
            print(" ===== lvl ", lvl, " ===== ")
            for _ in range(sz):
                curr = dq.popleft()
                print(" is_word: ", curr.is_word, " count: ", curr.count)
                for child in curr.children:
                    print(" ", child + " ,", end="")
                    dq.append(curr.children[child])
            print("")

            lvl += 1

    def add(self, word):
        itr = self.root
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]
            itr.count += 1
        itr.is_word = True

    def is_word(self, word):
        itr = self.root

        for c in word:
            if c not in itr.children:
                return False
            itr = itr.children[c]

        return itr.is_word


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        * break s into words in wordDict
        * word lookup -> Trie
        1. build Trie for wordDict
        2. try break s via Trie -> recursion dfs
        3. use memo to avoid repeated search
        """
        ans = False
        t = Trie()
        for word in wordDict:
            t.add(word)
        # t.pt()

        memo = set()

        def dfs2(idx):
            if idx >= len(s):
                return True
            if idx in memo:
                return False

            """
            012345
            abcder
            """
            itr = t.root
            for ii in range(idx, len(s)):
                if s[ii] in itr.children:
                    itr = itr.children[s[ii]]
                    if itr.is_word and dfs2(ii+1):
                        return True
                else:
                    break

            memo.add(idx)
            return False

        # return dfs(s)
        return dfs2(0)
