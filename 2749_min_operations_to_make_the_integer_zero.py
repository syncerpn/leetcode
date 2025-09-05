# math problem
# after some m operations, if just subtract num1 with num2
# we should have k = num1 - m * num2
# now that with 2^i to be subtracted from k for each m operation
# then k must be >= m because 2^i >= 1
# and that bit count of k must be <= m
# there is always a way to construct the sum of 2^i into k if the above condition is satisfied
# nice problem and i solved it
# thought of binary search initially, which is untrue because if m operations satisfies
# there is no guarantee that m+1 also satisfies
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        m = 0
        while (k := num1 - m * num2) >= 0:
            if k >= m >= bin(k)[2:].count("1"):
                return m
            m += 1
        return -1

# next time use bit_count instead of string conversion lol
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        m = 0
        while (k := num1 - m * num2) >= 0:
            if k >= m >= k.bit_count():
                return m
            m += 1
        return -1