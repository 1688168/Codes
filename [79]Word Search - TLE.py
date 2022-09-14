from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        : find path existance -> DFS
        : 1. locate the starting point
        : 2. try each starting point see if path exists
        """
        start_points=[]
        M=len(board)
        N=len(board[0])

        ctr=Counter(word)
        if ctr[word[0]] > ctr[word[-1]]:
            word=word[::-1]


        start_char=word[0]
        for ii in range(M):
            for jj in range(N):
                if board[ii][jj]==start_char:
                    start_points.append((ii, jj))



        dirs=[(1,0), (-1,0),(0,1),(0,-1)]

        def is_valid(xx, yy):
            if xx < 0 or yy < 0 or xx >=M or yy>=N:
                return False
            return True
        bad=set()
        visited=set()
        def dfs(xx, yy, ii):
            if ii >= len(word):
                return True

            if not is_valid(xx, yy):
                return False

            if board[xx][yy] != word[ii]: return False

            visited.add((xx, yy))


            if ii+1==len(word): return True

            for dx, dy in dirs:
                nx, ny = xx+dx, yy+dy

                if not is_valid(nx, ny): continue
                if (nx, ny) in visited: continue

                if dfs(nx, ny, ii+1):
                    return True

            visited.remove((xx, yy))

            return False




        for xx, yy in start_points:
            visited=set()

            if dfs(xx, yy, 0): return True

        return False
