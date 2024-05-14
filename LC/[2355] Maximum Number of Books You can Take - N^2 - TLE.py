"""
This is standard DP Type II solution with Time: O(N^2)
"""

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        N = len(books)

        dp=[0]*N

        for ii, nn in enumerate(books):
            if ii==0:
                dp[0]=nn
                continue
            
            if nn >= books[ii-1]+1:
                dp[ii]=dp[ii-1]+nn
            else:
                # we need to find jj that is NOT expected "arithmatic pregression"
                flag=False
                for jj in reversed(range(ii)):
                    expected = books[ii]-(ii-jj)
                    #print("ii: ", ii, "expected: ", expected)
                    if books[jj] < expected:
                        L=ii-jj
                        b=nn
                        a=nn-L+1
                        dp[ii]=dp[jj]+ (a+b)*L//2
                        flag=True
                        break
                
                if not flag: #not found
                    """
                    0 1 2
                    4 5 6
                    L=
                    """

                    L=min(ii+1, books[ii])
                    a=books[ii]-L+1
                    b=books[ii]
                    dp[ii]=(a+b)*L//2
            
        print(dp)
        return max(dp)
        