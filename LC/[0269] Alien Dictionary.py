#######
# 20221103
#######

from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        1. build graph. per words. with the order per dictionary rules
        2. topology sort
        3. confirm we can define a order complete all unique chars
        """

        g=defaultdict(set)
        idt={c:0 for w in words for c in w}

        # build the dictionary char relationship
        for ii, w1 in enumerate(words):
            for jj, w2 in enumerate(words[ii+1:]):
                if len(w1) > len(w2) and w1[:len(w2)] == w2: return ""
                for kk in range(min(len(w1), len(w2))):
                    if w1[kk] != w2[kk]:
                        if w2[kk] in g[w1[kk]]: break
                        g[w1[kk]].add(w2[kk])
                        idt[w2[kk]] +=1
                        break

        res=[]
        # topology sort
        dq=deque()
        for cc, ff in idt.items():
            if ff == 0: dq.append(cc)

        while len(dq) > 0:
            curr=dq.popleft()
            res.append(curr)
            for child in g[curr]:
                idt[child] -= 1
                if idt[child]==0:
                    dq.append(child)

        return "".join(res) if len(res)==len(idt) else ""

#####################################################
#####################################################
from collections import deque, defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        : return "" if no solution
        : return any solution if multiple -> DFS?
        : find order -> sort -> topology sort
        : 1. pair the words and find the order in graph
        : 2. topology sort for the order
        """
        # g=defaultdict(set)
        # arr=[]
        g=defaultdict(set)
        idt={c:0 for w in words for c in w}

        N=len(words)

        for ii, w1 in enumerate(words):
            for jj, w2 in enumerate(words[ii+1:]):
                if len(w1)>len(w2) and w1[:len(w2)]==w2: return ""
                for kk in range(min(len(w1), len(w2))):
                    if w1[kk]!=w2[kk]:
                        if w2[kk] in g[w1[kk]]: break
                        g[w1[kk]].add(w2[kk])
                        idt[w2[kk]] += 1
                        break

        # print(g)
        # print(idt)

        dq=deque()
        for kk, vv in idt.items():
            if vv==0: dq.append(kk)

        res=[]
        while sz:=len(dq) > 0:

            for _ in range(sz):
                curr=dq.popleft()
                res.append(curr)

                for child in g[curr]:
                    idt[child] -= 1
                    if idt[child]==0:
                        dq.append(child)


        if len(res)==len(g):
            return "".join(res)
        else:
            return ""
