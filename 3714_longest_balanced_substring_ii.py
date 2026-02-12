# prefix sum
# and a bit of math equivalence transform/normalization to 0
class Solution:
    def longestBalanced(self, s: str) -> int:
        A = {"a": 0, "b": 1, "c": 2}
        n = len(s)
        d = [[0, 0, 0]]
        for c in s:
            d.append(d[-1][:])
            d[-1][A[c]] += 1
        
        ans = 0
        f = {}
        for i, (a, b, c) in enumerate(d):
            for k in [
                    ("abc", a - b, a - c),
                    ("ab", a - b, c),
                    ("bc", b - c, a),
                    ("ca", c - a, b),
                    ("a", b, c),
                    ("b", c, a),
                    ("c", a, b),
                ]:
                if k in f:
                    ans = max(ans, i - f[k])
                else:
                    f[k] = i
        return ans
