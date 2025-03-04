# easy with interval filtering
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        p, q = bounds[0]
        n = len(original)
        for i in range(1, n):
            d = original[i] - original[i-1]
            u, v = bounds[i]
            p += d
            q += d
            p = max(p, u)
            q = min(q, v)
        
        return max(0, q - p + 1)