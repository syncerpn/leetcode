# fairly ok
# just keep track of the last index of a character
class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        d = {}
        ans = ""
        t = 0
        for i, c in enumerate(s):
            if c in d and i - t - d[c] <= k:
                t += 1
            else:
                d[c] = i - t
                ans += c
        return ans