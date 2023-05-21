from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])

        dirs=[(1, 0), (-1, 0), (0, 1), (0, -1)]


        char2freq={}

        for ii in range(m):
            for jj in range(n):
                char2freq[board[ii][jj]] = char2freq.get(board[ii][jj], 0) + 1

        def is_in_scope(ii, jj, visited):
            if (ii, jj) in visited: return False
            if ii < 0 or jj < 0 or ii >= m or jj >= n: return False
            return True

        def dfs(ii, jj, st, visited):
            if st >= len(word): return True
            if not is_in_scope(ii, jj, visited): return False
        
            if word[st] != board[ii][jj]: return False
            visited.add((ii, jj))
            for di, dj in dirs:
                ni, nj = ii+di, jj+dj
                if dfs(ni, nj, st+1, visited): return True
            
            visited.remove((ii, jj))            
            return False


        if word[0] not in char2freq or word[-1] not in char2freq: return False
        if char2freq[word[0]] > char2freq[word[-1]]: 
            word=word[::-1]

        for ii in range(m):
            for jj in range(n):
                c=board[ii][jj]
                if c == word[0]:
                    visited=set()
                    if dfs(ii, jj, 0, visited):
                        return True
        
        return False