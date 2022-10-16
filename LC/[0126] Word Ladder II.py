from collections import defaultdict, deque
class Solution:
    def findLadders(self,
                     beginWord: str,
                     endWord: str,
                     wordList: List[str]) -> int:

        # build the graph
        g=defaultdict(set)
        word_set=set([beginWord]+wordList)
        if endWord not in word_set: return []
        my_ancestors=defaultdict(set)
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
                    my_ancestors[child].add(cw)
                    dq.append(child)

            if is_found: break

        if not is_found: lvl=0
        #print(my_ancestors)
        paths=[]
        path=[]
        visited=set()
        def dfs(curr, path):
            if curr==beginWord:
                if (len(path)+1) == lvl:
                    paths.append([curr]+path)
                return

            if len(path)>= lvl: return

            for parent in my_ancestors[curr]:
                if parent in visited: continue
                visited.add(parent)

                dfs(parent, [curr]+path)
                visited.remove(parent)

        #print("lvl: ", lvl)
        dfs(endWord, path)

        return paths
