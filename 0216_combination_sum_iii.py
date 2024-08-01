# feel much more confident with backtracking now
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(s, k, l):
            if k == 0 and sum(s) == n:
                    ans.append(s[:])
            elif k <= 10 - l:
                for i in range(l, 10):
                    s.append(i)

                    backtrack(s, k-1, i+1)

                    s.pop()
        
        backtrack([], k, 1)
        return ans