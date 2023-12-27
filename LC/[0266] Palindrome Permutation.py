class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c2cnt = collections.Counter(s)
        odd_cnt = 0
        for cc, ff in c2cnt.items():
            if ff % 2 == 1:
                odd_cnt += 1

        return odd_cnt <= 1
