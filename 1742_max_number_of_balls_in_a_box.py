# dp solution similar to #1399 for quickly calculating sum of digits
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {0:0}
        c = {}
        m = 0
        for n in range(highLimit+1):
            r = n % 10
            q = n // 10
            k = d[q] + r
            d[n] = k
            if n < lowLimit:
                continue
            if k not in c:
                c[k] = 0
            c[k] += 1
            m = max(m, c[k])
        return m

# or calculating sum of digits normally might be better when lowLimit much larger than 1
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = {}
        m = 0
        for n in range(lowLimit, highLimit+1):
            k = 0
            while n:
                k += n % 10
                n //= 10
            if k not in c:
                c[k] = 0
            c[k] += 1
            m = max(m, c[k])
        return m

# following solution is pretty fast
# its a combination of the best of both worlds
# dp without having to calcualte from the beginning
# the idea is to consider when a number ends with 0 that leads to spike (going down) in digit sum
# each time a number ends with 0, its digit sum is 9*n_zero-1 unit smaller than the previous number
# we have a variable j to keep track of the digit sum of previous number
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = [0] * 46
        l, j = lowLimit, 0
        while l > 0:
            j += l % 10
            l //= 10
        box[j] += 1
        for i in range(lowLimit + 1, highLimit + 1):
            while i % 10 == 0:
                j -= 9
                i //= 10
            j += 1
            box[j] += 1
        return max(box)