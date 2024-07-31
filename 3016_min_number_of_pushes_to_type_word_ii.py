# fairly simple
class Solution:
    def minimumPushes(self, word: str) -> int:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        d = {c:i for i, c in enumerate(ALPHABET)}
        m = [1] * 8 + [2] * 8 + [3] * 8 + [4] * 2
        f = [0] * 26
        for c in word:
            f[d[c]] += 1
        f.sort(reverse=True)
        return sum(fi * mi for fi, mi in zip(f, m))
