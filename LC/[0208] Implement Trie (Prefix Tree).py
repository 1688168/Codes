class TrieNode:
    def __init__(self):
        self.children={}
        self.is_word=False

class Trie:

    def __init__(self):
        self.root=TrieNode()


    def insert(self, word: str) -> None:
        itr=self.root
        for c in word:
            if c in itr.children:
                itr=itr.children[c]
            else:
                itr.children[c]=TrieNode()
                itr=itr.children[c]

        itr.is_word=True


    def search(self, word: str) -> bool:
        itr=self.root
        for c in word:
            if c not in itr.children: return False
            itr=itr.children[c]

        return itr.is_word


    def startsWith(self, prefix: str) -> bool:
        itr=self.root
        for c in prefix:
            if c not in itr.children: return False
            itr=itr.children[c]

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
