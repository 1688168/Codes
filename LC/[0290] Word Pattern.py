class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_lst = list(pattern)
        s = s.split(" ")
        if len(pattern_lst) != len(s):
            return False
        char2word = {}
        word2char = {}

        for ii, cc in enumerate(pattern_lst):
            if cc in char2word:
                if char2word[cc] != s[ii]:
                    print(" false 1: char2word: ", char2word,
                          " word2char: ", word2char)
                    return False
            else:
                if s[ii] in word2char:
                    print(" false 2: char2word: ", char2word,
                          " word2char: ", word2char)
                    return False
                char2word[cc] = s[ii]
                word2char[s[ii]] = cc

        return True
