# math solution pure O(1)
# might not scale number of children very well lol
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > limit * 3:
            # there no way to make it
            return 0
        if n > limit * 2:
            # first child must take at least "a" and at most "limit" candies
            # then we can count the number of combs for the rest
            a = n - 2 * limit
            return (limit - a + 2) * (limit - a + 1) // 2
        if n > limit * 1:
            # case 1: first child may take 0 to "a-1" candies
            # case 2: first child takes at least "a" and at most "limit" candies
            # then we can count the number of combs for the rest in each case
            a = n - limit
            return (limit - a + 1) * (n + 2) // 2 + a * (limit - a) + a * (a + 1) // 2
        else:
            # this is pure comb because we dont need to care about overlimit
            return (n + 1) * (n + 2) // 2