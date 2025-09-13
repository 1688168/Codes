class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        g_min, g_max = arrays[0][0], arrays[0][-1]
        res=0
        for array in arrays[1:]:
            curr_min, curr_max = array[0], array[-1]
            res = max(res, abs(curr_max-g_min), abs(g_max-curr_min))
            g_min = min(g_min, curr_min)
            g_max = max(g_max, curr_max)
        return res

"""
* bruteforce: N^2
* on each min, we find max not in same row.
* when we observe we are repeating a lot of the pairing search, can we keep some info along the way traversing the matrix?
"""
        