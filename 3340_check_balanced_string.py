# easy
class Solution:
    def isBalanced(self, num: str) -> bool:
        s = [0, 0]
        for i, c in enumerate(num):
            s[i % 2] += int(c)
        return s[0] == s[1]