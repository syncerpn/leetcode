# O(1) space solution is beautiful
# though its two pass
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = 0
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        r = 0
        for c in s[:-1]:
            if c == "0":
                zeros += 1
            else:
                ones -= 1
            r = max(r, ones + zeros)
        return r