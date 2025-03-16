# binary search obviously
# this solution is straight-forward
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_valid(m):
            return sum(int((m // r) ** 0.5) for r in ranks) >= cars
        
        l, r = 1, min(ranks) * cars * cars
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r

# but optimizing binary search solution is usually tied with early stopping
# in this case, probably applicable to other cases, we can early stop the condition
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_valid(m):
            s = 0
            for r in ranks:
                s += int((m // r) ** 0.5)
                if s >= cars:
                    return True
            return False
        
        l, r = 1, min(ranks) * cars * cars
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r

# also how about making "ranks" array more compact
# this works thanks to the specific constraint of this problem
# 1 <= rank_i <= 100 while 1 <= len(ranks) <= 10^5
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks = Counter(ranks)

        def is_valid(m):
            return sum(ranks[r] * int((m // r) ** 0.5) for r in ranks) >= cars
        
        m = min(ranks)
        l, r = 1, m * cars * cars
        while l < r:
            m = (l + r) // 2
            if is_valid(m):
                r = m
            else:
                l = m + 1
        return r