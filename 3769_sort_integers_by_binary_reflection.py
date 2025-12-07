# easy
class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda a: (int(bin(a)[2:][::-1], 2), a))