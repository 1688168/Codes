from collections import defaultdict, deque
from pprint import pprint as pp


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        1. build graph connecting all neighboring words
        2.shortest transformation -> BFS
        """
        g = defaultdict(set)
        word_set = set(wordList+[beginWord])
        letter_set = set()
        for w in word_set:
            for c in w:
                letter_set.add(c)

        # build graph
        for w in word_set:
            for ii, cc in enumerate(w):
                for c in letter_set:
                    if c == cc:
                        continue  # skip same letter to avoid self neighboring to self
                    t = w[:ii]+c+w[ii+1:]
                    if t in word_set:
                        g[w].add(t)

        # print(" ===== the graph =====")
        # pp(g)
        dq = deque([(beginWord, [beginWord])])
        visited = set()

        # BFS for shortest distance

        res = []
        done = False
        while (sz := len(dq)) > 0:
            # print(" sz: ", sz)

            """
            A -> {B, C} -> {D}
            """
            local_visited = set()
            for _ in range(sz):  # all nodes in same lvl
                curr, path = dq.popleft()
                if curr == endWord:
                    res.append(path)
                    done = True
                    continue
                if curr in visited:
                    continue
                local_visited.add(curr)
                for child in g[curr]:
                    # print(" path ", path)
                    dq.append((child, path+[child]))

            if done:
                break
            for v in local_visited:
                visited.add(v)

        return res
