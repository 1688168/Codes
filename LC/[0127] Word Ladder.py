from collections import defaultdict, deque
class Solution:
    def ladderLength(self,
                     beginWord: str,
                     endWord: str,
                     wordList: List[str]) -> int:

        # build the graph
        g=defaultdict(set)
        word_set=set([beginWord]+wordList)
        #print("word_set :", word_set)
        for w in [beginWord]+wordList:
            #print(" adding w: ", w)
            wl=list(w)
            for ii in range(len(wl)):
                for jj in range(26):
                    cc=wl[ii]
                    nc=chr(ord('a')+jj)
                    if nc==cc: continue
                    wl[ii]=nc
                    nw="".join(wl)
                    wl[ii]=cc
                    if nw in word_set:
                        g[w].add(nw)
        #print(g)
        # BFS to count the levels reaching the ending word
        dq=deque([beginWord])
        visited=set()
        lvl=0
        is_found=False
        while (sz:=len(dq)) > 0:
            lvl+=1
            for _ in range(sz):
                cw=dq.popleft()

                if cw==endWord:
                    is_found=True
                    break

                if cw in visited: continue
                visited.add(cw)
                for child in g[cw]:

                    dq.append(child)

            if is_found: break
        #print("is_found: ",is_found, " lvl: ", lvl)
        return lvl if is_found else 0


##########
# 20221115: TLE
##########
from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        * shortest distance -> BFS
        """
        g=defaultdict(set)
        char_set=set()
        # all the used chars
        for w in [beginWord]+wordList:
            for c in w:
                char_set.add(c)

        # build the connected graph
        for w in [beginWord]+wordList:
            for ii in range(len(w)): # change each char
                for c in char_set:
                    nw=w[:ii]+c+w[ii+1:]
                    if nw==w: continue # skip same word
                    g[w].add(nw)

        # now we have connected BFS to the end word

        dq=deque([beginWord])

        visited=set()
        lvl=0
        while (sz:=len(dq)) > 0:
            lvl+=1
            for _ in range(sz):
                curr=dq.popleft()

                if curr==endWord: return lvl
                visited.add(curr)

                for child in g[curr]:
                    if child in visited: continue
                    dq.append(child)


        # build graph with connected words that diff only with one char
        # from begin word BFS
        # add child by trying all 26 chars (avoid pairing with all existing words)


        return 0
