# easy
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        for a, b in pairwise(word):
            if a == b:
                ans += 1
        return ans