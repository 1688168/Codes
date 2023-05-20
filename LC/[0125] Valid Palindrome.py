#####
# 20220520
#####
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        for c in s:
            if (c:=c.lower()).isalnum(): t.append(c)
        
        #print(t)
        
        return t==t[::-1]
        


#############################

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
