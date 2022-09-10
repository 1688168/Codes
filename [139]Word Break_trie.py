from functools import lru_cache
from collections import deque


class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = Node()

    def build_trie(self, s):
        if s is None or len(s) == 0: return
        itr = self.root
        for c in s:
            if c not in itr.children:
                itr.children[c] = Node()
            itr = itr.children[c]

        itr.is_word = True

    def is_word(self, w):
        if w is None or len(w) == 0: return False

        itr = self.root
        for c in w:
            if c not in itr.children:
                return False
            itr = itr.children[c]

        return itr.is_word

    def pt(self):
        itr = self.root
        lvl = 0

        dq = deque()
        for kk, vv in itr.children.items():
            dq.append((lvl + 1, kk, vv))

        while len(dq) > 0:
            sz = len(dq)
            for _ in range(sz):
                c = dq.popleft()  # got back a tuple from dq
                print(" lvl: ", c[0], " c: ", c[1], " is_word: ", c[2].is_word)
                for k, v in c[2].children.items():
                    dq.append((c[0] + 1, k, v))


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        : build a Trie
        : traverse all prefix see if a word
        : if true: recursive the remaining part with same trie until all original string are consumed
        """

        # 1. build Trie for wordDict
        t = Trie()
        for w in wordDict:
            t.build_trie(w)

        # t.pt()

        N = len(s)

        @lru_cache(None)
        def dfs(ss):
            # print(" the given ss: ", ss)
            if ss is None or len(ss) == 0: return True

            for ii in range(1, len(ss) + 1):
                # print(" checking: ", ss[:ii], " is_word: ", t.is_word(ss[:ii]))
                if t.is_word(ss[:ii]):
                    ans = dfs(ss[ii:])
                    if ans: return ans

            return False

        return dfs(s)