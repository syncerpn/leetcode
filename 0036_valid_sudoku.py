# check with set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        VS = "0123456789"
        rs = [set() for _ in range(9)]
        cs = [set() for _ in range(9)]
        bs = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".": continue
                if v in rs[i]: return False
                rs[i].add(v)
                if v in cs[j]: return False
                cs[j].add(v)
                bi, bj = i // 3, j // 3
                if v in bs[bi][bj]: return False
                bs[bi][bj].add(v)
        return True