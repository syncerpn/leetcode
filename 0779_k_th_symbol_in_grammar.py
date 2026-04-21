# nice problem
# after a while
# it comes to a pattern
# by simply counting the number of one-bits
# because if we iterate each bit
# we know which (first or second) half the bit should come from
# each one-bit can be thought of as "invert of" the original bit (which is 0)
# so if we have 3 one-bits, it will be "invert of invert of invert of 0" which is 1
# therefore, we just need to count the one-bits
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        k -= 1
        f = False
        while k:
            if k & 1:
                f = not f
            k >>= 1
        return 1 if f else 0