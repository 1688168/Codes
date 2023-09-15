#############
# 20230915
#############
from functools import lru_cache
from collections import deque


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
            if c not in itr.children:
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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        1. build trie for all words in wordDict: space: O(N)
        2. dfs s[st:ii]
        """
        trie = Trie()
        for w in wordDict:
            trie.add(w)

        res = []

        path = []
        N = len(s)

        memo = set()

        def dfs(st, path):
            if st >= N:
                res.append(" ".join(path))
                return True

            if st in memo:
                return False

            itr = trie.root
            flag = False
            for ii in range(st, N):
                if (c := s[ii]) in itr.children:
                    itr = itr.children[c]
                    if itr.is_word and dfs(ii+1, path+[s[st:ii+1]]):
                        flag = True
                else:
                    break

            if not flag:
                memo.add(st)
            return flag

        dfs(0, path)
        return res

######################################
######################################


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def pt(self):  # print Trie
        itr = self.root
        dq = deque([itr])
        lvl = 0
        while (sz := len(dq)) > 0:
            print(" ===== lvl: ", lvl, " =====")
            for _ in range(sz):
                curr = dq.popleft()
                print(" is_word: ", curr.is_word, ", cnt: ", curr.count)
                for kk, vv in curr.children.items():
                    print(kk, ", ", end="")
                    dq.append(vv)
                print(" | ", end="")
            print()
            lvl += 1

    def is_word(self, word):
        itr = self.root

        for c in word:
            if c not in itr.children:
                return False
            itr = itr.children[c]

        return itr.is_word

    def add(self, word):
        itr = self.root

        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]

        itr.is_word = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        : given a string and a list of words (dictionary)
        : output all space separated sentence that could be constructed from breaking the string per the dictionary
        : word lookup from dict -> build trie
        """
        t = Trie()
        for w in wordDict:
            t.add(w)
        # t.pt()

        res = []
        N = len(s)
        memo = set()

        def dfs(st, path):  # index into the string
            if st >= N:
                res.append(" ".join(path))
                return True

            if st in memo:
                return False

            flag = False
            for ii in range(st+1, N+1):
                if t.is_word(s[st:ii]) and dfs(ii, path + [s[st:ii]]):
                    flag = True

            if not flag:
                memo.add(st)

            return flag

        path = []
        dfs(0, path)

        return res


###########################################
###########################################


class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, w):
        itr = self.root

        for c in w:
            if c not in itr.children:
                itr.children[c] = Node()
            itr = itr.children[c]

        itr.is_word = True

    def is_word(self, w):
        itr = self.root
        for c in w:
            if c not in itr.children:
                return False

            itr = itr.children[c]
        return itr.is_word

    def pt(self):
        itr = self.root
        lvl = 0

        dq = deque([itr])
        lvl = 0
        while sz := len(dq) > 0:
            for _ in range(sz):
                curr = dq.popleft()
                for kk, vv in curr.children.items():
                    print("lvl: ", lvl, " kk: ", kk, " is_word: ", vv.is_word)
                    dq.append(vv)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        : given a string, construct all sentences where all words in the sentence are from the given word_dict
        : how do you look up from wordDict?
        : Output all paths -> DFS (shortest distance -> BFS)
        : part 1: try all sub-string -> O(N^2)

        : part 2: substring lookup
        : 1. list -> O(N) look up
        : 2. set  -> log(N) look up
        : 3. trie -> log(N) look up with space benefit
        """

        t = Trie()
        for w in wordDict:
            t.add(w)
        # t.pt()

        res = []
        N = len(s)
        visited = set()
        # @lru_cache(None)

        def dfs(s, path):
            if s is None or len(s) == 0:
                res.append(" ".join(path))
                return True

            if s in visited:
                return False
            visited.add(s)
            ans = False
            for sz in range(1, len(s)+1):
                if t.is_word(s[:sz]):
                    ans = dfs(s[sz:], path+[s[:sz]])
            visited.remove(s)
            return ans

        path = []
        dfs(s, path)
        return res
