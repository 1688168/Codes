class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0]*n for _ in range(n)]
        self.p1_row = [0]*n
        self.p2_row = [0]*n

        self.p1_col = [0]*n
        self.p2_col = [0]*n

        self.p1_dia1 = 0
        self.p1_dia2 = 0
        self.p2_dia1 = 0
        self.p2_dia2 = 0
        self.N = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        # print(" player: ", player)
        # print(self.board)
        if player == 1:
            self.p1_row[row] += 1
            if self.p1_row[row] == self.N:
                return player
            self.p1_col[col] += 1
            if self.p1_col[col] == self.N:
                return player
            if col == row:
                self.p1_dia1 += 1
            if self.p1_dia1 == self.N:
                return player
            if row == self.N-col-1:
                self.p1_dia2 += 1
            if self.p1_dia2 == self.N:
                return player
        elif player == 2:
            self.p2_row[row] += 1
            if self.p2_row[row] == self.N:
                return player
            self.p2_col[col] += 1
            if self.p2_col[col] == self.N:
                return player
            if col == row:
                self.p2_dia1 += 1
            if self.p2_dia1 == self.N:
                return player
            if row == self.N-col-1:
                self.p2_dia2 += 1
            if self.p2_dia2 == self.N:
                return player

        else:
            msg = f"unexpected player=[{player}]"
            raise Exception(msg)

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
