# easy
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        A = "abcdefghijklmnopqrstuvwxyz"
        d = {25 - i: c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        W = {c: w for c, w in zip(A, weights)}
        M = [d[sum(W[c] for c in word) % 26] for word in words]
        return "".join(M)
