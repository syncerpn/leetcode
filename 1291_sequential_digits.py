# easy
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for a in range(1, 10):
            b = a
            while a < 10 and b <= high:
                if b >= low:
                    ans.append(b)
                a += 1
                b = b * 10 + a
        return sorted(ans)