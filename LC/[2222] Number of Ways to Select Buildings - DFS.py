from functools import lru_cache


class Solution:
    def numberOfWays(self, s: str) -> int:
        N = len(s)

        @lru_cache(None)
        def dfs(st, path):

            if len(path) == 3:
                # print("path: ", path)
                return 1

            if st >= N:
                return 0

            if len(path) == 0:
                return dfs(st+1, path+s[st])+dfs(st+1, path)
            else:
                if s[st] == path[-1]:
                    return dfs(st+1, path)
                else:
                    return dfs(st+1, path)+dfs(st+1, path+s[st])

        path = ""
        return dfs(0, path)
