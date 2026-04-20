# easy
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        ans = inf
        for i, a in enumerate(cards):
            if a in d:
                ans = min(ans, i - d[a] + 1)
            d[a] = i
        return ans if ans < inf else -1