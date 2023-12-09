class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        """
        maximum possible height of the tallest building
        - DP, Binary Search, Greedy
        - looking for linear or logN

        """
        N = n
        h = [int(1e9)] * N

        # give the max per restriction
        for ii, hh in restrictions:
            h[ii-1] = hh  # rule 1

        # rule 2:
        h[0] = 0

        # rule 3:
        # from left-to-right
        for ii in range(1, N):
            h[ii] = min(h[ii-1]+1, h[ii])

        # from right-to-left
        for ii in reversed(range(N-1)):
            h[ii] = min(h[ii], h[ii+1]+1)

        return max(h)
