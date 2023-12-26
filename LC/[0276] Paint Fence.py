class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        => the last two elements ending on k is depends on last two elements ending on k-1
        same[k]: # of methods that satisfy nums[k-1]==nums[k]
        diff[k]: # of methods that satisfy nums[k-1]!=nums[k]
        same[k]=diff[k-1]
        diff[k]=same[k-1]*(k-1)+diff[k-1]*(k-1)
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same = k
        diff = k*(k-1)
        N = n
        for ii in range(2, N):
            same_tmp = same
            diff_tmp = diff
            same = diff_tmp
            diff = (same_tmp + diff_tmp)*(k-1)

        return same+diff
