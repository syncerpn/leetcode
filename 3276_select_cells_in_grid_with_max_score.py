# since the constraints are fairly small
# backtracking is obvious
# however, it was lte
# so some early stopping conditions are essential
# one of them is to calculate the max sum for all subsequent grid with prefix sum and sorting
# the following solution is made during the contest
# so it might not be very clean and compact
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        grid = [sorted(list(set(g)), reverse=True) for g in grid]
        acc = []
        t = 0
        for g in grid[::-1]:
            t += g[0]
            acc.append(t)
        acc = acc[::-1]
        m = len(grid)
        ans = [0]
        def backtrack(v, i, s):
            if i == m:
                ans[0] = max(ans[0], s)
            else:
                if s + acc[i] < ans[0]:
                    return True
                early_stop = False
                for c in grid[i]:
                    if c not in v:
                        v.add(c)
                        s += c
                        early_stop = backtrack(v, i+1, s)
                        s -= c
                        v.discard(c)
                    if early_stop:
                        break
                else:
                    backtrack(v, i+1, s)
            return False
        backtrack(set(), 0, 0)
        return ans[0]