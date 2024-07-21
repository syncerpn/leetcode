# you should leave the first n minimum piles to bob
# then probably try to greedily take the alternating smaller pile every two piles
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort()
        return sum(piles[n::2])