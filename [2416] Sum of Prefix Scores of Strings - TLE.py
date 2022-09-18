class Node:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.cnt=0

class Trie:

    def __init__(self):
        self.root = Node()
        self.prefix2cnt={}

    def build_trie(self, s):
        if s is None or len(s) == 0: return
        itr = self.root

        prefix=""
        for c in s:
            prefix += c
            self.prefix2cnt[prefix] = self.prefix2cnt.get(prefix, 0)+1
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
                print(" lvl: ", c[0], " c: ", c[1], " is_word: ", c[2].is_word, " child cnt: ", c[2].cnt)
                for k, v in c[2].children.items():
                    dq.append((c[0] + 1, k, v))



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t=Trie()
        for w in words:
            t.build_trie(w)

        #t.pt()
        #print(t.prefix2cnt)

        res=[]

        for w in words:
            prefix=""
            cnt=0
            for c in w:
                prefix+=c
                cnt += t.prefix2cnt.get(prefix, 0)
            res.append(cnt)

        return res
