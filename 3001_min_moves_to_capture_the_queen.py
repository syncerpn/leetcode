# fairly easy
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == c == e and min(b, f) < d < max(b, f):
            return 2
        if b == d == f and min(a, e) < c < max(a, e):
            return 2
        if f - e == d - c == b - a and min(f, d) < b < max(f, d):
            return 2
        if f + e == d + c == b + a and min(f, d) < b < max(f, d):
            return 2
        if a != e and b != f and f - e != d - c and f + e != d + c:
            return 2
        return 1