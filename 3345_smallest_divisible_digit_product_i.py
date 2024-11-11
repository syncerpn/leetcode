# will find one after a few iterations
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_prod(k):
            p = 1
            while k:
                p *= k % 10
                k //= 10
            return p
        
        while digit_prod(n) % t:
            n += 1
        return n