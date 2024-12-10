class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        N = len(s)
        def isPalindrome(ss):
            ii, jj = 0, len(ss)-1
            if ii==jj: return True
            while ii < jj:
                if ss[ii] != ss[jj]: return False
                ii+=1
                jj-=1
            #print( ss, " is palindrome")
            return True

        def allPalindrome(st, path):
            if st>=N: # when we reached the end of the string
                res.append(path)
                return
        
            for jj in range(st, N):
                if isPalindrome(s[st:jj+1]):         
                    allPalindrome(jj+1, path+[s[st:jj+1]])
            return
        
        path=[]
        allPalindrome(0, path)

        return res
        