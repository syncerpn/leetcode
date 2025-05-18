# easy
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, a in enumerate(nums):
            if sum(list(map(int, str(a)))) == i:
                return i
        return -1