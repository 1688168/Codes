
###################
# 20240407
###################
class Solution:
    def makePalindrome(self, s: str) -> bool:
        """
        Greedy: ll, rr
        => is palindrome
        N=10^5
        """
        N = len(s)

        is_palindrome = True
        ll, rr = 0, N-1
        cnt = 0
        while ll < rr:
            if s[ll] != s[rr]:
                if cnt >= 2:
                    return False
                cnt += 1
            ll += 1
            rr -= 1

        return is_palindrome
################


class Solution:
    def makePalindrome(self, s: str) -> bool:
        N = len(s)
        ll, rr = 0, N-1
        cnt = 0
        while ll < rr:
            if s[ll] != s[rr]:
                cnt += 1  # just break if cnt > 2
            ll += 1
            rr -= 1

        return cnt <= 2
