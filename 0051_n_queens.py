class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = [False] * n
        col = [False] * n
        dgf = [False] * (2*n-1)
        dgb = [False] * (2*n-1)
        ans = []
        def backtrack(k, p):
            if k == 0:
                t = [["."] * n for _ in range(n)]
                for i, j in p:
                    t[i][j] = "Q"
                t = ["".join(ti) for ti in t]
                ans.append(t)
            else:
                for i in range(n):
                    if row[i]:
                        continue
                    row[i] = True
                    for j in range(n):
                        if col[j]:
                            continue
                        col[j] = True
                        if not dgf[n-1+j-i] and not dgb[i+j]:
                            dgf[n-1+j-i] = True
                            dgb[i+j] = True
                            p.append([i, j])
                            
                            backtrack(k-1, p)

                            p.pop()
                            dgf[n-1+j-i] = False
                            dgb[i+j] = False
                        col[j] = False
                    row[i] = False

        backtrack(n, [])
        return ans