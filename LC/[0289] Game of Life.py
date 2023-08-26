class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        0-0: 0
        1-1: 1
        0-1: 2
        1-0: 3
        """
        M=len(board)
        N=len(board[0])
        # encoding to next stage
        dirs=[(1,0), (-1,0), (0, 1), (0,-1), (1, 1), (1,-1), (-1, 1), (-1, -1)]
        def neighbor_cnt(ii, jj):
            cnt = 0
            for dx, dy in dirs:
                nx, ny = ii+dx, jj+dy
                if nx < 0 or ny < 0 or nx >= M or ny >= N: continue
                if board[nx][ny] in (1, 3): cnt += 1

            return cnt
            
        for ii in range(M):
            for jj in range(N):
                cnt = neighbor_cnt(ii, jj)
                curr = board[ii][jj]
                if curr == 1 and cnt < 2:                    
                    board[ii][jj] = 3 
                elif curr == 1 and cnt in (2, 3):
                    board[ii][jj] = 1
                elif curr == 1 and cnt > 3:
                     board[ii][jj] = 3
                elif curr == 0 and cnt == 3:
                    board[ii][jj]=2
        
        for ii in range(M):
            for jj in range(N):
                if board[ii][jj] in (1, 2):
                    board[ii][jj]=1
                else:
                    board[ii][jj]=0

     
        # decoding to the next stage