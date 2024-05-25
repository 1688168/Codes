class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        books = [[0, 0]]+books
        N = len(books)
        memo = {}
        for ii in range(N):
            memo[ii] = math.inf
        memo[0] = 0

        def dp(ed):
            if ed >= N:
                return

            max_height = 0
            ttl_width = 0
            for ii in reversed(range(1, ed+1)):  # for each level ending @ ed
                max_height = max(max_height, books[ii][1])
                ttl_width += books[ii][0]
                if ttl_width > shelfWidth:
                    break
                memo[ed] = min(memo[ed], memo[ii-1]+max_height)

            dp(ed+1)
        dp(1)
        return memo[N-1]
