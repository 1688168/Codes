from collections import deque
class Node:
    def __init__(self):
        self.children={}
        self.is_word=False
        self.score=0


class Trie:
    def __init__(self):
        self.root=Node()

    def add(self, w):
        itr = self.root
        for c in w:
            if c not in itr.children:
                itr.children[c]=Node()
            itr=itr.children[c]
            itr.score += 1
        itr.is_word=True

    def is_word(self, w):
        itr=self.root

        for c in w:
            if c not in itr.children: return False
            itr=itr.children[c]

        return itr.is_word

    def get_score(self, w):
        itr=self.root

        ans=0
        for c in w:
            ans += itr.children[c].score
            itr = itr.children[c]
        return ans


    def pt(self):
        itr=self.root
        dq=deque([itr])

        lvl=0
        while (sz:=len(dq)) > 0:
            print(" ===== lvl: ======")
            for _ in range(sz):
                curr=dq.popleft()
                for kk, vv in curr.children.items():
                    print("lvl: ", lvl, " c: ", kk, " is_word: ", vv.is_word, " score: ", vv.score)
                    dq.append(vv)

            lvl += 1



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        rt

        a  b  c
           b
        b  c

        """
        t=Trie()
        for w in words:
            t.add(w)
        #t.pt()
        res=[]

        for w in words:
            res.append(t.get_score(w))



        return res

        
