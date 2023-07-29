from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        boxes=defaultdict(set)


        for ii in range(9):
            for jj in range(9):
                if board[ii][jj]==".": continue

                num=int(board[ii][jj])
                if num in rows[ii]: return False
                if num in cols[jj]: return False
                if num in boxes[(ii//3, jj//3)]: return False

                rows[ii].add(num)
                cols[jj].add(num)
                boxes[(ii//3, jj//3)].add(num)
            
        
        return True