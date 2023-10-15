# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

"""
Time: O(N) * 100 (words)
space: O(1) (26*6 is a constance)
"""


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = words[:]

        def update_candidates(matches, w):
            nonlocal candidates
            new_candidates = []

            for c in candidates:
                cnt = sum(a == b for a, b in zip(c, w))
                if matches == 0:
                    if cnt == 0:
                        new_candidates.append(c)
                else:
                    if cnt == matches:
                        new_candidates.append(c)

            candidates = new_candidates[:]

        def most_overlapped_word():
            score_board = [[0]*26 for _ in range(6)]

            # populate score_board for each char
            for w in candidates:
                for ii, cc in enumerate(w):
                    score_board[ii][ord(cc)-ord('a')] += 1

            # find the word with highest score to guess
            best_score = 0
            best_word = ""
            for w in candidates:
                score = 0
                for ii, cc in enumerate(w):
                    score += score_board[ii][ord(cc)-ord('a')]
                if score > best_score:
                    best_score = score
                    best_word = w
            return best_word

        while candidates:

            best_word = most_overlapped_word()
            matches = master.guess(best_word)

            if matches == 6:
                return
            # update candidates per filter
            update_candidates(matches, best_word)


#########################################################
#########################################################
class Solution(object):
    def findSecretWord(self, wordlist, master):

        def pair_matches(a, b):         # count the number of matching characters
            return sum(c1 == c2 for c1, c2 in zip(a, b))

        def most_overlap_word():
            # counts[i][j] is nb of words with char j at index i
            counts = [[0 for _ in range(26)] for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord("a")] += 1

            best_score = 0
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    # all words with same chars in same positions
                    score += counts[i][ord(c) - ord("a")]
                if score > best_score:
                    best_score = score
                    best_word = word

            return best_word

        # all remaining candidates, initially all words
        candidates = wordlist[:]
        while candidates:

            s = most_overlap_word()     # guess the word that overlaps with most others
            matches = master.guess(s)

            if matches == 6:
                return

            candidates = [w for w in candidates if pair_matches(
                s, w) == matches]   # filter words with same matches
