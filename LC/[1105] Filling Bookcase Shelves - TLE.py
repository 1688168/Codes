class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        book[ii]=[thickness_i, height_i]
        => min height
        * binary search: guess the answer and count (topK)
        * DP
        * Greedy - (sweep line, two-pointers)
        """
        N = len(books)
        memo = {}

        def dp(st, curr_w, curr_h, ttl_h):
            if st >= N:
                return ttl_h+curr_h

            if (st, curr_w, curr_h, ttl_h) in memo:
                return memo[(st, curr_w, curr_h, ttl_h)]

            thick, height = books[st]
            tke = math.inf
            if curr_w + thick <= shelfWidth:
                tke = dp(st+1, curr_w+thick, max(curr_h, height), ttl_h)
            ntk = math.inf
            if curr_w != 0:
                ntk = dp(st, 0, 0, ttl_h+curr_h)

            memo[(st, curr_w, curr_h, ttl_h)] = min(tke, ntk)
            return min(tke, ntk)

        return dp(0, 0, 0, 0)
