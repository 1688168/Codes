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
