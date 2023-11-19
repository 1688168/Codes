#############
# 20231119
#############
from pprint import pprint as pp
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        word_set.add(beginWord)
        if endWord not in word_set:
            return []
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
                        # g[t].add(w)

        dq = collections.deque([beginWord])
        visited = set()
        res = []
        done = False
        lvl = 0
        g_prev = collections.defaultdict(set)
        # BFS define lvl
        while (sz := len(dq)) > 0 and not done:
            lvl += 1
            for _ in range(sz):
                curr = dq.popleft()

                if curr == endWord:
                    done = True
                    break
                if curr in visited:
                    continue
                visited.add(curr)
                for child in g[curr]:
                    g_prev[child].add(curr)
                    dq.append(child)
            if done:
                break

        visited = set()

        def dfs(curr, path):
            if curr == beginWord:
                res.append(path)
                return

            if len(path) >= lvl:
                return
            for prev in g_prev[curr]:
                if prev in visited:
                    continue
                visited.add(prev)
                dfs(prev, [prev]+path)
                visited.remove(prev)

        path = [endWord]
        dfs(endWord, path)

        return res

#############################


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        1. build graph connecting all neighboring words
        2.shortest transformation -> BFS
        """
        g = defaultdict(set)
        g_prev = defaultdict(set)
        word_set = set(wordList+[beginWord])
        if endWord not in word_set:
            return []
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
        dq = deque([beginWord])
        visited = set()

        # BFS for shortest distance

        done = False
        lvl = 0
        while (sz := len(dq)) > 0:
            # print(" sz: ", sz)
            lvl += 1
            """
            A -> {B, C} -> {D}
            """

            for _ in range(sz):  # all nodes in same lvl
                curr = dq.popleft()
                if curr == endWord:
                    done = True
                    break

                if curr in visited:
                    continue
                visited.add(curr)
                for child in g[curr]:
                    # print(" path ", path)
                    dq.append(child)
                    g_prev[child].add(curr)

            if done:
                break

        res = []
        visited = set()

        def dfs(curr, path):
            if curr == beginWord:
                res.append(path)
                return
            if len(path) >= lvl:
                return

            for prev in g_prev[curr]:
                if prev in visited:
                    continue
                visited.add(prev)
                dfs(prev, [prev]+path)
                visited.remove(prev)

        path = [endWord]
        dfs(endWord, path)

        return res
