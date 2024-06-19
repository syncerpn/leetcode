# pretty straightforward
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set(candyType)
        return min(len(types), len(candyType) // 2)