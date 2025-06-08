# much much easier than it looks like from the description
# simply, we just need the complexity of the first computer to be the smallest one
# then permutations of the others are just factorial of n - 1
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        p, t, n = complexity[0], 1, len(complexity)
        for i in range(1, n):
            if complexity[i] <= p:
                return 0
            t = t * i % MOD
        return t