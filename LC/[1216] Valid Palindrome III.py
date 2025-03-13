class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
      
        #can you remove most k chars to make s a palindrome
        """
        * break the string to two halves
        * min removal to make two string equal
        * return if min <=k
        * even: 6//2=3. [:3][3:]
        * odd: 7//2=3. [[:3][4:]
        """
        N=len(s)
        s1 = s

        s2 = s[::-1]
        s1="#"+s1
        s2="#"+s2

        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

        # for ii in range(N+1): dp[ii][0]=ii
        # for jj in range(N+1): dp[0][jj]=jj

        # print(" s1: ", s1)
        # print(" s2: ", s2)

        dp[0][0]=0

        for ii in range(1, N+1):
            for jj in range(1, N+1):
                if s1[ii]==s2[jj]:
                    dp[ii][jj]=dp[ii-1][jj-1]+1
                else:
                    dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])
        
        print(dp[-1][-1])

        return N-dp[-1][-1] <= k