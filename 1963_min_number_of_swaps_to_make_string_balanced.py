# stack, as usual with parentheses
# each swap, we can remove 2 pairs of parentheses
class Solution:
    def minSwaps(self, s: str) -> int:
        r = []
        k = 0
        n = 0
        for c in s:
            if c == "[":
                k += 1
            else:
                if k > 0:
                    k -= 1
                else:
                    n += 1
        return n - n // 2