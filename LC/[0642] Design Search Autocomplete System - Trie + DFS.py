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


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.s2freq = {s: f for (s, f) in zip(sentences, times)}
        self.trie = Trie()
        self.itr = self.trie.root

        for s in sentences:
            self.trie.add(s)

        self.curr_s = ""
        self.is_dead_end = False
        self.itr = self.trie.root

    def input(self, c: str) -> List[str]:
        if c == "#":

            self.s2freq[self.curr_s] = self.s2freq.get(self.curr_s, 0) + 1
            self.trie.add(self.curr_s)

            # reset to init state
            self.curr_s = ""
            self.is_dead_end = False
            self.itr = self.trie.root
            return []

        self.curr_s += c
        if c not in self.itr.children or self.is_dead_end is True:
            self.is_dead_end = True
            return []

        self.itr = self.itr.children[c]
        matched = []
        path = ""

        def dfs(itr, path):
            if itr is None:
                return
            if itr.is_word:
                matched.append(path)

            for cc, node in itr.children.items():
                dfs(node, path+cc)

        dfs(self.itr, self.curr_s)
        ss = [(self.s2freq.get(s, 0), s) for s in matched]
        ss.sort(key=lambda x: (-x[0], x[1]))
        # print(" ss: ", ss)
        return [ss[x][1] for x in range(min(3, len(ss)))]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
"""
- TrieNode
- Trie

* build all sentences into Trie
* for each input
** dfs all qualified words
** sort per (freq, lexical)

"""
