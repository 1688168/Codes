class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        ss = []
        for w in s_list:
            if len(w) == 0:
                continue
            ss.append(w)

        ss.reverse()
        return " ".join(ss)
