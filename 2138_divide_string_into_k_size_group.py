# fill and divide, simple
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        f = len(s) % k
        if f > 0:
            s += fill * (k - f)
        return [s[i:i+k] for i in range(0, len(s), k)]