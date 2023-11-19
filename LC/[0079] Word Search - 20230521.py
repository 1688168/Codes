##############
# 20231118
##############
from collections import Counter


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(ii, jj, st, path):
            if st == len(word):
                return True
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False
            if word[st] != board[ii][jj]:
                return False
            if (ii, jj) in visited:
                return False
            visited.add((ii, jj))

            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if dfs(nx, ny, st+1, path+[word[st]]):
                    return True
            visited.remove((ii, jj))
            return False

        for ii in range(M):
            for jj in range(N):
                cc = board[ii][jj]
                if cc == word[0]:
                    path = []
                    visited = set()
                    if dfs(ii, jj, 0, path):
                        return True

        return False


##############
# 20230912
##############


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(st, ii, jj, path):
            # print(" st: ", st, " path: ", path, " wlen: ", len(word))
            if st >= len(word):
                return True
            if ii < 0 or ii >= M or jj < 0 or jj >= N:
                return False

            if (ii, jj) in visited:
                return False
            if board[ii][jj] != word[st]:
                return False

            visited.add((ii, jj))
            path.append(board[ii][jj])
            # print("path: ", path)
            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if dfs(st+1, nx, ny, path):
                    return True
            path.pop()
            visited.remove((ii, jj))
            return False

        for ii in range(M):
            for jj in range(N):
                visited = set()
                path = []
                # print("ii: ", ii, " jj: ", jj)
                if dfs(0, ii, jj, path):
                    return True
        return False


#####################################
# 20230521
#############


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        char2freq = {}

        for ii in range(m):
            for jj in range(n):
                char2freq[board[ii][jj]] = char2freq.get(board[ii][jj], 0) + 1

        def is_in_scope(ii, jj, visited):
            if (ii, jj) in visited:
                return False
            if ii < 0 or jj < 0 or ii >= m or jj >= n:
                return False
            return True

        def dfs(ii, jj, st, visited):
            if st >= len(word):
                return True
            if not is_in_scope(ii, jj, visited):
                return False

            if word[st] != board[ii][jj]:
                return False
            visited.add((ii, jj))
            for di, dj in dirs:
                ni, nj = ii+di, jj+dj
                if dfs(ni, nj, st+1, visited):
                    return True

            visited.remove((ii, jj))
            return False

        if word[0] not in char2freq or word[-1] not in char2freq:
            return False
        if char2freq[word[0]] > char2freq[word[-1]]:
            word = word[::-1]

        for ii in range(m):
            for jj in range(n):
                c = board[ii][jj]
                if c == word[0]:
                    visited = set()
                    if dfs(ii, jj, 0, visited):
                        return True

        return False
