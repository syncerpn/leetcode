# trivial counting with digit decompose O(nlog10n)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {0: 0}
        m = 0
        c = 0
        for i in range(1,n+1):
            s = 0
            while i:
                s += i % 10
                i //= 10
            if s not in d:
                d[s] = 0
            d[s] += 1
            if m < d[s]:
                m = d[s]
                c = 1
            elif m == d[s]:
                c += 1
        return c

# or maybe use dp O(n)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {0: 0}
        c = [0] * 4 * 9
        for i in range(1,n+1):
            q, r = divmod(i, 10)
            # d[i] is sum of all digits of i
            # the sum equals remainder, which is single digits, plus sum of quotient digits
            # sum of quotient digits is store in d[q]
            d[i] = d[q] + r
            c[d[i] - 1] += 1
        
        return c.count(max(c))