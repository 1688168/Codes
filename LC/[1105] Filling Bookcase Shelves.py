class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        minimize the maximum of all the subarrays
        dp[ii]: the min possible height for books upto ii

        * if you know the min height of each jj before ii.
        -> min height ending @ ii is
        1. try each jj prior to ii @ same level until the current level could not fit
        2. jj-1 is the prev level and we know dp[jj] is the min hight @ jj
        """
        books = [[0, 0]]+books
        N = len(books)
        dp = [math.inf]*N
        dp[0] = 0  # height of zero books is zero
        for ii in range(1, N):
            max_height = 0  # current level height
            ttl_width = 0
            # for each ii as the last book on this level
            # jj is the first book of this level, jj could be ii
            for jj in reversed(range(1, ii+1)):
                # find the max height of current level
                max_height = max(max_height, books[jj][1])
                ttl_width += books[jj][0]
                if ttl_width > shelfWidth:
                    break
                dp[ii] = min(dp[ii], dp[jj-1]+max_height)

        return dp[-1]
