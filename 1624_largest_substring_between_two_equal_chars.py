# track the first appearance of each character using hash map
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = {}
        l = -1
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                l = max(l, i - d[c] - 1)
        return l