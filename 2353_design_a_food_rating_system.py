# even though this solution passed
# i feel like we may push a lot of garbage into the heap
# so it is not really efficient
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.R = {f: r for f, r in zip(foods, ratings)}
        self.F = {f: c for f, c in zip(foods, cuisines)}
        self.C = {c: [] for c in cuisines}
        for f, c, r in zip(foods, cuisines, ratings):
            heapq.heappush(self.C[c], (-r, f))
        print(self.C)

    def changeRating(self, food: str, newRating: int) -> None:
        self.R[food] = newRating
        c = self.F[food]
        heapq.heappush(self.C[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rn, f = heapq.heappop(self.C[cuisine])
            if self.R[f] == -rn:
                heapq.heappush(self.C[cuisine], (rn, f))
                return f

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# someone also suggest using sorted set
# and we remove old rating as well to make it clean