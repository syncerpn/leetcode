# either concat s with itself then result offset-k string
# or do this
# k may be larger than length of s
# so we need to cut it down a bit
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        k = k % len(s)
        return s[k:] + s[:k]