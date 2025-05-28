# hard problem, yet quite easy lol
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        d, ans = 0, 0
        for c in target:
            if c > d:
                ans += c - d
            d = c
        return ans