class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def valid(x, y, board):
            # check column
            for i in range(x-1, -1, -1):
                if board[i][y] == 'Q':
                    return False
            
            # check top-left diagonal
            i, j = x-1, y-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # check top-right diagonal
            i, j = x-1, y+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True

        def helper(i, board):
            if i == n:
                ans.append(["".join(row) for row in board])
                return
            
            for j in range(n):
                if valid(i, j, board):
                    board[i][j] = 'Q'
                    helper(i + 1, board)
                    board[i][j] = '.'

        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        helper(0, board)
        return ans
