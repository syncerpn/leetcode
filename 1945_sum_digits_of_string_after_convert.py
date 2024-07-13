# just convert and calculate sum
# early stop if sum < 10, because there is only a single digit
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {c: str(i+1) for i, c in enumerate(ALPHABET)}
        n = ""
        for c in s:
            n += d[c]
        r = 0
        for _ in range(k):
            r = sum([int(c) for c in n])
            if r < 10:
                return r
            n = str(r)
        return r