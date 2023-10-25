class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        dfs: MXN
        """
        M = len(grid)
        N = len(grid[0])

        ttl_cnt = 0

        visited = set()

        def dfs(ii, jj):

            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False, 0
            if (ii, jj) in visited:
                return True, 0
            if grid[ii][jj] == 0:
                return True, 0
            visited.add((ii, jj))

            is_valid1, n1 = dfs(ii+1, jj)
            is_valid2, n2 = dfs(ii-1, jj)
            is_valid3, n3 = dfs(ii, jj+1)
            is_valid4, n4 = dfs(ii, jj-1)

            return (is_valid1 and is_valid2 and is_valid3 and is_valid4, 1+n1+n2+n3+n4)

        for ii in range(M):
            for jj in range(N):
                is_valid, nn = dfs(ii, jj)

                if is_valid:
                    ttl_cnt += nn
                # print("is_valid: ", is_valid, "ii: ", ii, " jj: ", jj, " nn: ", nn, " ttl_cnt: ", ttl_cnt)

        return ttl_cnt
