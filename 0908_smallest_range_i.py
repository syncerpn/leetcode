# simply close the gap between max and min
# because you can apply the operation to any number
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n_min = min(nums)
        n_max = max(nums)
        return max(n_max - n_min - 2 * k, 0)