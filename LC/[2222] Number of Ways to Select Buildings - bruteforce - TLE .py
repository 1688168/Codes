class Solution:
    def numberOfWays(self, s: str) -> int:

        def dfs(sz, st, path):
            nonlocal cnt
            if len(path) == 3:
                cnt += 1
                return
            if len(path) > 3:
                return

            for ii in range(st, N):
                if len(path) > 0 and s[ii] == path[-1]:
                    continue
                dfs(sz, ii+1, path+[s[ii]])

        N = len(s)
        cnt = 0
        path = []
        dfs(3, 0, path)
        return cnt
