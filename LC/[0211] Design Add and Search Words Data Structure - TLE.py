
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
