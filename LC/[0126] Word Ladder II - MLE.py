#############
# 20231119
#############
from pprint import pprint as pp
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        word_set.add(beginWord)
        chars = set()
        g = collections.defaultdict(set)
        for w in word_set:
            for c in w:
                chars.add(c)

        # build graph
        for w in word_set:
            for ii, cc in enumerate(w):
                for c in chars:
                    if c == cc:
                        continue
                    t = w[:ii]+c+w[ii+1:]
                    if t in word_set:
                        g[w].add(t)
                        g[t].add(w)

        dq = collections.deque([[beginWord]])
        visited = set()
        res = []
        done = False
        while (sz := len(dq)) > 0 and not done:
            for _ in range(sz):
                curr_path = dq.popleft()
                curr = curr_path[-1]
                visited.add(curr)
                if curr == endWord:
                    res.append(curr_path)
                    done = True

                for child in g[curr]:
                    if child in visited:
                        continue
                    dq.append(curr_path+[child])

        return res

#######################


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
