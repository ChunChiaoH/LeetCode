class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        tmp =[[0 for _ in range(m+2)]] + [[0] + row + [0] for row in board] + [[0 for _ in range(m+2)]]
        
        def conv(y, x) -> int:
            return sum(tmp[y][x:x+3]) + sum(tmp[y+1][x:x+3]) + sum(tmp[y+2][x:x+3])
        
        s = 0
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                s = conv(i, j) - num
                if num == 1:
                    if s < 2:
                        board[i][j] = 0
                    elif 2 <= s <=3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if s == 3:
                        board[i][j] = 1
                
        