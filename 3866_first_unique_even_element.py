# easy
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d = Counter(nums)
        for a in nums:
            if a % 2 == 0 and d[a] == 1:
                return a
        return -1