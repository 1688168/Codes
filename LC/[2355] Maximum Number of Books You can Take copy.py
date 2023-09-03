"""
https://www.bilibili.com/video/BV1PG411n7FS/
"""


class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        * contiguous section -> subarray
        * strictly fewer books[i] < books[i+1]
        * max subarray
        * all subarray -> T: O(N^2) + maxbooksCanTake  -> bad

        * binary search: guess a number and check feasibility: logC * (is there a subarray that can make it) -> bad

        * DP: 
        dp[i]: max books can take ending with shelf i
        8 5 9 9 9
          j 7 8 9   
                i //take the full number of i
        dp[j]

        -> dp[j] + sum(arithmatic_sequence)
        -> finding J is O(N) 
        => we are still O(N^2)


        leveraging a stack only keep prev j
        """
        N = len(books)
        dp = [0]*N
        stk = []
        for ii in range(N):
            # find prev J
            while len(stk) > 0 and books[ii]-(ii-stk[-1]) < books[stk[-1]]:
                stk.pop()

            """
            0 1 2 3 4 5
            1 2 3 7 8 9
                j     i
            """

            if len(stk) > 0:
                L = ii-stk[-1]
                dp[ii] = dp[stk[-1]] + (books[ii]+books[ii]-L+1)*L//2

            else:
                L = min(ii+1, books[ii])
                dp[ii] = (books[ii]+books[ii]-L+1)*L//2

            stk.append(ii)

        return max(dp)
