"""
https://www.bilibili.com/video/BV1PG411n7FS/
"""
###############
# 20240114
###############
class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        """
        books[ii]: # of books on iith shelf
        * strictly fewer - monotonic
        => max books

        # Translation
        - given single list nums
        - find a subarray with max sum 
          where given jj s.t. ll<=jj<=rr
                nums[jj-1] < nums[jj] < nums[jj]
                nums[jj] can be any number btn [0, nums[jj]] 

        let dp[ii]: max books we can take when ending @ index=ii for nums
            dp[ii] = dp[jj]+sum(arithmatic sequence[jj+1:ii+1])

        => O(N^2): for each ii, we need to find jj s.t. nums[jj] is lower than expectation
        -> N=10^5 --> N^2 won't work 
        --> how do we reduce time-complexity?
        -> what's the best way to find the jj?
        -> what's the previous jj that is lower than expection?
        -> leverate monotonic stack to maintain prev jj that is lower than expectation.        
        """
        N = len(books)
        dp = [0]*N
        stk = []

        # for each nn, calc the max_book you can carry
        for ii, nn in enumerate(books):
            # remove those that is higher than expectation
            """
            7 8 9 10
                   i
                j    
            """
            while stk and books[stk[-1]] >= nn - (ii-stk[-1]):  # do you have enough to cover expectation?
                stk.pop()

            if stk:  # we have prev dp
                # jj=stk[-1]
                L = ii-stk[-1]

                dp[ii] = dp[stk[-1]] + (nn + books[ii]-L+1)*L//2
                # ^^^^^^^^^^^^^^^^^^^^^^^^^
                # current + expected_bottom
            else:
                L = min(ii+1, nn)
                dp[ii] = (nn+books[ii]-L+1)*L//2

            stk.append(ii)

        return max(dp)


##############################


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
        dp = [0]*N  # dp[ii] is the max number you can take ending @ shelf ii
        # dp[i]: max books can take ending with shelf i

        # leverage stack to transform O(N^2) <looking for j> to O(N) <ignore those not relevant>
        stk = []
        for ii in range(N):
            # find prev J
            # maintain the monotonic stack observes expectation (not just smaller)
            while len(stk) > 0 and books[ii]-(ii-stk[-1]) < books[stk[-1]]:
                stk.pop()  # pop those that is higher than the expectation

            """
            0 1 2 3 4 5
            1 2 3 7 8 9
                j     i
            """

            if len(stk) > 0:
                L = ii-stk[-1]
                dp[ii] = dp[stk[-1]] + (books[ii]+books[ii]-L+1)*L//2

            else:
                """
                //10 10 9
                 7    8 9

                // 10 10 10 10 10 3
                            1  2  3
                """

                L = min(ii+1, books[ii])  # number of elements.
                dp[ii] = (books[ii]+books[ii]-L+1)*L//2

            stk.append(ii)

        return max(dp)
