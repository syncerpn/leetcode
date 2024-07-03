class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i, m in enumerate(moves):
            ri, ci = m
            mat[ri][ci] = 2 * (i % 2) - 1
        for i in range(3):
            s = sum(mat[i])
            if s == 3:
                return "B"
            elif s == -3:
                return "A"
        
        for j in range(3):
            s = sum([mat[i][j] for i in range(3)])
            if s == 3:
                return "B"
            elif s == -3:
                return "A"
        
        s = mat[0][0] + mat[1][1] + mat[2][2]
        if s == 3:
            return "B"
        elif s == -3:
            return "A"
        
        s = mat[2][0] + mat[1][1] + mat[0][2]
        if s == 3:
            return "B"
        elif s == -3:
            return "A"
        
        return "Draw" if len(moves) == 9 else "Pending"