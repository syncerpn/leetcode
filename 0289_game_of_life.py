# encoding:
# 2 means currently alive but dead next time
# -1 mean currently dead but alive next time
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == y == 0:
                            continue
                        if 0 <= i + x < m and 0 <= j + y < n:
                            neighbors += board[i+x][j+y] >= 1
                if board[i][j] <= 0:
                    if neighbors == 3:
                        board[i][j] = -1
                else:
                    if 2 > neighbors or neighbors > 3:
                        board[i][j] =  2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1
        