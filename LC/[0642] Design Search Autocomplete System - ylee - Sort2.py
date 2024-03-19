from collections import defaultdict
from heapq import nsmallest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentence2cnt = defaultdict(int)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, sentence, freq):
        if sentence is None or len(sentence) == 0:
            return
        itr = self.root
        for c in sentence:
            if c not in itr.children:
                itr.children[c] = TrieNode()

            itr = itr.children[c]
            itr.sentence2cnt[sentence] += freq

        itr.is_word = True


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()

        for s, f in zip(sentences, times):
            self.trie.add(s, f)

        self.dead_end = False
        self.curr_sentence = ""
        self.itr = self.trie.root

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.add(self.curr_sentence, 1)
            self.dead_end = False
            self.curr_sentence = ""
            self.itr = self.trie.root

            return []

        self.curr_sentence += c
        if c not in self.itr.children or self.dead_end is True:
            self.dead_end = True

            return []

        self.itr = self.itr.children[c]
        sentences = [(freq, sentence)
                     for sentence, freq in self.itr.sentence2cnt.items()]
        sentences.sort(key=lambda x: (-x[0], x[1]))

        return [x[1] for x in sentences[:min(3, len(sentences))]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
