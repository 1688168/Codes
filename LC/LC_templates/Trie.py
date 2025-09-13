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
        : print tree
        """
        dq=deque([self.root])
        lvl=0
        while (sz:=len(dq)) > 0:
            print(" ===== ", lvl, " ===== ")
            for _ in range(sz):
                curr=dq.popleft()

                curr_node=""
                for kk, vv in curr.children.items():
                    curr_node += (kk+",")
                    dq.append(vv)
                print(" curr_node: ", curr_node, " is_word: ", curr.is_word,
                      " count: ", curr.count)
            lvl+=1

    def is_word(self, word):
        itr=self.root
        for c in word:
            if c not in itr.children:
                return False
            itr=itr.children[c]

        return itr.is_word

    def add_word(self, word):
        itr=self.root
        for c in word:
            if c not in itr.children:
                itr.children[c]=TrieNode()
            itr=itr.children[c]
            itr.count +=1
        itr.is_word=True

    def remove(self, word):
        itr=self.root
        for c in word:
            if c in itr.children:
                itr=itr.children[c]
                itr.count -=1