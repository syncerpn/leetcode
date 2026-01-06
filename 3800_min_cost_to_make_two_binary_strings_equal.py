# there are three ways to equalize the strings
# case0: flip all the mismatched
# case1: swap most of the mismatched and flip the rest
# case2: swap most of the mismatched, cross and swap the rest, and flip a single remaining one if any
class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        c = [0, 0]
        for a, b in zip(s, t):
            if a != b:
                c[int(a)] += 1
        
        c0, c1 = c
        # case0: flip all mismatched
        f = (c0 + c1) * flipCost

        # case1:
        sf = min(c0, c1) * swapCost + abs(c0 - c1) * flipCost

        # case2:
        scf = min(c0, c1) * swapCost + abs(c0 - c1) // 2 * (swapCost + crossCost) + abs(c0 - c1) % 2 * flipCost

        return min(f, sf, scf)