class Solution:
    def makePalindrome(self, s: str) -> bool:
        N = len(s)
        ll, rr = 0, N-1
        cnt = 0
        while ll < rr:
            if s[ll] != s[rr]:
                cnt += 1
            ll += 1
            rr -= 1

        return cnt <= 2
