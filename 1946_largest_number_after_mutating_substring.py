# greedy
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        d = {c: str(i) for c, i in zip("0123456789", change)}
        ans = ""
        f = 0
        for c in num:
            if f == 0:
                if d[c] > c:
                    f = 1
                    ans += d[c]
                else:
                    ans += c
            elif f == 1:
                if d[c] < c:
                    f = 2
                    ans += c
                else:
                    ans += d[c]
            elif f == 2:
                ans += c
        return ans
