class TicTacToe:

    def __init__(self, n: int):
        self.x = [0]*n
        self.y = [0]*n
        self.diagnal = 0
        self.antidiagnal = 0
        return

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else -1
        self.x[row] += currentPlayer
        self.y[col] += currentPlayer

        if row == col:
            self.diagnal += currentPlayer

        if col == len(self.y) - row - 1:
            self.antidiagnal += currentPlayer

        n = len(self.x)
        if abs(self.x[row]) == n or abs(self.y[col]) == n or abs(self.diagnal) == n or abs(self.antidiagnal) == n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
