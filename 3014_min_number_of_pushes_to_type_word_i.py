# simple math
# lol, some posted solution claiming 100% with while loop are stupid
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        q = n // 8
        r = n % 8
        return 4 * (q * q + q) + r * (q + 1)