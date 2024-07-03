# counting
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"a": 0, "b": 0, "l": 0, "o": 0, "n": 0}
        for c in text:
            if c in d:
                d[c] += 1
        
        return min([d["a"], d["b"], d["l"] // 2, d["o"] // 2, d["n"]])