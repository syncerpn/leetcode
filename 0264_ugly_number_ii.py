# beautiful solution
# glad i solved it myself
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        s = [1]
        i2, i3, i5 = 0, 0, 0
        n -= 1
        while n > 0:
            r2 = s[i2] * 2
            r3 = s[i3] * 3
            r5 = s[i5] * 5
            m = min(r2, r3, r5)
            s.append(m)
            i2 += r2 == m
            i3 += r3 == m
            i5 += r5 == m
            n -= 1
        return s[-1]