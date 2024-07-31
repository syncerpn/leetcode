# backtracking practice
# or just use itertools combinations, lol
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, p):
            if p == 1:
                return [[j+1] for j in range(i, n)]
            ans = []
            for j in range(i, n):
                for c in backtrack(j+1, p-1):
                    ans.append([j+1] + c)
            return ans
        
        return backtrack(0, k)