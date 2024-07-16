# greedily pick all numOnes then numZeros then the rest
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        a = min(numOnes, k)
        b = min(k - a, numZeros)
        c = k - a - b
        return a - c