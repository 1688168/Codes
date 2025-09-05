class Solution:

    def dfs(self, arr, idx, memo, D):
        # visited
        if idx in memo: return memo[idx]

        # try jump to left per D
        res=1
        for kk in range(1, D+1):
            if idx-kk < 0: break
            if arr[idx-kk] >= arr[idx]: break
            res = max(res, 1+self.dfs(arr, idx-kk, memo, D))
        
        for kk in range(1, D+1):
            if idx+kk >= len(arr): break
            if arr[idx+kk] >= arr[idx]: break
            res = max(res, 1+self.dfs(arr, idx+kk, memo, D))

        # for ii in range(idx-1, max(-1, idx-D-1), -1): #jumping from idx to left up to D or 0
        #     if arr[ii] >= arr[idx]: break # cannot jump over something higher/equal in between
        #     res = max(res, 1+self.dfs(arr, ii, memo, D))
        # # try jump to right per D
        # for ii in range(idx+1, min(len(arr), idx+D+1)): #jumping from idx to left up to D or 0
        #     if arr[ii] >= arr[idx]: break # cannot jump over something higher/equal in between
        #     res = max(res, 1+self.dfs(arr, ii, memo, D))

        memo[idx]=res
        return res

    def maxJumps(self, arr: List[int], d: int) -> int:
        N=len(arr)
        memo={} #given an index, return the max steps we can jump from it
        res=1 #at least can visited one (starting) index
        for ii in range(N): #try each index and capture the max
            res = max(res, self.dfs(arr, ii, memo, d))

        return res

    """
    # D
    # N=1000
    # can start from any index -> need to try all: O(N)
    # if we jump to same index which we previously visited, we can reuse the previous result -> memorize (pruning)
    """
        