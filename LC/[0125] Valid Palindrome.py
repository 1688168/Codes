class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns=[]
        for c in s:
            c=c.lower()
            if c.isalpha() or c.isnumeric():
                ns.append(c)


        ll, rr = 0, len(ns)-1
        while ll < rr:
            if ns[ll] != ns[rr]: return False
            ll+=1
            rr-=1

        return True
