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
