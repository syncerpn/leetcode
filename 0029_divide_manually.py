# bit manip, simply set bit 1 if accumulate sum with divisor left shift << number of bits is still smaller than dividend
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            return min(-dividend, (1<<31) - 1)
        
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        s = 0
        r = 0
        for i in range(32):
            if s + (divisor << (31-i)) <= dividend:
                r += 1 << (31-i)
                s += divisor << (31-i)
        
        return r if sign == 1 else -r