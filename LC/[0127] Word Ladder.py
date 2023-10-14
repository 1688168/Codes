################
# 20231014
################
from collections import deque, defaultdict
from collections import defaultdict, deque
from pprint import pprint as pp


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        - beginWord 
        - endWord
        - wordList
        - shortest transformation sequence -> BFS
        - need to build the graph first for the BFS
        - all words in lowercase letters -> try all letters
        - all words are unique
        ------------
        1. build the graph represending the neighboring words
        2. BFS to endword and return the path length as shortest distance
        """
        ans = 0
        word_set = set(wordList)
        word_set.add(beginWord)
        # print(" ===== word_set =====")
        # pp(word_set)
        if endWord not in word_set:
            return ans

        # build graph representing the connected words per rules
        g = collections.defaultdict(set)
        letter_set = set()  # all lowercase in scope letters
        for w in word_set:
            for c in w:
                letter_set.add(c)

        for w in word_set:
            for ii in range(len(w)):
                t = w
                for c in letter_set:
                    if c == w[ii]:
                        continue  # same letter just skip
                    t = t[:ii]+c+t[ii+1:]  # replace to a new word
                    if t in word_set:  # a valid neighoring word
                        g[w].add(t)

        # BFS to reach endWord
        dq = deque([beginWord])
        visited = set()
        lvl = 0
        # pp(g)
        while (sz := len(dq)) > 0:
            lvl += 1
            # print(" ============= lvl: ", lvl)
            for _ in range(sz):  # exhausting same level
                curr = dq.popleft()
                # print("curr: ", curr)
                if curr == endWord:
                    ans = lvl
                    return ans
                if curr in visited:
                    continue
                visited.add(curr)

                for child in (g[curr]):
                    dq.append(child)

        return ans

##############################################


class Solution:
    def ladderLength(self,
                     beginWord: str,
                     endWord: str,
                     wordList: List[str]) -> int:

        # build the graph
        g = defaultdict(set)
        word_set = set([beginWord]+wordList)
        # print("word_set :", word_set)
        for w in [beginWord]+wordList:
            # print(" adding w: ", w)
            wl = list(w)
            for ii in range(len(wl)):
                for jj in range(26):
                    cc = wl[ii]
                    nc = chr(ord('a')+jj)
                    if nc == cc:
                        continue
                    wl[ii] = nc
                    nw = "".join(wl)
                    wl[ii] = cc
                    if nw in word_set:
                        g[w].add(nw)
        # print(g)
        # BFS to count the levels reaching the ending word
        dq = deque([beginWord])
        visited = set()
        lvl = 0
        is_found = False
        while (sz := len(dq)) > 0:
            lvl += 1
            for _ in range(sz):
                cw = dq.popleft()

                if cw == endWord:
                    is_found = True
                    break

                if cw in visited:
                    continue
                visited.add(cw)
                for child in g[cw]:

                    dq.append(child)

            if is_found:
                break
        # print("is_found: ",is_found, " lvl: ", lvl)
        return lvl if is_found else 0


##########
# 20221115: TLE
##########


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        * shortest distance -> BFS
        """
        g = defaultdict(set)
        char_set = set()
        # all the used chars
        for w in [beginWord]+wordList:
            for c in w:
                char_set.add(c)

        # build the connected graph
        for w in [beginWord]+wordList:
            for ii in range(len(w)):  # change each char
                for c in char_set:
                    nw = w[:ii]+c+w[ii+1:]
                    if nw == w:
                        continue  # skip same word
                    g[w].add(nw)

        # now we have connected BFS to the end word

        dq = deque([beginWord])

        visited = set()
        lvl = 0
        while (sz := len(dq)) > 0:
            lvl += 1
            for _ in range(sz):
                curr = dq.popleft()

                if curr == endWord:
                    return lvl
                visited.add(curr)

                for child in g[curr]:
                    if child in visited:
                        continue
                    dq.append(child)

        # build graph with connected words that diff only with one char
        # from begin word BFS
        # add child by trying all 26 chars (avoid pairing with all existing words)

        return 0
