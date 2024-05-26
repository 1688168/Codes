#####
# 20240525
#####
class Solution:
    def isPalindrome(self, s: str) -> bool:
        N=len(s)

        ll, rr = 0, N-1

        while ll<=rr:
            while ll < rr and not (s[ll].isalnum()): ll+=1
            while rr > ll and not (s[rr].isalnum()): rr-=1

            if s[ll].lower() != s[rr].lower(): return False

            ll+=1
            rr-=1
        
        return True

        

#####
# 20230619
#####


class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        ll, rr = 0, N-1
        while ll <= rr:
            # print(" ll: ", ll, " rr: ", rr)

            # (s[ll].isdigit() or s[ll].isalpha()):
            while ll < rr and not s[ll].isalnum():
                ll += 1

            # (s[rr].isdigit() or s[rr].isalpha()):
            while rr > ll and not s[rr].isalnum():
                rr -= 1

            cl = s[ll].lower()
            cr = s[rr].lower()
            # print(" cl: ", cl, " cr: ", cr)
            if cl != cr:
                return False
            ll += 1
            rr -= 1

        return True


#####
# 20220520
#####
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []
        for c in s:
            if (c := c.lower()).isalnum():
                t.append(c)

        # print(t)

        return t == t[::-1]


#############################

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = []
        for c in s:
            c = c.lower()
            if c.isalpha() or c.isnumeric():
                ns.append(c)

        ll, rr = 0, len(ns)-1
        while ll < rr:
            if ns[ll] != ns[rr]:
                return False
            ll += 1
            rr -= 1

        return True
