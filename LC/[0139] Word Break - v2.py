from collections import deque
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.count=0

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def pt(self):
        """
        level order print
        """
        dq=deque([self.root])

        lvl=0
        while (sz:=len(dq)) > 0:
            print(" ===== lvl ", lvl, " ===== ")
            for _ in range(sz):
                curr=dq.popleft()
                print(" is_word: ", curr.is_word, " count: ", curr.count)
                for child in curr.children:
                    print(" ", child + " ,", end="")
                    dq.append(curr.children[child])
            print("")


            lvl += 1

    def add(self, word):
        itr=self.root
        for c in word:
            if c not in itr.children:
                itr.children[c]=TrieNode()
            itr=itr.children[c]
            itr.count += 1
        itr.is_word=True

    def is_word(self, word):
        itr=self.root

        for c in word:
            if c not in itr.children:
                return False
            itr=itr.children[c]

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
        ans=False
        t=Trie()
        for word in wordDict:
            t.add(word)
        #t.pt()

        memo=set()
        def dfs2(idx):
            if idx >= len(s): return True
            if idx in memo: return False

            """
            012345
            abcder
            """
            itr=t.root
            for ii in range(idx, len(s)):
                if s[ii] in itr.children:
                    itr=itr.children[s[ii]]
                    if itr.is_word and dfs2(ii+1): return True
                else:
                    break

            memo.add(idx)
            return  False

        #return dfs(s)
        return dfs2(0)
