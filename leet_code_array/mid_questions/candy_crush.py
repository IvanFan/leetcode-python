class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        todo = False
        R, C = len(board), len(board[0])
        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = abs(board[r][c]) * -1
                    board[r][c+1] = abs(board[r][c+1]) * -1
                    board[r][c+2] = abs(board[r][c+2]) * -1
                    todo = True

        for c in range(C):
            for r in range(R-2):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = abs(board[r][c]) * -1
                    board[r+1][c] = abs(board[r+1][c]) * -1
                    board[r+2][c] = abs(board[r+2][c]) * -1
                    todo = True

        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = abs(board[r][c])
                    wr = wr - 1
            for wrr in range(wr, -1, -1):
                board[wrr][c] = 0
        return self.candyCrush(board) if todo else board







