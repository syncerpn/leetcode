# would be good to make an animation out of it
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(E, k):
            if k == len(E):
                return True
            i, j, b = E[k]
            for d in range(1, 10):
                if i not in R[str(d)] and j not in C[str(d)] and b not in B[str(d)]:
                    R[str(d)].append(i)
                    C[str(d)].append(j)
                    B[str(d)].append(b)
                    if backtrack(E, k+1):
                        return True
                    R[str(d)].pop()
                    C[str(d)].pop()
                    B[str(d)].pop()
            return False

        R = {str(d): [] for d in range(1, 10)}
        C = {str(d): [] for d in range(1, 10)}
        B = {str(d): [] for d in range(1, 10)}
        E = []
        for i in range(9):
            for j in range(9):
                d = board[i][j]
                if d.isdigit():
                    R[d].append(i)
                    C[d].append(j)
                    B[d].append(i // 3 * 3 + j // 3)
                else:
                    E.append((i, j, i // 3 * 3 + j // 3))
        
        backtrack(E, 0)
        for d in range(1, 10):
            for i, j in zip(R[str(d)], C[str(d)]):
                board[i][j] = str(d)
