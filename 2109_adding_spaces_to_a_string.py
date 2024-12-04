# fairly easy with python at least
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        ans = ""
        for i, c in enumerate(s):
            if j >= len(spaces):
                ans += s[i:]
                break
            if i == spaces[j]:
                j += 1
                ans += " "
            ans += c
        return ans