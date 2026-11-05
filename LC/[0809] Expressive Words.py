class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        s_dict = Counter(s)
        count = 0

        is_stretchy(ww):
            w_dict=Counter(ww)
            for kk, vv in w_dict.items():
                if kk not in s_dict: return False
                
            return True


        for ww in words:
            if is_stretchy(ww): count+=1

        return count
        