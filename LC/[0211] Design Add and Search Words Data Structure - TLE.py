"""
20230503: T: 88.47
"""
class TreeNode:
    def __init__(self):
        self.isWord=False
        self.children={}

class WordDictionary:

    def __init__(self):
        self.root=TreeNode()
                
    def addWord(self, word: str) -> None:
        itr = self.root
        for c in word:
            if c not in itr.children:
                itr.children[c]=TreeNode()
            itr=itr.children[c]
        itr.isWord=True
        

    def search(self, word: str) -> bool:
        itr=self.root
        
        def dfs(w, itr):
            if itr is None: return False        
            if w is None or len(w)==0: return itr.isWord

            if w[0] == ".":
                for kk, vv in itr.children.items():
                    res = dfs(w[1:], vv)
                    if res: return True
                return False
            else:
                if w[0] not in itr.children: return False
                itr=itr.children[w[0]]
                return dfs(w[1:], itr)

            return itr.isWord

        return dfs(word, itr)
        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)





class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        itr=self.root

        for c in word:
            if c not in itr.children:
                itr.children[c]=TrieNode()

            itr=itr.children[c]
        itr.is_word=True


    def search(self, word: str) -> bool:
        def dfs(w, itr):
            if itr is None: return False
            if w is None: return itr.is_word

            for ii, cc in enumerate(w):
                if cc == '.':
                    for kk, vv in itr.children.items():
                        ans = dfs(w[ii+1:], vv)
                        if ans: return True
                    return False
                else:
                    if cc not in itr.children: return False
                    itr=itr.children[cc]


            return itr.is_word

        return dfs(word, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
