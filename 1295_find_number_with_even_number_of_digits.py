# digit detaching is trivial
# this one is hacked to work with the given constraints, lol
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for n in nums:
            if 10 <= n <= 99 or 1000 <= n <= 9999 or n == 100000:
                c += 1
        return c