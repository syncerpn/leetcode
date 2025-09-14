# easy
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        m = sum(nums) / len(nums)
        k = 1
        s = set(nums)
        while k <= m or k in s:
            k += 1
        return k
