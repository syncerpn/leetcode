# same as n queens i
# counting instead of generating solutions
class Solution:
    def totalNQueens(self, n: int) -> int:
        # row = [False] * n
        col = [False] * n
        dgf = [False] * (2*n-1)
        dgb = [False] * (2*n-1)
        ans = [0]
        def backtrack(k, i, p):
            if k == 0:
                ans[0] += 1
            else:
                for j in range(n):
                    if not col[j] and not dgf[n-1+j-i] and not dgb[i+j]:
                        # row[i] = True
                        col[j] = True
                        dgf[n-1+j-i] = True
                        dgb[i+j] = True
                        p.append([i, j])
                        
                        backtrack(k-1, i+1, p)

                        p.pop()
                        dgf[n-1+j-i] = False
                        dgb[i+j] = False
                        col[j] = False
                        # row[i] = False

        backtrack(n, 0, [])
        return ans[0]
        