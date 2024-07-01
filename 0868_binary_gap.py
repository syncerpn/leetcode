# tracking "1" bit
class Solution:
    def binaryGap(self, n: int) -> int:
        s = None
        e = None
        i = 0
        l_max = 0
        while n:
            b = n % 2
            n = n >> 1
            if b == 1:
                if s is None:
                    s = i
                else:
                    if e is None:
                        e = i
                    else:
                        s, e = e, i
                    d = e - s
                    if d > l_max:
                        l_max = d
            i += 1
        return l_max