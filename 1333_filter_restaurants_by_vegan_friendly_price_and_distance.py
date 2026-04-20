# easy
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for i, r, v, p, d in restaurants:
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                ans.append((r, i))
        return [i for _, i in sorted(ans, reverse=True)]