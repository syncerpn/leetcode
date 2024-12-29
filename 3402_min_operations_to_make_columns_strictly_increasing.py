# fairly easy
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for c in zip(*grid):
            x = c[0]
            for y in c[1:]:
                if y <= x:
                    ans += x + 1 - y
                    x = x + 1
                else:
                    x = y
        return ans