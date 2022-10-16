from collections import deque
from functools import lru_cache
class Node:
    def __init__(self):
        self.children={}
        self.is_word=False

class Trie:
    def __init__(self):
        self.root=Node()

    def add(self, w):
        itr=self.root

        for c in w:
            if c not in itr.children:
                itr.children[c]=Node()
            itr=itr.children[c]

        itr.is_word=True

    def is_word(self, w):
        itr=self.root
        for c in w:
            if c not in itr.children: return False

            itr=itr.children[c]
        return itr.is_word

    def pt(self):
        itr=self.root
        lvl=0

        dq=deque([itr])
        lvl=0
        while sz:=len(dq) > 0:
            for _ in range(sz):
                curr=dq.popleft()
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

        t=Trie()
        for w in wordDict: t.add(w)
        #t.pt()

        res=[]
        N=len(s)
        visited=set()
        #@lru_cache(None)
        def dfs(s, path):
            if s is None or len(s)==0:
                res.append(" ".join(path))
                return True

            if s in visited: return False
            visited.add(s)
            ans=False
            for sz in range(1, len(s)+1):
                if t.is_word(s[:sz]):
                    ans=dfs(s[sz:], path+[s[:sz]])
            visited.remove(s)
            return ans

        path=[]
        dfs(s, path)
        return res

        
